"""remove a column

Revision ID: 16b9c1fcca34
Revises: 
Create Date: 2023-08-04 09:36:44.985611

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '16b9c1fcca34'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('reports', schema=None) as batch_op:
        batch_op.drop_column('reporter_email')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('reports', schema=None) as batch_op:
        batch_op.add_column(sa.Column('reporter_email', sa.VARCHAR(length=50), nullable=False))

    # ### end Alembic commands ###
