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

    @staticmethod
    def get_ranking():
        query = mongo.db.clients.find({}, {'_id': 0, "first_name": 1, "last_name": 1, "total_stars": 1})\
            .sort('total_stars', -1)

        return json.loads(
            dumps(query)
        )
