from flask import Blueprint
from flask_restplus import Api


v1_blueprint = Blueprint('v1', __name__, url_prefix='')

api = Api(v1_blueprint,
          doc='/docs',
          title='HackaPrev API',
          version='0.0.1',
          description='O principal desta documentação é facilitar o entendimento das chamadas REST.')

from api.blueprints.clients.routes import api as clients_api
from api.blueprints.simulator.routes import api as simulator_api
from api.blueprints.machine_learning.routes import api as machine_learning_api

api.add_namespace(clients_api)
api.add_namespace(simulator_api)
api.add_namespace(machine_learning_api)





