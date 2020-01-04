from flask import Flask
from flask_restplus import Api
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from config import Configuration

app = Flask(__name__)
CORS(app)
app.config.from_object(Configuration)
api = Api(app=app, version='1.0', title='Jenkins nodes usage service')

database = SQLAlchemy(app)

from controller.working_controller import working_namespace
from controller.node_controller import node_namespace
import controller.views_controller
api.add_namespace(working_namespace)
api.add_namespace(node_namespace)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
    database.init_app(app)
