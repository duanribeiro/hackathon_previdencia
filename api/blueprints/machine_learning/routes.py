from flask_restplus import Resource, Namespace
from .models import MachineLearning
from api.blueprints.machine_learning import serializers

api = Namespace('machine_learning', 'Endpoints do Machine Learning')


@api.route('/<string:user_id>')
class Home(Resource):

    @api.doc(responses={
        200: 'Sucesso',
        500: 'Erro interno do servidor',
    },
        params={"user_id": "id do usuaŕio (5ed354e9abb821d580c6886c)"},
        security=None)
    def get(self, user_id):
        """
        Simula uma predição ao usuário

        """

        return MachineLearning.run(user_id)

