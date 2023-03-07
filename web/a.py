# from flask_login import UserMixin
# from werkzeug.security import generate_password_hash, check_password_hash
# from datetime import datetime

# class User(db.Model, UserMixin):
#     __tablename__ = 'users'

#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     username = db.Column(db.String(64), unique=True, nullable=False)
#     password_hash = db.Column(db.String(128), nullable=False)
#     is_admin = db.Column(db.Boolean, default=False)
#     created_at = db.Column(db.DateTime, default=datetime.utcnow)

#     @property
#     def password(self):
#         raise AttributeError('password is not a readable attribute')

#     @password.setter
#     def password(self, password):
#         self.password_hash = generate_password_hash(password)

#     def verify_password(self, password):
#         return check_password_hash(self.password_hash, password)

# 建立文章管理資料表(Article)
# class Article(db.Model):
#     __tablename__ = 'articles'

#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(200), nullable=False)
#     content = db.Column(db.Text, nullable=False)
#     created_at = db.Column(db.DateTime, default=datetime.utcnow)
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

#     user = db.relationship('User', backref=db.backref('articles', lazy='dynamic'))

#     def __repr__(self):
#         return '<Article %r>' % self.title

# 建立後台權限資料表(Role)
# class Role(db.Model):
#     __tablename__ = 'roles'

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(64), unique=True)
#     is_admin = db.Column(db.Boolean, default=False)
#     users = db.relationship('User', backref='role', lazy='dynamic')

#     def __repr__(self):
#         return '<Role %r>' % self.name


# 建立後台管理者權限資料表(Admin)
# class Admin(db.Model):
#     __tablename__ = 'admins'

#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

#     user = db.relationship('User', backref=db.backref('admin', uselist=False))
