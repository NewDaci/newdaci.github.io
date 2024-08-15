"""empty message

Revision ID: 3dd1b673a582
Revises: dc8d878f052f
Create Date: 2024-04-07 18:10:42.585026

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3dd1b673a582'
down_revision = 'dc8d878f052f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('enrollments', schema=None) as batch_op:
        batch_op.add_column(sa.Column('issue_date', sa.Date(), nullable=True))
        batch_op.add_column(sa.Column('return_date', sa.Date(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('enrollments', schema=None) as batch_op:
        batch_op.drop_column('return_date')
        batch_op.drop_column('issue_date')

    # ### end Alembic commands ###
