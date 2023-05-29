"""Init

Revision ID: f35c9bc1f9f6
Revises: 
Create Date: 2023-05-28 22:19:21.767142

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'f35c9bc1f9f6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('file',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('root_folder', sa.TEXT(), nullable=True),
    sa.Column('file_path', sa.TEXT(), nullable=True),
    sa.Column('file_folder', sa.TEXT(), nullable=True),
    sa.Column('file_name', sa.String(length=255), nullable=True),
    sa.Column('file_ext', sa.String(length=11), nullable=True),
    sa.Column('file_size', sa.BigInteger(), nullable=True),
    sa.Column('file_ctime', sa.TIMESTAMP(), nullable=True),
    sa.Column('file_mtime', sa.TIMESTAMP(), nullable=True),
    sa.Column('date_c', sa.String(length=11), nullable=True),
    sa.Column('date_m', sa.String(length=11), nullable=True),
    sa.Column('date_u', sa.String(length=11), nullable=True),
    sa.Column('fpath', sa.TEXT(), nullable=True),
    sa.Column('fpath_md5', sa.TEXT(), nullable=True),
    sa.Column('field', sa.String(length=255), nullable=True),
    sa.Column('areaoil', sa.String(length=255), nullable=True),
    sa.Column('lu', sa.String(length=255), nullable=True),
    sa.Column('well', sa.String(length=255), nullable=True),
    sa.Column('lat', sa.Float(), nullable=True),
    sa.Column('lon', sa.Float(), nullable=True),
    sa.Column('report_name', sa.TEXT(), nullable=True),
    sa.Column('report_text', sa.TEXT(), nullable=True),
    sa.Column('report_author', sa.TEXT(), nullable=True),
    sa.Column('report_year', sa.Integer(), nullable=True),
    sa.Column('report_tgf', sa.TEXT(), nullable=True),
    sa.Column('is_deleted', sa.Boolean(), nullable=True),
    sa.Column('lastupdate', sa.TIMESTAMP(), nullable=True),
    sa.Column('file_path_fts', postgresql.TSVECTOR(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###

    op.drop_table('file')

    # ### end Alembic commands ###