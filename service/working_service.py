import datetime

from sqlalchemy import desc

from app import database
from model.working import Working
from dto.usage_dto import UsageDto


date_pattern = '%Y-%m-%d'


def start_working(data):
    working = Working(
        node_name=data['node_name'],
        activated=True,
        time=datetime.datetime.now()
    )
    save_working_record(working)


def stop_working(data):
    working = Working(
        node_name=data['node_name'],
        activated=False,
        time=datetime.datetime.now()
    )
    save_working_record(working)


def get_node_usage_one_day(node_name, string_date):
    date = datetime.datetime.strptime(string_date, date_pattern)
    seconds = get_node_usage_in_seconds(node_name, date)
    return {"date": date.date(), "duration": seconds}


def get_node_usage_period(node_name, string_start_date, string_stop_date):
    start_date = datetime.datetime.strptime(string_start_date, date_pattern)
    stop_date = datetime.datetime.strptime(string_stop_date, date_pattern)
    current_date = start_date
    usages = list()
    while current_date <= stop_date:
        usages.append(
            {
                "date": current_date.date(),
                "duration": get_node_usage_in_seconds(node_name, current_date)
            }
        )
        current_date += datetime.timedelta(days=1)
    return usages


def get_node_usage_in_seconds(node_name, date):
    now = datetime.datetime.now()

    if now.date() < date.date():
        return 0

    records = Working\
        .query\
        .filter_by(node_name=node_name)\
        .filter(Working.time >= date)\
        .filter(Working.time < (date + datetime.timedelta(days=1)))\
        .order_by(desc(Working.time))\
        .all()
    if len(records) == 0:
        action_day_before = Working\
            .query\
            .filter_by(node_name=node_name)\
            .filter(Working.time < date)\
            .order_by(desc(Working.time))\
            .first()
        if action_day_before is None:
            return 0
        else:
            if action_day_before.activated:
                if now.date() == date.date():
                    return get_duration(now, False)
                else:
                    return 24 * 60 * 60
            else:
                return 0

    worked = 0
    seconds_for_job = 0

    for record in records:
        time = record.time
        if record.activated:
            if seconds_for_job == 0 and now.date() == date.date():
                seconds_for_job -= get_duration(now)
            seconds_for_job += get_duration(time)
            worked += seconds_for_job
            seconds_for_job = 0
        else:
            seconds_for_job -= get_duration(time)

    #if node started do job previous day
    if seconds_for_job < 0:
        worked += 24 * 60 * 60 + seconds_for_job
    return worked


def get_duration(time, from_end=True):
    seconds = time.second + time.minute * 60 + time.hour * 60 * 60
    if from_end:
        return 24 * 60 * 60 - seconds
    else:
        return seconds


def save_working_record(working):
    database.session.add(working)
    database.session.commit()
