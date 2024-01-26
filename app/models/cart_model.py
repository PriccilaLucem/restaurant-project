from app.configs.database import db
from app.models.cart_menu_table import cart_menu_association
from dataclasses import dataclass,field
from sqlalchemy.orm import Mapped
from typing import List
from app.models.menu_model import Menu

@dataclass
class Cart(db.Model):
    id: int
    items: Mapped[List[Menu]] = field(default_factory=list)


    id = db.Column(db.Integer, primary_key=True)
    client_id = db.relationship('Client', backref='cart')
    items = db.relationship('Menu', secondary=cart_menu_association, backref='carts')


    __tablename__ = "cart"