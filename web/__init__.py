from flask import Flask
from web.configs import config
from web.expand.other import init_other


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    init_other(app)
    from web.blog import blog
    app.register_blueprint(blog, url_prefix='/blog')
    return app

