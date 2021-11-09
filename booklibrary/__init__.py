from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from booklibrary.config import Config
from flask_marshmallow import Marshmallow



ma = Marshmallow()
db = SQLAlchemy()
migrate = Migrate(db)
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
mail = Mail()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from booklibrary.users.routes import users
    from booklibrary.books.routes import booky
    from booklibrary.books.routes import my_books
    from booklibrary.main.routes import main
    from booklibrary.errors.handlers import errors
    from booklibrary.help.routes import helps
    from booklibrary.tests.routes import test


    app.register_blueprint(users)
    app.register_blueprint(booky)
    app.register_blueprint(my_books)
    app.register_blueprint(main)
    app.register_blueprint(errors)
    app.register_blueprint(helps)
    app.register_blueprint(test)

    return app