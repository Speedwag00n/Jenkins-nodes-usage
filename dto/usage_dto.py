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
