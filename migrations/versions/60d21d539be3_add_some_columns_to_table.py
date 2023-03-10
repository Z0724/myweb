"""add some columns to table

Revision ID: 60d21d539be3
Revises: ff88ead3e183
Create Date: 2023-03-13 01:15:16.302756

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '60d21d539be3'
down_revision = 'ff88ead3e183'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('IndexMessageBoard',
    sa.Column('mb_id', sa.Integer(), nullable=False),
    sa.Column('mb_message', sa.String(length=300), nullable=True),
    sa.Column('mb_data', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('mb_id')
    )
    op.drop_table('categories')
    op.drop_table('article_tag')
    op.drop_table('indexmessageboard')
    op.drop_table('tags')
    with op.batch_alter_table('role', schema=None) as batch_op:
        batch_op.drop_index('name')

    op.drop_table('role')
    op.drop_table('articles')
    op.drop_table('users_role')
    with op.batch_alter_table('permission', schema=None) as batch_op:
        batch_op.drop_index('name')

    op.drop_table('permission')
    op.drop_table('role_permission')
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_admin', sa.Boolean(), nullable=True))
        batch_op.alter_column('email',
               existing_type=mysql.VARCHAR(length=64),
               nullable=False)
        batch_op.alter_column('username',
               existing_type=mysql.VARCHAR(length=64),
               nullable=False)
        batch_op.alter_column('password_hash',
               existing_type=mysql.VARCHAR(length=128),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('password_hash',
               existing_type=mysql.VARCHAR(length=128),
               nullable=True)
        batch_op.alter_column('username',
               existing_type=mysql.VARCHAR(length=64),
               nullable=True)
        batch_op.alter_column('email',
               existing_type=mysql.VARCHAR(length=64),
               nullable=True)
        batch_op.drop_column('is_admin')

    op.create_table('role_permission',
    sa.Column('role_id', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('permission_id', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['permission_id'], ['permission.id'], name='role_permission_ibfk_2'),
    sa.ForeignKeyConstraint(['role_id'], ['role.id'], name='role_permission_ibfk_1'),
    sa.PrimaryKeyConstraint('role_id', 'permission_id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('permission',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', mysql.VARCHAR(length=64), nullable=False),
    sa.Column('description', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('is_activate', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True),
    sa.Column('created_at', mysql.DATETIME(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    with op.batch_alter_table('permission', schema=None) as batch_op:
        batch_op.create_index('name', ['name'], unique=False)

    op.create_table('users_role',
    sa.Column('users_id', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('role_id', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['role.id'], name='users_role_ibfk_2'),
    sa.ForeignKeyConstraint(['users_id'], ['users.id'], name='users_role_ibfk_1'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('articles',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('title', mysql.VARCHAR(length=200), nullable=False),
    sa.Column('content', mysql.TEXT(), nullable=False),
    sa.Column('created_at', mysql.DATETIME(), nullable=True),
    sa.Column('user_id', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('category_id', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['category_id'], ['categories.id'], name='articles_ibfk_2'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='articles_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('role',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', mysql.VARCHAR(length=64), nullable=False),
    sa.Column('description', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('created_at', mysql.DATETIME(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    with op.batch_alter_table('role', schema=None) as batch_op:
        batch_op.create_index('name', ['name'], unique=False)

    op.create_table('tags',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', mysql.VARCHAR(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('indexmessageboard',
    sa.Column('mb_id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('mb_message', mysql.VARCHAR(length=300), nullable=True),
    sa.Column('mb_data', mysql.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('mb_id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('article_tag',
    sa.Column('article_id', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('tag_id', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['article_id'], ['articles.id'], name='article_tag_ibfk_1'),
    sa.ForeignKeyConstraint(['tag_id'], ['tags.id'], name='article_tag_ibfk_2'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('categories',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', mysql.VARCHAR(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.drop_table('IndexMessageBoard')
    # ### end Alembic commands ###
