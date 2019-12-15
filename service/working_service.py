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
    return {"stats": "none for " + node_name}


def save_working_record(working):
    database.session.add(working)
    database.session.commit()
