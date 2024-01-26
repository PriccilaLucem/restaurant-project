from app.configs.database import db

cart_menu_association = db.Table(
    'cart_menu_association',
    db.Column('cart_id', db.Integer, db.ForeignKey('cart.id'), primary_key=True),
    db.Column('menu_id', db.Integer, db.ForeignKey('menu.id'), primary_key=True),
    db.Column('quantity', db.Integer, nullable=False),
    db.Column('is_selected', db.Boolean, default=True)
)
