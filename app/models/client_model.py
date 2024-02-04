from dataclasses import dataclass, field
from app.configs.database import db
from uuid import uuid4
from sqlalchemy.orm import validates
import re
from werkzeug.security import generate_password_hash, check_password_hash
from app.models.client_address_table import client_address
from app.models.address_model import Address
from app.models.cart_model import Cart
from typing import List
from sqlalchemy.orm import Mapped
from app.exc.AddressAlreadyRegisteredError import AddressAlreadyRegisteredError
@dataclass
class Client(db.Model):
    id: str
    name: str
    email: str
    addresses: Mapped[List[Address]] = field(default_factory=list)
    cart: Mapped[List[Cart]]= field(default_factory=list)


    id = db.Column(db.String(36), primary_key=True, default=str(uuid4()))
    name = db.Column(db.String(40), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password_hash = db.Column(db.String(200), nullable=False)
    addresses = db.relationship('Address', secondary=client_address, lazy="subquery")
    cart_id = db.Column(db.Integer, db.ForeignKey('cart.id'), unique=True)
    cart = db.relationship("Cart", uselist=False, foreign_keys=[cart_id], backref="cart_id")
    credit_cards = db.relationship("CreditCard", backref='client', lazy=True)

    __tablename__ = 'clients'

    @validates
    def validate_email(self, _, email):
        email_regex = r"^[\w-]+@[a-z\d]+\.[\w]{3}(.br)?"

        if not re.fullmatch(email_regex, email):
            raise ValueError("Invalid email, format should be equal to xxxx@xxxx.xxx.(xx)")
        return email

    @validates
    def validate_name(self, _, name):
        if type(name) != str or len(name) < 4:
            raise ValueError("Name should have length > 4 and be a string")
        return name

    @property
    def password(self):
        raise ValueError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password_to_compare):
        return check_password_hash(self.password_hash, password_to_compare)

    def validate_keys(**kwargs):
        VALIDATED_ARGS = ['name', 'email', 'password']
        return {arg_name: arg_value for arg_name, arg_value in kwargs.items() if arg_name in VALIDATED_ARGS}
    
    @staticmethod
    def validate_if_user_already_registered_address(client, address):
        for client_address in client.addresses:
            if (
                client_address.street == address.street
                and client_address.city == address.city
                and client_address.state == address.state
                and client_address.zip_code == address.zip_code
                and client_address.number == address.number
                and client_address.complement == address.complement
            ):
                raise AddressAlreadyRegisteredError




