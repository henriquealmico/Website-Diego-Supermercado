from flask import Flask
from .config import Config
from .extensions import db, migrate, mail, jwt
from app.user.routes import user_api
from app.cupons.routes import cupom_api
from app.produtos.routes import produto_api
from app.encarte.routes import encarte_api
from app.carrinho.routes import carrinho_api
from app.pedido.routes import pedido_api


def create_app():

    app = Flask(__name__, instance_relative_config=True)
    app.config['SECRET_KEY'] = 'Fluxo'
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    mail.init_app(app)
    jwt.init_app(app)

    app.register_blueprint(user_api)
    app.register_blueprint(cupom_api)
    app.register_blueprint(produto_api)
    app.register_blueprint(pedido_api)
    app.register_blueprint(carrinho_api)
    app.register_blueprint(encarte_api)
    
    return app

