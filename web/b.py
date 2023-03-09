

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
