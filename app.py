from flask import Flask
from flask_restplus import Api

from api.working import working_namespace
from config import Configuration

app = Flask(__name__)
app.config.from_object(Configuration)
api = Api(app=app, version='1.0', title='Jenkins nodes usage service')
api.add_namespace(working_namespace)


if __name__ == '__main__':
    app.run()
