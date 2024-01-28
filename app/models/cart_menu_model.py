from app.configs.database import db
from dataclasses import dataclass, field
from app.models.menu_model import Menu
from sqlalchemy.orm import Mapped
from typing import List

@dataclass
class Cart_Menu(db.Model):
    id: int
    quantity: int
    is_selected: bool
    menu: Mapped[list[Menu]] = field(default_factory=list)

    id = db.Column(db.Integer, primary_key=True)
    cart_id = db.Column(db.Integer, db.ForeignKey('cart.id'))
    menu_id = db.Column(db.Integer, db.ForeignKey('menu.id')) 
    quantity = db.Column(db.Integer, nullable=False, default=1)
    is_selected = db.Column(db.Boolean, default=True)

    cart = db.relationship("Cart", backref="items")
    menu = db.relationship("Menu", backref="carts")

    __tablename__ = 'cart_menu_association'
