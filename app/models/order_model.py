from app.configs.database import db
from sqlalchemy.orm import validates
from app.exc.StatusError import StatusError

class Orders(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(10), default='PENDING')
    products = db.relationship("Cart_Menu", backref="orders")
    payment = db.relationship("CreditCard", backref="orders")
    client_id = db.Column(db.String(36), db.ForeignKey("clients.id"))
    
    __tablename__= 'orders'

    @validates
    def validate_status(self,_, status):
        POSSIBLE_STATUS = ['PENDING','PRE_TRANSIT', 'IN_TRANSIT', 'OUT_FOR_DELIVERY', 'DELIVERED']
        if status not in POSSIBLE_STATUS:
            raise StatusError
        return status