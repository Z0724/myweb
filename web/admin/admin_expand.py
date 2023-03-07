from .admin_config import admin_permissions


def fill_form_choices(form_field, collection_name: str, db_field_name: str):
    from web.expand.other import db
    form_field.choices = [(str(item['_id']), item[db_field_name]) for item in db[collection_name].find()]


def get_user_permissions(users):
    from web.expand.other import db
    if users['is_admin']:
        return set([p[0] for p in admin_permissions])
    if 'role_ids' not in users:
        return set()
    roles = db.roles.find({'_id': {'$in': users['role_ids']}})
    permissions = []
    for role in roles:
        permissions += role['permissions']
    return set(permissions)