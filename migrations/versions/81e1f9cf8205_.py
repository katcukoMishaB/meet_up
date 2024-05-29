"""empty message

Revision ID: 81e1f9cf8205
Revises: 4a9dad9ce43f
Create Date: 2024-04-30 16:47:41.999913

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '81e1f9cf8205'
down_revision = '4a9dad9ce43f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tags',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.String(length=140), nullable=True),
    sa.Column('tag_1', sa.String(length=140), nullable=True),
    sa.Column('tag_2', sa.String(length=140), nullable=True),
    sa.Column('tag_3', sa.String(length=140), nullable=True),
    sa.Column('tag_4', sa.String(length=140), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('tags', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_tags_tag_1'), ['tag_1'], unique=False)
        batch_op.create_index(batch_op.f('ix_tags_tag_2'), ['tag_2'], unique=False)
        batch_op.create_index(batch_op.f('ix_tags_tag_3'), ['tag_3'], unique=False)
        batch_op.create_index(batch_op.f('ix_tags_tag_4'), ['tag_4'], unique=False)
        batch_op.create_index(batch_op.f('ix_tags_user_id'), ['user_id'], unique=True)

    with op.batch_alter_table('posts', schema=None) as batch_op:
        batch_op.drop_index('ix_posts_body')
        batch_op.drop_index('ix_posts_timestamp')
        batch_op.drop_index('ix_posts_user_id')

    op.drop_table('posts')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('posts',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('body', sa.VARCHAR(length=140), nullable=True),
    sa.Column('timestamp', sa.DATETIME(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('posts', schema=None) as batch_op:
        batch_op.create_index('ix_posts_user_id', ['user_id'], unique=False)
        batch_op.create_index('ix_posts_timestamp', ['timestamp'], unique=False)
        batch_op.create_index('ix_posts_body', ['body'], unique=1)

    with op.batch_alter_table('tags', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_tags_user_id'))
        batch_op.drop_index(batch_op.f('ix_tags_tag_4'))
        batch_op.drop_index(batch_op.f('ix_tags_tag_3'))
        batch_op.drop_index(batch_op.f('ix_tags_tag_2'))
        batch_op.drop_index(batch_op.f('ix_tags_tag_1'))

    op.drop_table('tags')
    # ### end Alembic commands ###
