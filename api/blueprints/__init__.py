from flask import Blueprint
from flask_restplus import Api


v1_blueprint = Blueprint('v1', __name__, url_prefix='')

api = Api(v1_blueprint,
          doc='/docs',
          title='Database API',
          version='0.0.1',
          description='O principal objetivo desta API é facilitar a inserção e edição de dados do banco de dados.')

from api.blueprints.clients.routes import api as clients_api
api.add_namespace(clients_api)



