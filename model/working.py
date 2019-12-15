from app import database


class Working(database.Model):
    __tablename__ = 'working'

    id = database.Column(database.BigInteger, primary_key=True, autoincrement=True)
    node_name = database.Column(database.String(255), nullable=False)
    activated = database.Column(database.Boolean, nullable=False)
    time = database.Column(database.DateTime, nullable=False)

    def __init__(self, node_name, activated, time):
        self.node_name = node_name
        self.activated = activated
        self.time = time
