"""Add defaults and constraints to sets/reps in WorkoutPlan

Revision ID: 3bc64480fe9b
Revises: 297a3326b08e
Create Date: 2025-05-03 18:43:04.662502

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3bc64480fe9b'
down_revision = '297a3326b08e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('workout_plan', schema=None) as batch_op:
        batch_op.alter_column('sets',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('reps',
               existing_type=sa.INTEGER(),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('workout_plan', schema=None) as batch_op:
        batch_op.alter_column('reps',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('sets',
               existing_type=sa.INTEGER(),
               nullable=True)

    # ### end Alembic commands ###
