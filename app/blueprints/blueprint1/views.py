from flask import abort, render_template
from jinja2 import TemplateNotFound


def home():
    try:
        return render_template("home.html")
    except TemplateNotFound:
        abort(404)
