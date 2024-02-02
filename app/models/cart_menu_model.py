from app.configs.database import db
from dataclasses import dataclass, field
from sqlalchemy.orm import Mapped
from typing import List
from app.models.menu_model import Menu


@dataclass
class Cart_Menu(db.Model):
    id: int
    quantity: int
    is_selected: bool
    cart_id: int
    menu_id: int
    menu: Mapped[List[Menu]] = field(default_factory=list)


    id = db.Column(db.Integer, primary_key=True)
    cart_id = db.Column(db.Integer, db.ForeignKey("cart.id"), nullable=False)
    menu_id = db.Column(db.Integer, db.ForeignKey("menu.id"), nullable=False)
    quantity = db.Column(db.Integer, nullable=False, default=1)
    is_selected = db.Column(db.Boolean, default=True)
    
    cart = db.relationship("Cart", back_populates="cart_relationship")
    menu = db.relationship("Menu", back_populates="cart_relationship")


    @staticmethod
    def validate_args(**kwargs):
        VALIDATED_ARGS = ["quantity", "is_selected"]
        return {arg_name: arg_value for arg_name, arg_value in kwargs.items() if arg_name in VALIDATED_ARGS}


    