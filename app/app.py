from flask import Flask

from .blueprints.blueprint1 import create_blueprint1
from .blueprints.blueprint1.entities.person import PersonBp1
from .config import DevelopmentConfig, ProductionConfig, TestingConfig
from .extensions import db, migrate


def create_app(config_class=None) -> Flask:
    app = Flask(__name__)

    if config_class is None:
        config_class = DevelopmentConfig

    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)

    blueprint1 = create_blueprint1()
    app.register_blueprint(blueprint1, url_prefix="")

    return app
