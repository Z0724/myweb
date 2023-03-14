from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from web.expand.other import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id       = db.Column(db.Integer, primary_key = True)
    email    = db.Column(db.String(64),unique=True, index=True, nullable=False)
    username = db.Column(db.String(64),unique=True, index=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    regist_date = db.Column(db.DateTime, default = datetime.utcnow())
    last_login = db.Column(db.DateTime, default = datetime.utcnow())
    # roles = db.relationship('Role', secondary='user_role', backref=db.backref('users', lazy=True))
    # role_id = db.Column(db.Integer, db.ForeignKey('role.id'))

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        # 實際存入的為password_hash，而非password本身
        self.password_hash = generate_password_hash(password)
    # 檢查密碼
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    # 調用密碼時顯示錯誤
    @property
    def password(self):
        raise AttributeError('不可讀取密碼')
    # 修改密碼用
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)




    

class R(dict): # 網頁訊息管理(存在字典內)

    @staticmethod # 靜態方法，類似在類裡面放獨立函式，放一起方便歸類的概念
    def ok(msg=None, data=None):
        r = R()
        r.put('status', 0)
        r.put('msg', msg)
        r.put('data', data)
        return r
    
    @staticmethod
    def fail(code=404, msg=None):
        r = R()
        r.put('status', code)
        r.put('msg', msg)
        return r

    def put(self, k, v): # 儲存訊息
        self.__setitem__(k, v)
        return self

    def get_status(self): # 取得該status的訊息數字
        return self.get('status')

    def get_msg(self): # 取得該msg的訊息內容
        return self.get('msg')

# 首頁碎碎念
class IndexMessageBoard(db.Model):
    __tablename__ = 'IndexMessageBoard'
    
    # columns
    mb_id       = db.Column(db.Integer, primary_key = True)
    mb_message = db.Column(db.String(300))
    mb_data = db.Column(db.DateTime, default=datetime.utcnow)
    def __init__(self, mb_message):
        self.mb_message = mb_message