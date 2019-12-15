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
    worked = 0

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
            raise NodeNotFoundException
        else:
            if action_day_before.activated:
                worked = 24
            else:
                worked = 0
            return {
                "date": string_date,
                "hours": worked
            }
    hours_for_job = 0

    for record in records:
        hours = record.time.hour
        if record.activated:
            hours_for_job += 24 - hours
            worked += hours_for_job
            hours_for_job = 0
        else:
            hours_for_job -= 24 - hours

    #if node started do job previous day
    if hours_for_job < 0:
        worked += 24 + hours_for_job

    return {
        "date": string_date,
        "hours": worked
    }


def save_working_record(working):
    database.session.add(working)
    database.session.commit()


class NodeNotFoundException(Exception):
    pass