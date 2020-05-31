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

