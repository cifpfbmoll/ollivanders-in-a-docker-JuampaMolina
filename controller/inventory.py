from flask_restful import Resource

from services.service import Service


class Inventory(Resource):
    def get(self):
        return Service.get_inventory()
