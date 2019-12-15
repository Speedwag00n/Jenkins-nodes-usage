import json

from flask import request
from flask_restplus import Namespace, Resource

from dto.working_dto import working_dto
from service.working_service import *

working_namespace = Namespace('api/working', description='Request for track node working processes')


@working_namespace.route('/start')
class WorkingStart(Resource):
    @working_namespace.doc(description='Node started do task request')
    @working_namespace.expect(working_dto, validate=True)
    def post(self):
        start_working(data=json.loads(request.data))
        pass


@working_namespace.route('/stop')
class WorkingStop(Resource):
    @working_namespace.doc(description='Node finished do task request')
    @working_namespace.expect(working_dto, validate=True)
    def post(self):
        stop_working(data=json.loads(request.data))
        pass


@working_namespace.route('/stats')
class WorkingStats(Resource):
    @working_namespace.param(name='nodeName', description='Node name')
    @working_namespace.doc(responses={404: 'Node not found'})
    @working_namespace.doc(description='Get stats about node usage')
    def get(self):
        node_name = request.args.get("nodeName")
        return get_stats(node_name)


@working_namespace.errorhandler(NodeNotFoundException)
def handle_root_exception(error):
    return {'message': 'Node with specified name not found'}, 404
