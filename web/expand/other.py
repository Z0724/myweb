from flask_login import LoginManager
from web.model import User
from .. import db

login_manager = LoginManager()
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    u = db.users.find_one({'_id':user_id})
    if not u:
        return None
    return User(u)

def init_other(app):
    # global use_cache
    # whoosh_searcher.init_app(app)
    # configure_uploads(app, upload_photos)
    # mail.init_app(app)
    # admin.init_app(app)
    # mongo.init_app(app, "MONGO")
    # oauth.init_app(app)
    login_manager.init_app(app)
    # use_cache = app.config.get('USE_CACHE', False)
    # if use_cache:
    #     cache.init_app(app, {})

    # with app.app_context():
    #     # 添加flask-admin视图
    #     admin.add_view(admin_view.RolesModelView(mongo.db['roles'], '角色管理'))
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
    #     chinese_analyzer = ChineseAnalyzer()
    #     post_schema = Schema(obj_id=ID(unique=True, stored=True), title=TEXT(stored=True, analyzer=chinese_analyzer)
    #                          , content=TEXT(stored=True, analyzer=chinese_analyzer), create_at=DATETIME(stored=True)
    #                          , catalog_id=ID(stored=True), user_id=ID(stored=True))
    #     whoosh_searcher.add_index('posts', post_schema)

    # def clear_cache(f):
    # global use_cache

    # @functools.wraps(f)
    # def decorator(*args, **kwargs):
    #     if use_cache:
    #         cache.clear()
    #     return f(*args, **kwargs)
    # return decorator