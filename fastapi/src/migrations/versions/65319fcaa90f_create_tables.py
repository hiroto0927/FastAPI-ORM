"""create tables

Revision ID: 65319fcaa90f
Revises: 
Create Date: 2023-02-18 14:57:01.730341

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '65319fcaa90f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('department',
    sa.Column('dep_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('dep_id')
    )
    op.create_table('member',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=16), nullable=False),
    sa.Column('age', sa.Integer(), nullable=False),
    sa.Column('dep_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['dep_id'], ['department.dep_id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('member')
    op.drop_table('department')
    # ### end Alembic commands ###
