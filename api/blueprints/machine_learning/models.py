import json
from bson.json_util import dumps, ObjectId
from api import mongo
import pandas as pd


def clean_data(transactions):
    for idx, transaction in transactions.iterrows():
        if not transaction.get('cashback_percentage'):
            transaction['cashback_percentage'] = 0

    return transactions


def make_prediction(clean_transactions, total_stars):
    total_value = 0

    for idx, transaction in clean_transactions.iterrows():
        total_value += transaction['price_value']

    mean_transactions = round(total_value / len(clean_transactions), 2)
    if total_stars > 50:
        potencial_buy = round(mean_transactions * 0.05, 2)
    else:
        potencial_buy = round(mean_transactions * 0.02, 2)

    return {"mean_transactions": mean_transactions, "potencial_buy": potencial_buy}


class MachineLearning:

    @staticmethod
    def run(user_id):
        query = mongo.db.clients.find_one({"_id": ObjectId(user_id)}, {"_id": 0})
        transactions = pd.DataFrame(query.pop('transactions'))
        clean_transactions = clean_data(transactions)
        total_stars = query['total_stars']

        return make_prediction(clean_transactions, total_stars)
