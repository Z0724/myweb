import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_admin import Admin,AdminIndexView
from web.configs import BaseConfig
from datetime import datetime
from flask_mail import Mail

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(BaseConfig)
    db.init_app(app)
    migrate.init_app(app,db)
    # loginmanager.init_app(app)
    from web.blog import blog  
    app.register_blueprint(blog, url_prefix='/blog')
    return app


# login_manager = LoginManager()
# login_manager.init_app(app)
# login_manager.login_view = 'login'

# mail = Mail()
# admin = Admin(app, name='後台管理')



