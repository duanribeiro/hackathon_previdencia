from api.blueprints import api
from flask_restplus import fields


simulation = api.model('Parâmetros para gerar uma simulação', {
    'time': fields.Integer(required=True,
                          description='O tempo de contribuição em meses',
                          example=372),
    'interest': fields.Float(required=True,
                           description='A rentabilidade estimada',
                           example=0.005),
    'deposit_value': fields.Float(required=True,
                             description='O valor do depóstio mensal',
                             example=35),
})
