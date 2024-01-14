from flask import Flask
from app.routes.menu_bp import menu_bp
from app.routes.client_bp import client_bp


def init_app(app:Flask):
    app.register_blueprint(menu_bp)
    app.register_blueprint(client_bp)