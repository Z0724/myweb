# from flask_sqlalchemy import SQLAlchemy

# db = SQLAlchemy()

# # 使用者資料表
# class User(db.Model):
#     __tablename__ = 'users'
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(255), unique=True, nullable=False)
#     username = db.Column(db.String(50), unique=True, nullable=False)
#     password = db.Column(db.String(255), nullable=False)
#     active = db.Column(db.Boolean, default=True, nullable=False)
#     posts = db.relationship('Post', backref='author', lazy=True)

# # 文章管理資料表
# class Post(db.Model):
#     __tablename__ = 'posts'
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(255), nullable=False)
#     body = db.Column(db.Text, nullable=False)
#     pub_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
#     category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
#     comments = db.relationship('Comment', backref='post', lazy=True)
#     tags = db.relationship('Tag', secondary='post_tags', lazy='subquery', backref=db.backref('posts', lazy=True))

# # 文章分類資料表
# class Category(db.Model):
#     __tablename__ = 'categories'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50), nullable=False)
#     posts = db.relationship('Post', backref='category', lazy=True)

# # 文章標籤資料表
# class Tag(db.Model):
#     __tablename__ = 'tags'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50), nullable=False)

# # 文章與標籤關聯表
# post_tags = db.Table('post_tags',
#     db.Column('post_id', db.Integer, db.ForeignKey('posts.id'), primary_key=True),
#     db.Column('tag_id', db.Integer, db.ForeignKey('tags.id'), primary_key=True)
# )

# # 留言資料表
# class Comment(db.Model):
#     __tablename__ = 'comments'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50), nullable=False)
#     email = db.Column(db.String(255), nullable=False)
#     body = db.Column(db.Text, nullable=False)
#     pub_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
#     post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=False)

# # 訂閱者資料表
# class Subscriber(db.Model):
#     __tablename__ = 'subscribers'
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(255), unique=True, nullable=False)
#     active = db.Column(db.Boolean, default=True, nullable=False)
    
# # 建立資料庫
# db.create_all()
