from flask_restful import Resource

from services.service import Service


class Sell_in(Resource):
    def get(self, sell_in):
        return Service.get_item_by_sell_in(sell_in)
