import json

from flask import request
from flask_restplus import Namespace, Resource

from service.working_service import start_working, stop_working

working_namespace = Namespace('api/working', description='')


@working_namespace.route('/start')
class Working(Resource):
    def post(self):
        start_working(data=json.loads(request.data))
        pass


@working_namespace.route('/stop')
class Working(Resource):
    def post(self):
        stop_working(data=json.loads(request.data))
        pass
