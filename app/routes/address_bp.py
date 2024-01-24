from flask import Blueprint
from app.controllers import address_controller

address_bp = Blueprint("address_bp", __name__, url_prefix="/address")


address_bp.post("")(address_controller.post_address_controller)
address_bp.delete("/<int:address_id>")(address_controller.delete_address_from_client_controller)