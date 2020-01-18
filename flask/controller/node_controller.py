from flask_restplus import Namespace, Resource

from dto.node_dto import NodeDto
from service.node_service import *

node_namespace = Namespace('api/node', description='Requests for work with nodes')


@node_namespace.route('')
class ExistingNodes(Resource):
    @node_namespace.marshal_with(NodeDto.node_dto, as_list=True)
    @node_namespace.doc(description='Get names of all known nodes (by their working stats)')
    def get(self):
        nodes = get_nodes_names()
        names = list()
        for node in nodes:
            names.append({"name": node[0]})
        return names
