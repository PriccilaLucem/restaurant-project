from app.configs.database import db
from app.models.cart_menu_model import Cart_Menu
from dataclasses import dataclass, field
from sqlalchemy.orm import Mapped
from typing import List

@dataclass 
class Cart(db.Model):
    id: int
    cart_relationship: Mapped[List[Cart_Menu]] = field(default_factory=list)


    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.String(36), db.ForeignKey('clients.id'), unique=True)
    cart_relationship = db.relationship("Cart_Menu", back_populates="cart")

    __tablename__="cart"


    @staticmethod
    def valid_args(**kwargs):
        VALIDATED_ARGS = ["id"]
        if type(kwargs['id']) != int:
            raise TypeError
        return {arg_name: arg_value for arg_name, arg_value in kwargs.items() if arg_name in VALIDATED_ARGS}

