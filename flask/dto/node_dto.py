from flask_restplus import fields

from app import api


class NodeDto:
    node_dto = api.model(
        'Node_DTO',
        {
            'name': fields.String(description='Node name')
        }
    )
