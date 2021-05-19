from flask_restful import Resource

from services.service import Service


class Quality(Resource):
    def get(self, quality):
        return Service.get_item_by_quality(quality)
