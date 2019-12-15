import json

from flask import request
from flask_restplus import Namespace, Resource

from dto.working_dto import working_dto
from service.working_service import start_working, stop_working

working_namespace = Namespace('api/working', description='')


@working_namespace.route('/start')
class Working(Resource):
    @working_namespace.doc(description='Node started do task request')
    @working_namespace.expect(working_dto, validate=True)
    def post(self):
        start_working(data=json.loads(request.data))
        pass


@working_namespace.route('/stop')
class Working(Resource):
    @working_namespace.doc(description='Node finished do task request')
    @working_namespace.expect(working_dto, validate=True)
    def post(self):
        stop_working(data=json.loads(request.data))
        pass
