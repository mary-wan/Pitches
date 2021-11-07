"""Add table

Revision ID: ab7ba12d4a53
Revises: 5733e0439457
Create Date: 2021-11-08 01:34:31.110286

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ab7ba12d4a53'
down_revision = '5733e0439457'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('usr_id', sa.Integer(), nullable=True))
    op.drop_constraint('comments_user_id_fkey', 'comments', type_='foreignkey')
    op.create_foreign_key(None, 'comments', 'users', ['usr_id'], ['id'])
    op.drop_column('comments', 'user_id')
    op.add_column('downvotes', sa.Column('usr_id', sa.Integer(), nullable=True))
    op.drop_constraint('downvotes_user_id_fkey', 'downvotes', type_='foreignkey')
    op.create_foreign_key(None, 'downvotes', 'users', ['usr_id'], ['id'])
    op.drop_column('downvotes', 'user_id')
    op.add_column('pitches', sa.Column('usr_id', sa.Integer(), nullable=True))
    op.drop_constraint('pitches_user_id_fkey', 'pitches', type_='foreignkey')
    op.create_foreign_key(None, 'pitches', 'users', ['usr_id'], ['id'])
    op.drop_column('pitches', 'user_id')
    op.add_column('upvotes', sa.Column('usr_id', sa.Integer(), nullable=True))
    op.drop_constraint('upvotes_user_id_fkey', 'upvotes', type_='foreignkey')
    op.create_foreign_key(None, 'upvotes', 'users', ['usr_id'], ['id'])
    op.drop_column('upvotes', 'user_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('upvotes', sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'upvotes', type_='foreignkey')
    op.create_foreign_key('upvotes_user_id_fkey', 'upvotes', 'users', ['user_id'], ['id'])
    op.drop_column('upvotes', 'usr_id')
    op.add_column('pitches', sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'pitches', type_='foreignkey')
    op.create_foreign_key('pitches_user_id_fkey', 'pitches', 'users', ['user_id'], ['id'])
    op.drop_column('pitches', 'usr_id')
    op.add_column('downvotes', sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'downvotes', type_='foreignkey')
    op.create_foreign_key('downvotes_user_id_fkey', 'downvotes', 'users', ['user_id'], ['id'])
    op.drop_column('downvotes', 'usr_id')
    op.add_column('comments', sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.create_foreign_key('comments_user_id_fkey', 'comments', 'users', ['user_id'], ['id'])
    op.drop_column('comments', 'usr_id')
    # ### end Alembic commands ###
