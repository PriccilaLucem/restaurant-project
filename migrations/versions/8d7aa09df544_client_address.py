"""client_address

Revision ID: 8d7aa09df544
Revises: new_initial
Create Date: 2024-01-21 18:41:45.589251

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8d7aa09df544'
down_revision = 'new_initial'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('client_address',
    sa.Column('client_id', sa.String(length=36), nullable=False),
    sa.Column('address_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['address_id'], ['address.id'], ),
    sa.ForeignKeyConstraint(['client_id'], ['clients.id'], ),
    sa.PrimaryKeyConstraint('client_id', 'address_id')
    )
    with op.batch_alter_table('clients', schema=None) as batch_op:
        batch_op.drop_constraint('clients_address_id_fkey', type_='foreignkey')
        batch_op.drop_column('address_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('clients', schema=None) as batch_op:
        batch_op.add_column(sa.Column('address_id', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.create_foreign_key('clients_address_id_fkey', 'address', ['address_id'], ['id'])

    op.drop_table('client_address')
    # ### end Alembic commands ###
