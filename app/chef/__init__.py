# app/chef/__init__.py

from flask import Blueprint

home = Blueprint('chef', __name__)

from . import views
