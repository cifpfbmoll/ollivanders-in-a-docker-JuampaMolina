from flask_restful import Resource, reqparse

from services.service import Service


class Items(Resource):
    def get(self, name):
        return Service.get_item_by_name(name)

    def delete(self):
        args = self.parseRequest()
        return Service.delete_item(args)

    def post(self):
        args = self.parseRequest()
        return Service.add_item(args)

    def parseRequest(self):
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument("name", type=str, required=True, help="name required")
        parser.add_argument("sell_in", type=int, required=True, help="sell_in required")
        parser.add_argument("quality", type=int, required=True, help="quality required")
        return parser.parse_args()
