"""issuelibrary

Revision ID: 6884b19a9fd0
Revises: b86354bace64
Create Date: 2023-08-24 17:54:53.056678

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6884b19a9fd0'
down_revision = 'b86354bace64'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('issue_library',
    sa.Column('id', sa.String(length=80), nullable=False),
    sa.Column('reporter', sa.String(length=80), nullable=True),
    sa.Column('date', sa.String(length=80), nullable=True),
    sa.Column('severity', sa.String(length=80), nullable=False),
    sa.Column('cyclename', sa.String(length=80), nullable=False),
    sa.Column('regression', sa.String(length=3), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('issue_library')
    # ### end Alembic commands ###