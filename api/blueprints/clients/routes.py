from flask_restplus import Resource, Namespace
from .models import Clients


api = Namespace('clients', 'Endpoints das informações dos clientes')


@api.route('/')
class Home(Resource):

    @api.doc(responses={
        200: 'Sucesso',
    },
        security=None)
    def get(self):
        """
        Lista todos os clientes
        """

        return Clients.get_all()

@api.route('/ranking')
class Ranking(Resource):

    @api.doc(responses={
        200: 'Sucesso',
    },
        security=None)
    def get(self):
        """
        Lista o ranking
        """

        return Clients.get_ranking()

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
        Lista as transações do usuário

        """

        return Clients.get_transactions(user_id)
