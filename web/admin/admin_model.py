


# # 建立後台權限資料表(Role)
# class Role(db.Model):
#     __tablename__ = 'roles'

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(64), unique=True)
#     is_admin = db.Column(db.Boolean, default=False)
#     users = db.relationship('User', backref='role', lazy='dynamic')

#     def __repr__(self):
#         return '<Role %r>' % self.name
    
# # 建立後台管理者權限資料表(Admin)
# class Admin(db.Model):
#     __tablename__ = 'admins'

#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

#     user = db.relationship('User', backref=db.backref('admin', uselist=False))
