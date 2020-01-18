from flask_restplus import fields

from app import api


class WorkingDto:
    working_dto = api.model(
        'Working_DTO',
        {
            'node_name': fields.String(required=True, desription='Node name that did action')
        }
    )
