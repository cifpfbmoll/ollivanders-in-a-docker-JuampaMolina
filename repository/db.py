from flask import g
from flask_restful import fields, marshal_with, abort
from mongoengine import Q

from repository.db_engine import get_db
from repository.factory import Factory


class DB:
    inventory_resource_fields = {
        "name": fields.String,
        "sell_in": fields.Integer,
        "quality": fields.Integer,
    }

    users_resource_fields = {
        "user_name": fields.String,
        "email": fields.String,
        "password": fields.String,
        "credit": fields.Integer,
        "inventory": fields.List(
            fields.Nested(inventory_resource_fields)
        ),  # Lista de objetos Item(Inventory model)
    }

    @staticmethod
    @marshal_with(inventory_resource_fields)
    def get_inventory():
        db = get_db()
        inventory = []
        for object in g.Inventory.objects():
            inventory.append(object)
        return inventory

    @staticmethod
    @marshal_with(inventory_resource_fields)
    def get_item_by_name(name):
        db = get_db()
        items = []
        for object in g.Inventory.objects(name=name):
            items.append(object)
        return items

    @staticmethod
    @marshal_with(inventory_resource_fields)
    def get_item_by_quality(quality):
        db = get_db()
        items = []
        for object in g.Inventory.objects(quality=quality):
            items.append(object)
        return items

    @staticmethod
    @marshal_with(inventory_resource_fields)
    def get_item_by_sell_in(sell_in):
        db = get_db()
        items = []
        for object in g.Inventory.objects(sell_in__lte=sell_in):
            items.append(object)
        return items

    @staticmethod
    @marshal_with(inventory_resource_fields)
    def add_item(args):
        db = get_db()
        g.Inventory(
            name=args["name"], sell_in=args["sell_in"], quality=args["quality"]
        ).save()

    @staticmethod
    @marshal_with(inventory_resource_fields)
    def delete_item(args):
        db = get_db()
        item = g.Inventory.objects(
            Q(name=args["name"])
            & Q(sell_in=args["sell_in"])
            & Q(quality=args["quality"])
        ).first()
        if item:
            item.delete()
        return item

    @staticmethod
    def update_quality():
        db = get_db()
        for item in g.Inventory.objects():
            itemObject = Factory.createItemObject(
                [item.name, item.sell_in, item.quality]
            )
            itemObject.update_quality()
            item.sell_in = itemObject.sell_in
            item.quality = itemObject.quality
            item.save()
        return DB.get_inventory()

    ## USERS
    @staticmethod
    @marshal_with(users_resource_fields)
    def get_users():
        db = get_db()
        users = []
        for user in g.Users.objects():
            users.append(user)
        return users

    @staticmethod
    @marshal_with(users_resource_fields)
    def register_user(args):
        db = get_db()
        g.Users(
            user_name=args["user_name"],
            email=args["email"],
            password=args["password"],
            credit=50,
            inventory=[],
        ).save()

    @staticmethod
    def buy_item(args):
        db = get_db()
        item = g.Inventory.objects(
            Q(name=args["name"])
            & Q(sell_in=args["sell_in"])
            & Q(quality=args["quality"])
        ).first()

        if not item:
            abort(404, message="No item found with that name")

        itemDict = {"name": item.name, "sell_in": item.sell_in, "quality": item.quality}

        user = g.Users.objects(
            Q(user_name=args["user_name"]) & Q(password=args["password"])
        ).first()

        if not user:
            abort(404, message="There is no user with this name and password")

        if user.credit >= item.quality:
            inventory = user.inventory
            inventory.append(itemDict)

            user.inventory = inventory
            user.credit -= item.quality
            user.save()

            if item:
                item.delete()
        else:
            abort(404, message="You do not have enough credits")

    @staticmethod
    def get_personal_inventory(args):
        db = get_db()
        user = g.Users.objects(
            Q(user_name=args["user_name"]) & Q(password=args["password"])
        ).first()

        personal_inventory = []

        if user:
            for item in user.inventory:
                personal_inventory.append(item)
            return personal_inventory
        else:
            abort(404, message="There is no user with this name and password")
