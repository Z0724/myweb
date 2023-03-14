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
        return current_user.is_authenticated and (current_user.is_admin or self.permission_name in get_user_permissions(current_user))

    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        return redirect(url_for('blog.login', next=request.url))
    
class I_MessageForm(form.Form):
    I_Message = fields.StringField('碎碎念', validators=[DataRequired('說點話吧!')])
    form_columns = ('mb_message',)

class I_MessageView(BaseModelView):
    column_list = ('mb_message',)
    column_labels = dict(mb_message='碎碎念')
    column_sortable_list = ('mb_message',)
    column_default_sort = ('mb_message', False)
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

class RolesForm(form.Form):
    name = fields.StringField('角色名', validators=[DataRequired('角色名不能为空')])
    permissions = fields.SelectMultipleField('权限', widget=Select2Widget(multiple=True), validators=[DataRequired('权限不能为空')])


class RolesModelView(BaseModelView):
    column_list = ('name', )
    column_labels = dict(name='角色名')
    column_sortable_list = ('name',)
    column_default_sort = ('name', False)
    can_create = True
    can_delete = True
    can_edit = True
    form = RolesForm
    permission_name = 'roles'

    def create_form(self, obj=None):
        real_form = super(RolesModelView, self).create_form(obj)
        user_permissions = get_user_permissions(current_user)
        real_form.permissions.choices = list(filter(lambda p: p[0] in user_permissions, admin_permissions))
        return real_form

    def edit_form(self, obj=None):
        real_form = super(RolesModelView, self).edit_form(obj)
        user_permissions = get_user_permissions(current_user)
        real_form.permissions.choices = list(filter(lambda p: p[0] in user_permissions, admin_permissions))
        return real_form

