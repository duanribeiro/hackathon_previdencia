import json
from bson.json_util import dumps
from api import mongo


class Clients:

    @staticmethod
    def get_all():
        query = mongo.db.clients.find({}, {'_id': 0, "transactions": 0}).sort('first_name', 1)

        return json.loads(
            dumps(query)
        )
