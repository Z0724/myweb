"""empty message

Revision ID: 0f614b5794dc
Revises: 455c300d3c07
Create Date: 2023-03-09 04:15:20.767621

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '0f614b5794dc'
down_revision = '455c300d3c07'
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
    op.drop_table('articles')
    op.drop_table('indexmessageboard')
    with op.batch_alter_table('users', schema=None) as batch_op:
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

    op.create_table('indexmessageboard',
    sa.Column('mb_id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('mb_message', mysql.VARCHAR(length=300), nullable=True),
    sa.Column('mb_data', mysql.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('mb_id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('articles',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('title', mysql.VARCHAR(length=200), nullable=False),
    sa.Column('content', mysql.TEXT(), nullable=False),
    sa.Column('created_at', mysql.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.drop_table('IndexMessageBoard')
    # ### end Alembic commands ###
