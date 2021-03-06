"""empty message

Revision ID: 0a1371ca131f
Revises: b17a11418818
Create Date: 2020-03-20 08:51:13.328090

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0a1371ca131f'
down_revision = 'b17a11418818'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('student',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_student_email'), 'student', ['email'], unique=True)
    op.create_index(op.f('ix_student_username'), 'student', ['username'], unique=True)
    op.create_table('subject',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('description', sa.String(length=100), nullable=True),
    sa.Column('subject_name', sa.String(length=102), nullable=True),
    sa.Column('student_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['student_id'], ['student.id'], ),
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
    op.drop_index(op.f('ix_student_username'), table_name='student')
    op.drop_index(op.f('ix_student_email'), table_name='student')
    op.drop_table('student')
    # ### end Alembic commands ###
