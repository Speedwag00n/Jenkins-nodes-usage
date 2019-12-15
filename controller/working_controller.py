import json

from flask import request
from flask_restplus import Namespace, Resource

from dto.usage_dto import UsageDto
from dto.working_dto import WorkingDto
from service.working_service import *

working_namespace = Namespace('api/working', description='Requests for track node working processes')


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


@working_namespace.route('/usage/one_day/<node_name>')
class WorkingStatsOneDay(Resource):
    @working_namespace.marshal_with(UsageDto.usage_dto)
    @working_namespace.param(name='date', description='Date when node was in use (example: 2019-12-31)')
    @working_namespace.doc(description='Get how many hours node was in use in specified day')
    def get(self, node_name):
        date = request.args.get("date")
        return get_node_usage_one_day(node_name, date)


@working_namespace.route('/usage/period/<node_name>')
class WorkingStatsPeriod(Resource):
    @working_namespace.marshal_with(UsageDto.usage_dto, as_list=True)
    @working_namespace.param(name='start_date', description='First date of period when node was in use (example: 2019-12-31)')
    @working_namespace.param(name='stop_date', description='Last date of period when node was in use (example: 2019-12-31)')
    @working_namespace.doc(description='Get how many hours node was in use in each day of specified period')
    def get(self, node_name):
        start_date = request.args.get("start_date")
        stop_date = request.args.get("stop_date")
        return get_node_usage_period(node_name, start_date, stop_date)
