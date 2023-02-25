

# class Func(db.Model):
#     __tablename__ = 'funcs'
#     id = db.Column(db.Integer, primary_key=True)
#     func_module_name = db.Column(db.String(50))
#     func_description = db.Column(db.String(100))
#     func_is_activate = db.Column(db.Boolean, default=True)
#     func_remark = db.Column(db.String(100))

#     def __init__(self, func_module_name, func_description, func_is_activate=True, func_remark=None):
#         self.func_module_name = func_module_name
#         self.func_description = func_description
#         self.func_is_activate = func_is_activate
#         self.func_remark = func_remark

#     def __repr__(self):
#         return 'id = %i, module_name = %s, is_activate = %s'

# with app.app_context():
#     db.create_all()