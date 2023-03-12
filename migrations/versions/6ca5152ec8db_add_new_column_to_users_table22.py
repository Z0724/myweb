"""Add new column to users table22

Revision ID: 6ca5152ec8db
Revises: 60d21d539be3
Create Date: 2023-03-13 01:24:43.946527

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '6ca5152ec8db'
down_revision = '60d21d539be3'
branch_labels = None
depends_on = None


def upgrade():
    # Add new column to users table
    op.add_column('users', sa.Column('is_admin', sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # Remove new column from users table
    op.drop_column('users', 'is_admin')
