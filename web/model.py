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