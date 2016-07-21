"""empty message

Revision ID: 643838ca305f
Revises: 239f31c6b83a
Create Date: 2016-07-21 13:32:38.000928

"""

# revision identifiers, used by Alembic.
revision = '643838ca305f'
down_revision = '239f31c6b83a'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('videos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('url', sa.String(), nullable=True),
    sa.Column('record_date', sa.DateTime(), nullable=True),
    sa.Column('class_team', sa.String(length=50), nullable=True),
    sa.Column('slide_summary', sa.String(length=300), nullable=True),
    sa.Column('teacher', sa.String(length=50), nullable=True),
    sa.Column('title', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('videos')
    ### end Alembic commands ###
