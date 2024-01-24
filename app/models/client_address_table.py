from app.configs.database import db

client_address = db.Table('client_address', 
    db.Column('client_id', db.String(36), db.ForeignKey('clients.id'), primary_key=True),
    db.Column('address_id', db.Integer, db.ForeignKey('address.id'), primary_key=True),
)
