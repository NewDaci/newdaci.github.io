"""empty message

Revision ID: 27e9e4d82435
Revises: 35051d041b1a
Create Date: 2024-04-02 11:13:40.647403

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '27e9e4d82435'
down_revision = '35051d041b1a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('book', schema=None) as batch_op:
        batch_op.add_column(sa.Column('rating', sa.Integer(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('book', schema=None) as batch_op:
        batch_op.drop_column('rating')

    # ### end Alembic commands ###
