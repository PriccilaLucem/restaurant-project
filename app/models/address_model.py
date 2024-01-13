from dataclasses import dataclass
from app.configs.database import db


@dataclass
class Address(db.Model):
    id: int
    street: str
    city: str
    state: str
    zip_code: str

    __tablename__ = 'address'

    id = db.Column(db.Integer, primary_key=True)
    street = db.Column(db.String(100))
    city = db.Column(db.String(50))
    state = db.Column(db.String(50))
    zip_code = db.Column(db.String(10))
    client = db.relationship("clients")
