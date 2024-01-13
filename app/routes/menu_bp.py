from flask import Blueprint
from app.controllers import  menu_controllers

menu_bp = Blueprint("menu_bp", __name__, url_prefix="/menu")


menu_bp.get("")(menu_controllers.get_menu_controller)
menu_bp.get("/<int:id>")(menu_controllers.get_by_id_menu_controller)
menu_bp.post("")(menu_controllers.post_menu_controller)
menu_bp.delete("/<int:id>")(menu_controllers.delete_menu_controller)
menu_bp.patch("/<int:id>")(menu_controllers.patch_menu_controller)