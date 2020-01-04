from flask_restplus import fields

from app import api


class UsageDto:
    usage_dto = api.model(
        'Usage_DTO',
        {
            'date': fields.String(description='Analysed date'),
            'duration': fields.Integer(desription='How many second node was is use')
        }
    )


class NodeUsageDto:
    node_usage_dto = api.model(
        'Node_Usage_DTO',
        {
            'node_name': fields.String(description='Node name'),
            'usages': fields.List(fields.Nested(UsageDto.usage_dto), description='Node usage')
        }
    )
