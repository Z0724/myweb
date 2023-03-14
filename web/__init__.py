from flask import Flask
from web.configs import config
from web.expand.other import init_other



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
    init_other(app)
    from web.blog import blog
    app.register_blueprint(blog, url_prefix='/blog')
    return app

