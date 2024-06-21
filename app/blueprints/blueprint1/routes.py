from flask import Blueprint

from .views import home


def register_routes(blueprint) -> Blueprint:

    blueprint.add_url_rule("/", "home", home)
