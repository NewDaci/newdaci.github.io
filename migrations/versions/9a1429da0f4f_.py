"""empty message

Revision ID: 9a1429da0f4f
Revises: dbdf5b6028f5
Create Date: 2024-04-07 13:26:10.694346

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9a1429da0f4f'
down_revision = 'dbdf5b6028f5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('book', schema=None) as batch_op:
        batch_op.drop_column('genre')

    with op.batch_alter_table('book_req', schema=None) as batch_op:
        batch_op.add_column(sa.Column('req_days', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('issue_date', sa.Date(), nullable=True))
        batch_op.add_column(sa.Column('return_date', sa.Date(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('book_req', schema=None) as batch_op:
        batch_op.drop_column('return_date')
        batch_op.drop_column('issue_date')
        batch_op.drop_column('req_days')

    with op.batch_alter_table('book', schema=None) as batch_op:
        batch_op.add_column(sa.Column('genre', sa.VARCHAR(), nullable=True))

    # ### end Alembic commands ###
