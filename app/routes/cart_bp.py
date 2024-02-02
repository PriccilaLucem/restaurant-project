from flask import Blueprint
from app.controllers import cart_controller


cart_bp = Blueprint("cart_bp", __name__, url_prefix="/cart")


cart_bp.get("")(cart_controller.get_cart_controller)
cart_bp.post("")(cart_controller.post_cart_controller)
cart_bp.patch("/<int:product_id>")(cart_controller.patch_cart_controller)
cart_bp.delete("/<int:product_id>")(cart_controller.delete_cart_product_controller)