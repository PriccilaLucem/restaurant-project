from dataclasses import dataclass
from app.configs.database import db
from uuid import uuid4
from app.models.address_model import Address

@dataclass
class Client(db.Model):
    id: str
    name: str
    address_id: int
    email:str


    id = db.Column(db.String(36), primary_key=True, default=str(uuid4()))
    name = db.Column(db.String(40), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password_hash = db.Column(db.String(200), nullable=False)    
    
    address_id = db.Column(db.Integer, db.ForeignKey('address.id'))  # Adicionado para a relação many-to-one
    addresses = db.relationship('Address', backref="address", lazy="dynamic")

    valid_keys = ['name', 'email', 'password']

    __tablename__= 'clients'
    

