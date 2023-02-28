from web import db, datetime
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    __tablename__ = 'users'

    id       = db.Column(db.Integer, primary_key = True)
    email    = db.Column(db.String(64),unique=True, index=True)
    username = db.Column(db.String(64),unique=True, index=True)
    password_hash = db.Column(db.String(128))
    regist_date = db.Column(db.DateTime, default = datetime.utcnow())
    last_login = db.Column(db.DateTime, default = datetime.utcnow())

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        # 實際存入的為password_hash，而非password本身
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        # """檢查使用者密碼"""
        return check_password_hash(self.password_hash, password)
    

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