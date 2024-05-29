"""empty message

Revision ID: ff4c79c172e7
Revises: 81e1f9cf8205
Create Date: 2024-04-30 17:17:33.204559

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ff4c79c172e7'
down_revision = '81e1f9cf8205'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tags', schema=None) as batch_op:
        batch_op.alter_column('user_id',
               existing_type=sa.VARCHAR(length=140),
               type_=sa.Integer(),
               existing_nullable=True)
        batch_op.drop_index('ix_tags_user_id')
        batch_op.create_index(batch_op.f('ix_tags_user_id'), ['user_id'], unique=False)
        batch_op.create_foreign_key('fk_user_id', 'user', ['user_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tags', schema=None) as batch_op:
        batch_op.drop_constraint('fk_user_id', type_='foreignkey')
        batch_op.drop_index(batch_op.f('ix_tags_user_id'))
        batch_op.create_index('ix_tags_user_id', ['user_id'], unique=1)
        batch_op.alter_column('user_id',
               existing_type=sa.Integer(),
               type_=sa.VARCHAR(length=140),
               existing_nullable=True)

    # ### end Alembic commands ###