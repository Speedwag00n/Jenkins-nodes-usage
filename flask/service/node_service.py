from app import database

from model.working import Working


def get_nodes_names():
    records = database\
        .session\
        .query(Working.node_name)\
        .distinct()\
        .all()
    a = 1
    return records
