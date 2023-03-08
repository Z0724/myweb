from web import datetime
from web.expand.other import db
from app import app
from web.model import User



# 建立文章管理資料表(Article)
class Article(db.Model):
    __tablename__ = 'articles'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    # user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    # author = db.relationship('User', backref=db.backref('articles', lazy=True))

    def __init__(self, title, content):
        self.title = title
        self.content = content

    def __repr__(self):
        return '<Article %r>' % self.title
    

# # 文章分類資料表
# class Category(db.Model):
#     __tablename__ = 'categories'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50), nullable=False)
#     articles = db.relationship('Article', backref='category', lazy=True)

# # 文章標籤資料表
# class Tag(db.Model):
#     __tablename__ = 'tags'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50), nullable=False)

# # 文章與標籤關聯表
# article_tags = db.Table('article_tags',
#     db.Column('article_id', db.Integer, db.ForeignKey('articles.id'), primary_key=True),
#     db.Column('tag_id', db.Integer, db.ForeignKey('tags.id'), primary_key=True)
# )






with app.app_context():
    db.create_all()