from flask_restplus import fields

from app import api

working_dto = api.model(
    'Working_DTO',
    {
        'node_name': fields.String(required=True, desription='Node name that did action')
    }
)
