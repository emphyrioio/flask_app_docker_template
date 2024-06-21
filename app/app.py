from flask import Flask

from .blueprints import create_blueprint1
from .config import DevelopmentConfig, ProductionConfig, TestingConfig


def create_app(config_class=None) -> Flask:
    app = Flask(__name__)

    if config_class is None:
        config_class = DevelopmentConfig

    app.config.from_object(config_class)

    blueprint1 = create_blueprint1()
    app.register_blueprint(blueprint1, url_prefix="")

    return app
