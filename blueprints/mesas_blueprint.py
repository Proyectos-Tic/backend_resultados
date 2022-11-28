from flask import Blueprint, request

from controllers.mesas_controller import MesasController

mesas_blueprint = Blueprint('mesas_blueprint', __name__)
mesas_controller = MesasController()

@mesas_blueprint.route("/mesa/all", methods=["GET"])
def get_all_tables():
    response = mesas_controller.index()
    return response, 200

@mesas_blueprint.route("/mesa/<string:id>", methods=["GET"])
def get_table_by_id(id):
    response = mesas_controller.show(id)
    return response, 200

@mesas_blueprint.route("/mesa/create", methods=["POST"])
def create_table():
    table = request.get_json()
    response = mesas_controller.create(table)
    return response, 200

@mesas_blueprint.route("/mesa/update/<string:id>", methods=["PATCH"])
def update_table(id):
    table = request.get_json()
    response = mesas_controller.update(id, table)
    return response, 200

@mesas_blueprint.route("/mesa/delete/<string:id>", methods=["DELETE"])
def delete_table(id):
    response = mesas_controller.delete(id)
    return response, 200
