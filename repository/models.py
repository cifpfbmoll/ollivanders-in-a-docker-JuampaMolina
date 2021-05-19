from mongoengine import *


class Inventory(Document):
    name = StringField(required=True)
    sell_in = IntField()
    quality = IntField()


class Users(Document):
    user_name = StringField(required=True, unique=True)
    email = StringField(unique=True)
    password = StringField()
    credit = IntField()
    inventory = ListField(DictField())
