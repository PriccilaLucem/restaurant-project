from flask import Flask
from flask_migrate import Migrate


def init_app(app:Flask):
    migrate = Migrate(compare_type=True)
    
    from app.models.menu_model import Menu
    from app.models.address_model import Address
    from app.models.client_model import Client
    from app.models.adm_model import Adm

    migrate.init_app(app, app.db)

