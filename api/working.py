from flask_restplus import Namespace, Resource


working_namespace = Namespace('api/working', description='')


@working_namespace.route('/')
class Working(Resource):
    def post(self):
        return {
            'info': 'request received'
        }
