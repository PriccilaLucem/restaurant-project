from dataclasses import dataclass
from app.configs.database import db



@dataclass 
class Menu(db.Model):
    id:int
    product_name:str
    product_description:str
    product_price:float
    
    __tablename__ = 'menu'


    id = db.Column(db.Integer, primary_key = True)
    product_name = db.Column(db.String(40), nullable=False)
    product_description = db.Column(db.String(200), nullable=True)
    product_price = db.Column(db.Float, nullable=False)
    
    @staticmethod
    def validate_args(**kwargs):
        if type(kwargs['product_name']) != str:
            raise TypeError
        if kwargs['product_description']:
            if type(kwargs['product_description']) != str:
                raise TypeError
        float(kwargs['product_price'])
        
    @staticmethod
    def check_args(**kwargs):
        VALIDATED_ARGS = ['product_name', 'product_description', 'product_price']
        valid_args = {arg_name: arg_value for arg_name, arg_value in kwargs.items() if arg_name in VALIDATED_ARGS}
        return valid_args