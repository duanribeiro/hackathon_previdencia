from flask_restplus import Resource, Namespace
from .models import Simulator
from api.blueprints.simulator import serializers

api = Namespace('simulator', 'Endpoints do Simulador')


@api.route('/')
class Home(Resource):

    @api.expect(serializers.simulation)
    @api.doc(responses={
        200: 'Sucesso',
        500: 'Erro interno do servidor',
    },
        security=None)
    def post(self):
        """
        Lista todos os clientes
        """

        return Simulator.run(api.payload)

