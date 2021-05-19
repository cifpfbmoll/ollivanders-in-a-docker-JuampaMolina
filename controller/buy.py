from flask_restful import Resource, reqparse

from services.service import Service


class Buy(Resource):
    def put(self):
        args = self.parseRequest()
        return Service.buy_item(args)

    @staticmethod
    def parseRequest():
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument(
            "user_name", type=str, required=True, help="user_name required"
        )
        parser.add_argument(
            "password", type=str, required=True, help="password required"
        )
        parser.add_argument("name", type=str, required=True, help="item name required")
        parser.add_argument(
            "sell_in", type=str, required=True, help="item sell_in required"
        )
        parser.add_argument(
            "quality", type=str, required=True, help="item quality required"
        )
        return parser.parse_args()
