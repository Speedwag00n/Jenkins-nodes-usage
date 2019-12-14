import os


class Configuration:

    DEBUG = True,
    SQLALCHEMY_DATABASE_URI = 'postgresql://' \
                              + os.getenv('JENKINS_NODES_USAGE_DB_USERNAME') \
                              + ':' \
                              + os.getenv('JENKINS_NODES_USAGE_DB_PASSWORD') \
                              + '@localhost:5432/jenkins'
