from os import path
from .admin_config import admin_permissions
from .admin_expand import fill_form_choices, get_user_permissions
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user
from flask_admin.form import Select2Widget
from flask import redirect, url_for, request
from wtforms import form, fields
from wtforms.validators import DataRequired, Email

file_path = path.join(path.dirname(__file__), 'static')


class BaseModelView(ModelView):
    permission_name = ''

    def is_accessible(self):
        # return True
        return current_user.is_authenticated and (current_user.user['is_admin'] or self.permission_name in get_user_permissions(current_user.user))

    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        return redirect(url_for('user.login', next=request.url))
    
class I_MessageForm(form.Form):
    I_Message = fields.StringField('碎碎念', validators=[DataRequired('說點話吧!')])

class I_MessageView(BaseModelView):
    column_list = ('I_Message', )
    column_labels = dict(I_Message='碎碎念')
    column_sortable_list = 'I_Message'
    column_default_sort = ('I_Message', False)
    can_create = True
    can_delete = True
    can_edit = True
    form = I_MessageForm
    permission_name = 'soliloquy'

    def create_form(self, obj=None):
        real_form = super(I_MessageView, self).create_form(obj)
        return real_form

    def edit_form(self, obj=None):
        real_form = super(I_MessageView, self).edit_form(obj)
        return real_form