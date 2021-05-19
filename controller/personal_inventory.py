from flask_restful import Resource, reqparse

from services.service import Service


class PersonalInventory(Resource):
    def put(self):
        args = self.parseRequest()
        return Service.get_personal_inventory(args)

    def parseRequest(self):
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument(
            "user_name", type=str, required=True, help="user name required"
        )
        parser.add_argument(
            "password", type=str, required=True, help="password required"
        )
        return parser.parse_args()
