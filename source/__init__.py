from flask import Flask
from flask_admin.contrib.sqla import ModelView
from source.models import User
from source.extensions import db, bcrypt, login_manager, admin

def create_app(config_file = 'config.py'):
    app = Flask(__name__)
    app.config.from_pyfile(config_file)
    register_extension(app)
    register_blueprints(app)

    return app

def register_extension(app):
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    admin.init_app(app)
    admin.add_view(ModelView(User, db.session))


def register_blueprints(app):
    from source.users.views import users_blueprint
    app.register_blueprint(users_blueprint)

    from source.main.views import main_blueprint
    app.register_blueprint(main_blueprint)

    from source.ml.views import ml_blueprint
    app.register_blueprint(ml_blueprint)

