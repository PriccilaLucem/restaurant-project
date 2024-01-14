from flask import Blueprint
from app.controllers import client_controller


client_bp = Blueprint("client_bp", __name__, url_prefix="/client")
client_bp.get("")(client_controller.get_all_clients_controller)
client_bp.get("/<string:id>")(client_controller.get_by_id_client_controller)
client_bp.post("")(client_controller.post_client_controller)
client_bp.patch("<string:id>")(client_controller.patch_client_controller)
client_bp.delete("<string:id>")(client_controller.delete_client_controller)