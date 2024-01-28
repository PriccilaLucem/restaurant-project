from app.configs.database import db
from app.models.cart_menu_model import Cart_Menu
from dataclasses import dataclass,field
from sqlalchemy.orm import Mapped
from typing import List

@dataclass
class Cart(db.Model):
    id: int
    items: Mapped[List[Cart_Menu]] = field(default_factory=list)


    id = db.Column(db.Integer, primary_key=True)
    client_id = db.relationship('Client', backref='cart')
    items = db.relationship("Cart_Menu", backref="cart_menu_association")

    __tablename__ = "cart"