"""empty message

Revision ID: 9a23653e0592
Revises: ff4c79c172e7
Create Date: 2024-05-29 18:09:45.130753

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9a23653e0592'
down_revision = 'ff4c79c172e7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tags', schema=None) as batch_op:
        batch_op.add_column(sa.Column('description', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('tags', sa.JSON(), nullable=True))
        batch_op.drop_index('ix_tags_tag_1')
        batch_op.drop_index('ix_tags_tag_2')
        batch_op.drop_index('ix_tags_tag_3')
        batch_op.drop_index('ix_tags_tag_4')
        batch_op.create_index(batch_op.f('ix_tags_description'), ['description'], unique=False)
        batch_op.drop_column('tag_2')
        batch_op.drop_column('tag_4')
        batch_op.drop_column('tag_1')
        batch_op.drop_column('tag_3')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tags', schema=None) as batch_op:
        batch_op.add_column(sa.Column('tag_3', sa.VARCHAR(length=140), nullable=True))
        batch_op.add_column(sa.Column('tag_1', sa.VARCHAR(length=140), nullable=True))
        batch_op.add_column(sa.Column('tag_4', sa.VARCHAR(length=140), nullable=True))
        batch_op.add_column(sa.Column('tag_2', sa.VARCHAR(length=140), nullable=True))
        batch_op.drop_index(batch_op.f('ix_tags_description'))
        batch_op.create_index('ix_tags_tag_4', ['tag_4'], unique=False)
        batch_op.create_index('ix_tags_tag_3', ['tag_3'], unique=False)
        batch_op.create_index('ix_tags_tag_2', ['tag_2'], unique=False)
        batch_op.create_index('ix_tags_tag_1', ['tag_1'], unique=False)
        batch_op.drop_column('tags')
        batch_op.drop_column('description')

    # ### end Alembic commands ###