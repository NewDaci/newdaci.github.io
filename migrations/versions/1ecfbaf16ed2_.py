"""empty message

Revision ID: 1ecfbaf16ed2
Revises: 3e0966bc2c05
Create Date: 2024-03-15 10:35:09.686905

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1ecfbaf16ed2'
down_revision = '3e0966bc2c05'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('book', schema=None) as batch_op:
        batch_op.add_column(sa.Column('content2', sa.LargeBinary(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('book', schema=None) as batch_op:
        batch_op.drop_column('content2')

    # ### end Alembic commands ###
