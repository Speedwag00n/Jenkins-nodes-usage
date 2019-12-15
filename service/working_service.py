import datetime

from sqlalchemy import desc

from app import database
from model.working import Working


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


def get_stats(node_name):
    records = Working.query.filter_by(node_name=node_name).order_by(desc(Working.time)).all()
    if len(records) == 0:
        raise NodeNotFoundException
    worked = 0
    hours_for_job = 0
    date_now = datetime.datetime.now().date()

    for record in records:
        current_date = record.time.date()
        difference_in_days = (date_now - current_date).days
        #skip current day
        if difference_in_days == 0:
            continue
        #skip previous day
        if difference_in_days > 1:
            break
        hours = record.time.hour
        if record.activated:
            hours_for_job += 24 - hours
            worked += hours_for_job
            hours_for_job = 0
        else:
            hours_for_job -= 24 - hours

    #if node started do job previous day
    if hours_for_job < 0:
        worked += - hours_for_job

    return {
        "date": date_now.strftime('%Y-%d-%m'),
        "hours": worked
    }


def save_working_record(working):
    database.session.add(working)
    database.session.commit()


class NodeNotFoundException(Exception):
    pass