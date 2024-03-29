from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail, Message
from flask_bootstrap import Bootstrap
from flaskext.markdown import Markdown
from flask_pagedown import PageDown
from flask_admin import Admin, AdminIndexView
from flask_misaka import Misaka
from flask_ckeditor import CKEditor

# 图片上传
# from flask_uploads import UploadSet, configure_uploads, IMAGES, ALL
# upload_photos = UploadSet(extensions=ALL)

# Cache
from flask_cache import Cache
cache = Cache()
use_cache = False

# OAuth
# from flask_oauthlib.client import OAuth
# oauth = OAuth()

from web.expand.whoosh import WhooshSearcher
from whoosh.fields import Schema, TEXT, ID, DATETIME
from jieba.analyse import ChineseAnalyzer
import functools
whoosh_searcher = WhooshSearcher()


# 各種初始化
login_manager = LoginManager()
login_manager.login_view = 'login'
db = SQLAlchemy()
migrate = Migrate()
mail = Mail()
bootstrap = Bootstrap()
admin = Admin(name='後台管理',index_view=AdminIndexView(
        name='後台首頁',
        url='/admin'))
pagedown = PageDown()
ckeditorfield = CKEditor()

# Flask-OAuthlib 和 Flask-Dance


def init_other(app):
    global use_cache
    whoosh_searcher.init_app(app)
    # configure_uploads(app, upload_photos)
    mail.init_app(app)
    Markdown(app) # Markdown簡單版
    Misaka(app) # Markdown進階版
    pagedown.init_app(app)
    db.init_app(app)
    migrate.init_app(app,db)
    admin.init_app(app)
    ckeditorfield.init_app(app)
    # oauth.init_app(app)
    login_manager.init_app(app)
    bootstrap.init_app(app)
    use_cache = app.config.get('USE_CACHE', False)
    if use_cache:
        cache.init_app(app, {})
    with app.app_context():
    #     # 添加flask-admin视图
        from ..model import IndexMessageBoard, User
        from web.admin import admin_views, admin_model
        
        admin.add_view(admin_views.backindex(name='回主頁'))
        admin.add_view(admin_views.I_MessageView(IndexMessageBoard, db.session))
        admin.add_view(admin_views.RolesModelView(admin_model.Role, db.session))
        admin.add_view(admin_views.BaseModelView(User, db.session))
        admin.add_view(admin_views.BaseModelView(admin_model.Permission, db.session))

    #     admin.add_view(admin_view.UsersModelView(mongo.db['users'], '用户管理'))
    #     admin.add_view(admin_view.CatalogsModelView(mongo.db['catalogs'], '栏目管理', category='内容管理'))
    #     admin.add_view(admin_view.PostsModelView(mongo.db['posts'], '帖子管理', category='内容管理'))
    #     admin.add_view(admin_view.PassagewaysModelView(mongo.db['passageways'], '温馨通道', category='推广管理'))
    #     admin.add_view(admin_view.FriendLinksModelView(mongo.db['friend_links'], '友链管理', category='推广管理'))
    #     admin.add_view(admin_view.PagesModelView(mongo.db['pages'], '页面管理', category='推广管理'))
    #     admin.add_view(admin_view.FooterLinksModelView(mongo.db['footer_links'], '底部链接', category='推广管理'))
    #     admin.add_view(admin_view.AdsModelView(mongo.db['ads'], '广告管理', category='推广管理'))
    #     admin.add_view(admin_view.OptionsModelView(mongo.db['options'], '系统设置'))

    #     # 初始化Whoosh索引
        chinese_analyzer = ChineseAnalyzer()
        post_schema = Schema(id=ID(unique=True, stored=True), title=TEXT(stored=True, analyzer=chinese_analyzer)
                             , content=TEXT(stored=True, analyzer=chinese_analyzer), create_at=DATETIME(stored=True)
                             , user_id=ID(stored=True))
        whoosh_searcher.add_index('posts', post_schema)

def clear_cache(f):
    global use_cache

    @functools.wraps(f)
    def decorator(*args, **kwargs):
        if use_cache:
            cache.clear()
        return f(*args, **kwargs)
    return decorator