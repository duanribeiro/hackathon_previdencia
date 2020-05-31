from faker import Faker
import random
from mock_data import fake_info
import pymongo
from config import DevConfig
from bson.json_util import dumps
import json
from datetime import datetime


fake = Faker()
myclient = pymongo.MongoClient(DevConfig.MONGO_URI)
db = myclient["playground"]


class FakeClient:
    def __init__(self, sex):
        if sex == 'male':
            self.first_name = random.choice(fake_info.male_names)
            self.sex = 'M'
        else:
            self.first_name = random.choice(fake_info.female_names)
            self.sex = 'F'

        self.last_name = random.choice(fake_info.last_names)
        self.age = random.randrange(18, 80)
        self.email = fake.email()
        self.city = random.choice(fake_info.citys)
        self.phone = f'9{random.randrange(1111, 9999)}-{random.randrange(1111, 9999)}'
        self.total_stars = random.randrange(1, 100)
        self.transactions = [FakeTransaction().__dict__ for total_transactions in range(1, random.randrange(2, 100))]


class FakeTransaction:
    def __init__(self):
        self.product = random.choice(fake_info.products)
        self.category = random.choice(fake_info.category)
        self.seller_feedback_score = random.randrange(1, 99)
        self.condition = random.choice(['NEW', 'USED'])
        self.price_value = round(random.uniform(10, 10000), 2)
        self.price_currency = 'BRL'
        self.cashback_percentage = random.randrange(1, 50)
        self.date = datetime.combine(fake.date_between(start_date='-1y', end_date='today'), datetime.min.time())


for i in range(20):
    if i % 2 == 0:
        client = FakeClient(sex='male')
    else:
        client = FakeClient(sex='female')

        db.clients.insert_one(client.__dict__)
        print('ok')
