"""empty message

Revision ID: 7e4ffa39d50d
Revises: 6bc355f89e39
Create Date: 2023-08-04 07:57:05.091565

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7e4ffa39d50d'
down_revision = '6bc355f89e39'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('roles', schema=None) as batch_op:
        batch_op.add_column(sa.Column('default', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('permissions', sa.Integer(), nullable=True))
        batch_op.create_index(batch_op.f('ix_roles_default'), ['default'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('roles', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_roles_default'))
        batch_op.drop_column('permissions')
        batch_op.drop_column('default')

    # ### end Alembic commands ###
