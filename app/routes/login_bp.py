from flask import Blueprint
from app.controllers import login_controller


login_bp = Blueprint("login_bp", __name__, url_prefix="/login")


login_bp.post("")(login_controller.login_controller)