from flask import Blueprint

from .routes import register_routes


def create_blueprint1() -> Blueprint:
    blueprint1 = Blueprint(
        "blueprint1",
        __name__,
        template_folder="data/templates",
        static_folder="data/static",
    )

    register_routes(blueprint1)

    return blueprint1
