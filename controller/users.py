from flask_restful import Resource, reqparse

from services.service import Service


class Users(Resource):
    def get(self):
        return Service.get_users()

    def post(self):
        args = self.parseRequest()
        return Service.register_user(args)

    @staticmethod
    def parseRequest():
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument(
            "user_name", type=str, required=True, help="user_name required"
        )
        parser.add_argument("email", type=str, required=True, help="email required")
        parser.add_argument(
            "password", type=str, required=True, help="password required"
        )
        return parser.parse_args()
