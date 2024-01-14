from app.configs.database import db
from dataclasses import dataclass
from uuid import uuid4

@dataclass
class Adm(db.Model):
    id: str
    email:str
    password_hash:str
    is_adm = bool
    
    id = db.Column(db.String(36), primary_key=True, default=str(uuid4()))
    email = db.Column(db.String(100), nullable=False, unique=True)
    password_hash = db.Column(db.String(200), nullable=False)    
    is_adm = db.Column(db.Boolean, default=True)