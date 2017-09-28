from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import app_config
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_migrate import Migrate

# Initialize the app
app = Flask(__name__, instance_relative_config=True)

# Load the views
from app import views

# Load the config file
app.config.from_object('config')

#db variable initialization
db = SQLAlchemy()

login_manager = LoginManager()

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    db.init_app(app)

    login_manager.init_app(app)
    login_manager.login_message = "You must be logged in to access this page."
    login_manager.login_view = "auth.login"

    migrate = Migrate(app, db)
    
    from app import models
    
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    from .recipes import recipes as recipes_blueprint
    app.register_blueprint(recipes_blueprint)

    from .chef import chef as chef_blueprint
    app.register_blueprint(chef_blueprint)

    Bootstrap(app)
    

    return app
