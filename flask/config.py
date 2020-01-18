import os


class Configuration:

    DEBUG = True,
    SQLALCHEMY_DATABASE_URI = 'postgresql://' \
                              + os.getenv('JENKINS_NODES_USAGE_DB_USERNAME') \
                              + ':' \
                              + os.getenv('JENKINS_NODES_USAGE_DB_PASSWORD') \
                              + '@' \
                              + os.getenv('DATABASE_PORT_5432_TCP_ADDR') \
                              + ':' \
                              + os.getenv('DATABASE_PORT_5432_TCP_PORT') \
                              + '/' \
                              + os.getenv('DATABASE_NAME')
