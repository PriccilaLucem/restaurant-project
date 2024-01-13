from flask import Flask
from app.routes.menu_bp import menu_bp

def init_app(app:Flask):
    app.register_blueprint(menu_bp)