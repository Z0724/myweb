from web.expand.other import db
from datetime import datetime



class Permission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    description = db.Column(db.String(255))
    is_activate = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.now, nullable=False)

class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    description = db.Column(db.String(255))
    permissions = db.relationship('Permission', secondary='role_permission')
    created_at = db.Column(db.DateTime, default=datetime.now, nullable=False)


role_permission = db.Table('role_permission',
    db.Column('role_id', db.Integer, db.ForeignKey('role.id'), primary_key=True),
    db.Column('permission_id', db.Integer, db.ForeignKey('permission.id'), primary_key=True)
)

users_role = db.Table('users_role',
                     db.Column('users_id', db.Integer, db.ForeignKey('users.id')),
                     db.Column('role_id', db.Integer, db.ForeignKey('role.id'))
)

