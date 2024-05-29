"""empty message

Revision ID: fb1b292ab425
Revises: 9a23653e0592
Create Date: 2024-05-30 01:01:47.378442

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fb1b292ab425'
down_revision = '9a23653e0592'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_encounter',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('encountered_user_id', sa.Integer(), nullable=False),
    sa.Column('skipped', sa.Boolean(), nullable=True),
    sa.Column('last_encountered', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['encountered_user_id'], ['user.id'], name='fk_encountered_user_id'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='fk_encounter_id'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_encounter')
    # ### end Alembic commands ###
