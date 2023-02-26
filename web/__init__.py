import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_admin import Admin,AdminIndexView
from web.configs import BaseConfig
from datetime import datetime


app = Flask(__name__)
app.config.from_object(BaseConfig)

db = SQLAlchemy(app)
Migrate(app,db)

# login_manager = LoginManager()
# login_manager.init_app(app)
# login_manager.login_view = 'login'

# admin = Admin(app, name='就是後台', template_mode='bootstrap3',index_view=AdminIndexView(
#         name='導覽',
#         template='base_admin.html',
#         url='/admin')
#         )

from web.blog import blog  
app.register_blueprint(blog, url_prefix='/blog')