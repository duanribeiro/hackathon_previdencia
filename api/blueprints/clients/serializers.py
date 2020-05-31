from api.blueprints import api
from flask_restplus import fields


economic_group = api.model('Parâmetros para grupo econômico', {
    'name': fields.String(required=True,
                          description='O nome do grupo econômico',
                          example="petro"),
})

counterparty = api.model('Parâmetros para contraparte', {
    'cnpj': fields.String(required=True,
                          description='O número do CNPJ (somente números) da contraparte',
                          example="12345671000400"),
})

key_val = api.model('Parâmetros para edição', {
    'key': fields.List(fields.String(required=True,
                                     description='Uma lista com os nome das chaves a serem acessadas em ordem.',
                                     ),
                       example=["group", "petro", "fxspot", "usd", "sell"]),
    'value': fields.List(fields.Float(required=True,
                                      description='O valor a ser inserido dentro da chave.'),
                         example=[1.1, 2.2, 3.3])
})
