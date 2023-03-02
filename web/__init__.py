import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from expand.other import init_other
from flask_admin import Admin,AdminIndexView
from web.configs import config
from datetime import datetime
from flask_mail import Mail

# 各種初始化
db = SQLAlchemy()
migrate = Migrate()
# mail = Mail()
# admin = Admin(app, name='後台管理')


# 图片上传
# from flask_uploads import UploadSet, configure_uploads, IMAGES, ALL
# upload_photos = UploadSet(extensions=ALL)

# Cache
# from flask_cache import Cache
# cache = Cache()
# use_cache = False

# OAuth
# from flask_oauthlib.client import OAuth
# oauth = OAuth()

# from fly_bbs.plugins import WhooshSearcher
# from whoosh.fields import Schema, TEXT, ID, DATETIME
# from jieba.analyse import ChineseAnalyzer
# import functools
# whoosh_searcher = WhooshSearcher()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    db.init_app(app)
    migrate.init_app(app,db)
    init_other(app)
    from web.blog import blog  
    app.register_blueprint(blog, url_prefix='/blog')
    return app











