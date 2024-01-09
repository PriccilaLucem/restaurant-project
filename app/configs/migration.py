from flask import Flask
from flask_migrate import Migrate


def init_app(app:Flask):
    migrate = Migrate(compare_type=True)
    from app.models.menu import Menu
    migrate.init_app(app, app.db)
