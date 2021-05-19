from flask import jsonify
from flask_restful import abort
from mongoengine import errors
from repository.db import DB


class Service:
    @staticmethod
    def check(items):
        if not items:
            abort(404, message="There are no items that meet the criterion")
        return items

    @staticmethod
    def get_inventory():
        items = DB.get_inventory()
        if not items:
            response = jsonify({"message": "The inventory is empty"})
            response.status_code = 404
            return response
        else:
            return items

    @staticmethod
    def get_item_by_name(name):
        return Service.check(DB.get_item_by_name(name))

    @staticmethod
    def get_item_by_quality(quality):
        return Service.check(DB.get_item_by_quality(quality))

    @staticmethod
    def get_item_by_sell_in(sell_in):
        return Service.check(DB.get_item_by_sell_in(sell_in))

    @staticmethod
    def add_item(args):
        DB.add_item(args)
        response = jsonify(
            {"message": "Item {} added successfully".format(args["name"])}
        )
        response.status_code = 201
        return response

    @staticmethod
    def delete_item(args):
        item = DB.delete_item(args)
        if item["name"] is None:
            response = jsonify({"message": "Item {} not found".format(args["name"])})
            response.status_code = 404
            return response

        response = jsonify(
            {"message": "Item {} deleted successfully".format(item["name"])}
        )
        response.status_code = 200
        return response

    @staticmethod
    def update_quality():
        return DB.update_quality()

    ## USERS

    @staticmethod
    def get_users():
        users = DB.get_users()
        if not users:
            response = jsonify({"message": "There are no users :("})
            response.status_code = 404
            return response
        else:
            return users

    @staticmethod
    def register_user(args):
        try:
            DB.register_user(args)
            response = jsonify(
                {"message": "User {} added successfully".format(args["user_name"])}
            )
            response.status_code = 201
        except errors.NotUniqueError:
            response = jsonify(
                {"message": "The user {} already exists".format(args["user_name"])}
            )
            response.status_code = 409
        finally:
            return response

    @staticmethod
    def buy_item(args):
        DB.buy_item(args)
        response = jsonify(
            {
                "message": "Congratulations {user}! {item} buyed successfully".format(
                    user=args["user_name"], item=args["name"]
                )
            }
        )
        response.status_code = 201
        return response

    @staticmethod
    def get_personal_inventory(args):
        personal_inventory = DB.get_personal_inventory(args)
        if personal_inventory:
            return personal_inventory
        else:
            response = jsonify(
                {
                    "message": "The user {} doesn't have any items".format(
                        args["user_name"]
                    )
                }
            )
            response.status_code = 404
            return response
