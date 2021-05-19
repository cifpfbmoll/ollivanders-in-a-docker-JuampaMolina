from flask_restful import Resource

from services.service import Service


class UpdateQuality(Resource):
    def get(self):
        return Service.update_quality()
