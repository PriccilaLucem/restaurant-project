from dataclasses import dataclass
from app.configs.database import db



@dataclass 
class Menu(db.Model):
    __tablename__ = 'menu'

    
    id = db.Column(db.Integer, primary_key = True)
    product_name = db.Column(db.String(40), nullable=False)
    product_description = db.Column(db.String(200), nullable=True)
    product_price = db.Column(db.Float, nullable=False)
    