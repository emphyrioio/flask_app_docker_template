from flask import Flask

from .blueprints import create_blueprint1
from .config import DevelopmentConfig, ProductionConfig, TestingConfig
from .extensions import db_bp1


def create_app(config_class=None) -> Flask:
    app = Flask(__name__)

    if config_class is None:
        config_class = DevelopmentConfig

    app.config.from_object(config_class)

    db_bp1.init_app(app)

    blueprint1 = create_blueprint1()
    app.register_blueprint(blueprint1, url_prefix="")

    return app
