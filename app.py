from flask import Flask, render_template
from flask_cors import CORS
from flask_restful import Resource, Api

from controller.buy import Buy
from controller.inventory import Inventory
from controller.items import Items
from controller.personal_inventory import PersonalInventory
from controller.quality import Quality
from controller.sell_in import Sell_in
from controller.update_quality import UpdateQuality
from controller.users import Users
from repository.db_engine import init_app
from services.service import Service

app = Flask(__name__)
CORS(app)
api = Api(app)
init_app(app)


class WelcomeOllivanders(Resource):
    def get(self):
        return {"Welcome": "Ollivanders"}


@app.route("/home")
def show_inventory():
    items = Service.get_inventory()
    return render_template("inventory.html", inventory=items)


api.add_resource(WelcomeOllivanders, "/")
api.add_resource(Inventory, "/inventory")
api.add_resource(Items, "/item/name/<name>", "/item")
api.add_resource(Quality, "/item/quality/<int:quality>")
api.add_resource(Sell_in, "/item/sell_in/<int:sell_in>")
api.add_resource(UpdateQuality, "/update_quality")
api.add_resource(Users, "/user")
api.add_resource(Buy, "/buy")
api.add_resource(PersonalInventory, "/user/inventory")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
