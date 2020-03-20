"""subject table

Revision ID: fb35fd8e0709
Revises: e2461dd73d50
Create Date: 2020-03-19 13:43:28.728207

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fb35fd8e0709'
down_revision = 'e2461dd73d50'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('subject',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('description', sa.String(length=100), nullable=True),
    sa.Column('subject_name', sa.String(length=102), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_index(op.f('ix_subject_description'), 'subject', ['description'], unique=False)
    op.create_index(op.f('ix_subject_subject_name'), 'subject', ['subject_name'], unique=False)
    op.create_index(op.f('ix_subject_timestamp'), 'subject', ['timestamp'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_subject_timestamp'), table_name='subject')
    op.drop_index(op.f('ix_subject_subject_name'), table_name='subject')
    op.drop_index(op.f('ix_subject_description'), table_name='subject')
    op.drop_table('subject')
    # ### end Alembic commands ###
