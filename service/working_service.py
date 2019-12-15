import datetime

from sqlalchemy import desc

from app import database
from model.working import Working


date_pattern = '%Y-%m-%d'


def start_working(data):
    working = Working(
        node_name=data['node_name'],
        activated=True
    )
    save_working_record(working)


def stop_working(data):
    working = Working(
        node_name=data['node_name'],
        activated=False
    )
    save_working_record(working)


def get_stats(node_name, string_date):
    date = datetime.datetime.strptime(string_date, date_pattern)

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
                return 24 * 60 * 60
            else:
                return 0
        return worked

    worked = 0
    hours_for_job = 0

    for record in records:
        time = record.time
        if record.activated:
            hours_for_job += get_duration(time)
            worked += hours_for_job
            hours_for_job = 0
        else:
            hours_for_job -= get_duration(time)

    #if node started do job previous day
    if hours_for_job < 0:
        worked += 24 * 60 * 60 + hours_for_job
    return worked


def get_duration(time):
    seconds = 24 * 60 * 60 - (time.second + time.minute * 60 + time.hour * 60 * 60)
    return seconds


def save_working_record(working):
    database.session.add(working)
    database.session.commit()
