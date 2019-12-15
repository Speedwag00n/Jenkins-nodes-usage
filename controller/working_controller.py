import json

from flask import request
from flask_restplus import Namespace, Resource

from dto.usage_dto import UsageDto
from dto.working_dto import WorkingDto
from service.working_service import *

working_namespace = Namespace('api/working', description='Request for track node working processes')


@working_namespace.route('/start')
class WorkingStart(Resource):
    @working_namespace.doc(description='Node started do task request')
    @working_namespace.expect(WorkingDto.working_dto, validate=True)
    def post(self):
        start_working(data=json.loads(request.data))
        pass


@working_namespace.route('/stop')
class WorkingStop(Resource):
    @working_namespace.doc(description='Node finished do task request')
    @working_namespace.expect(WorkingDto.working_dto, validate=True)
    def post(self):
        stop_working(data=json.loads(request.data))
        pass


@working_namespace.route('/usage/<node_name>')
class WorkingStats(Resource):
    @working_namespace.marshal_with(UsageDto.usage_dto)
    @working_namespace.param(name='date', description='Date when node was used (example: 2019-12-31)')
    @working_namespace.doc(description='Get how many hours node was in use')
    def get(self, node_name):
        date = request.args.get("date")
        return get_node_usage(node_name, date)
