"""Initial migration.

Revision ID: 2ff78c43d159
Revises: 
Create Date: 2024-06-22 11:47:01.157813

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2ff78c43d159'
down_revision = None
branch_labels = None
depends_on = None


def upgrade(engine_name):
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name):
    globals()["downgrade_%s" % engine_name]()





def upgrade_():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('people',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_names', sa.String(length=100), nullable=False),
    sa.Column('last_name', sa.String(length=100), nullable=False),
    sa.Column('birth_date', sa.Date(), nullable=False),
    sa.Column('birth_city', sa.String(length=100), nullable=False),
    sa.Column('birth_postal_code', sa.Integer(), nullable=False),
    sa.Column('birth_country', sa.String(length=100), nullable=False),
    sa.Column('death_date', sa.Date(), nullable=True),
    sa.Column('death_city', sa.String(length=100), nullable=True),
    sa.Column('death_postal_code', sa.Integer(), nullable=True),
    sa.Column('death_country', sa.String(length=100), nullable=True),
    sa.Column('unique_hash', sa.String(length=250), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('people', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_people_unique_hash'), ['unique_hash'], unique=True)

    # ### end Alembic commands ###


def downgrade_():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('people', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_people_unique_hash'))

    op.drop_table('people')
    # ### end Alembic commands ###

