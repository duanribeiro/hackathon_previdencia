from api.blueprints import api
from flask_restplus import fields


model = api.model('Parâmetros para gerar uma predição para um usúario', {
    'user_id': fields.String(required=True,
                             description='O id do usuário',
                             example="5ed354e9abb821d580c6886c"),
})
