from app.configs.database import db
from uuid import uuid4 
from dataclasses import dataclass

@dataclass
class CreditCard(db.Model):

    id: str
    card_number: str
    expiration_date: str
    security_code: str

    id = db.Column(db.String(36), primary_key=True, default=str(uuid4()))
    card_number = db.Column(db.String(16), nullable=False)
    expiration_date = db.Column(db.String(5), nullable=False)
    security_code = db.Column(db.String(3), nullable=False)
    client_id = db.Column(db.String(36), db.ForeignKey("clients.id"))

    __tablename__ = "credit_cards"


    @staticmethod
    def validate_args(**kwargs):
        VALIDATED_ARGS = ['card_number', 'expiration_date', 'security_code']
        if type(kwargs['card_number']) != str: 
            raise TypeError
        if type(kwargs['expiration_date']) != str: 
            raise TypeError
        if type(kwargs['security_code']) != str: 
            raise TypeError
        return {arg_name: arg_value for arg_name, arg_value in kwargs.items() if arg_name in VALIDATED_ARGS}
