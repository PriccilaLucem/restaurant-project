from flask import Blueprint
from app.controllers import credit_card_controller



credit_card_bp = Blueprint("credit_card_bp", __name__, url_prefix="/credit_card")


credit_card_bp.get("")(credit_card_controller.get_credit_card_controller)
credit_card_bp.post("")(credit_card_controller.post_credit_card_controller)
credit_card_bp.delete("<string:credit_card_id>")(credit_card_controller.delete_credit_card_controller)