"""create users table

Revision ID: [generate a unique ID, maybe 'a1b2c3d4e5f6']
Revises: 
Create Date: [current timestamp]

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic
revision = 'a1b2c3d4e5f6'  # Use this same ID
down_revision = None  # This makes it the first migration
branch_labels = None
depends_on = None

def upgrade():
    op.create_table('users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('first_name', sa.String(length=50), nullable=False),
        sa.Column('last_name', sa.String(length=50), nullable=False),
        sa.Column('email', sa.String(length=120), nullable=False),
        sa.Column('password_hash', sa.String(length=128), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)

def downgrade():
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')