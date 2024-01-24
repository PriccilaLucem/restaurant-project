from dataclasses import dataclass
from app.configs.database import db
@dataclass
class Address(db.Model):
    id: int
    street: str
    city: str
    state: str
    zip_code: str
    number: str
    complement: str

    __tablename__ = 'address'

    id = db.Column(db.Integer, primary_key=True)
    street = db.Column(db.String(100))
    city = db.Column(db.String(50))
    state = db.Column(db.String(50))
    zip_code = db.Column(db.String(10))
    number = db.Column(db.String(10))
    complement = db.Column(db.String(50), nullable=True)
    
    @staticmethod   
    def validate_args(**kwargs):
        VALID_ARGS = ['zip_code', 'number', 'complement']

        validated_args = {arg_name: arg_value for arg_name, arg_value in kwargs.items() if arg_name in VALID_ARGS}
        if not len(kwargs['zip_code']) == 8:
            raise ValueError
        if type(kwargs['number']) != str:
            raise TypeError
        
        return validated_args
    