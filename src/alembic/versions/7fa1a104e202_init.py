"""Init

Revision ID: 7fa1a104e202
Revises: 
Create Date: 2023-07-26 21:34:18.484516

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '7fa1a104e202'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ext',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ext', sa.TEXT(), nullable=True),
    sa.Column('category', sa.TEXT(), nullable=True),
    sa.Column('description', sa.TEXT(), nullable=True),
    sa.Column('product', sa.TEXT(), nullable=True),
    sa.Column('is_project', sa.TEXT(), nullable=True),
    sa.Column('lastupdate', sa.TIMESTAMP(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_ext_category'), 'ext', ['category'], unique=False)
    op.create_index(op.f('ix_ext_description'), 'ext', ['description'], unique=False)
    op.create_index(op.f('ix_ext_ext'), 'ext', ['ext'], unique=False)
    op.create_index(op.f('ix_ext_is_project'), 'ext', ['is_project'], unique=False)
    op.create_index(op.f('ix_ext_product'), 'ext', ['product'], unique=False)
    op.create_table('file',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('f_root', sa.TEXT(), nullable=True),
    sa.Column('f_path', sa.TEXT(), nullable=True),
    sa.Column('f_folder', sa.TEXT(), nullable=True),
    sa.Column('f_name', sa.String(length=255), nullable=True),
    sa.Column('f_ext', sa.String(length=255), nullable=True),
    sa.Column('f_size', sa.BigInteger(), nullable=True),
    sa.Column('f_ctime', sa.TIMESTAMP(), nullable=True),
    sa.Column('f_mtime', sa.TIMESTAMP(), nullable=True),
    sa.Column('f_atime', sa.TIMESTAMP(), nullable=True),
    sa.Column('f_path_md5', sa.TEXT(), nullable=True),
    sa.Column('f_text', sa.TEXT(), nullable=True),
    sa.Column('ngp', sa.String(length=255), nullable=True),
    sa.Column('ngo', sa.String(length=255), nullable=True),
    sa.Column('ngr', sa.String(length=255), nullable=True),
    sa.Column('field', sa.String(length=255), nullable=True),
    sa.Column('areaoil', sa.String(length=255), nullable=True),
    sa.Column('lu', sa.String(length=255), nullable=True),
    sa.Column('lu_num', sa.String(length=255), nullable=True),
    sa.Column('well', sa.String(length=255), nullable=True),
    sa.Column('lat', sa.Float(), nullable=True),
    sa.Column('lon', sa.Float(), nullable=True),
    sa.Column('report_id', sa.Integer(), nullable=True),
    sa.Column('report_name', sa.TEXT(), nullable=True),
    sa.Column('report_text', sa.TEXT(), nullable=True),
    sa.Column('report_author', sa.TEXT(), nullable=True),
    sa.Column('report_year', sa.Integer(), nullable=True),
    sa.Column('report_tgf', sa.TEXT(), nullable=True),
    sa.Column('dog_zakaz', sa.TEXT(), nullable=True),
    sa.Column('dog_name', sa.TEXT(), nullable=True),
    sa.Column('dog_num', sa.TEXT(), nullable=True),
    sa.Column('dog_date', sa.TIMESTAMP(), nullable=True),
    sa.Column('dog_isp', sa.TEXT(), nullable=True),
    sa.Column('dog_rep', sa.TEXT(), nullable=True),
    sa.Column('dog_prikaz', sa.TEXT(), nullable=True),
    sa.Column('is_deleted', sa.Boolean(), nullable=True),
    sa.Column('lastupdate', sa.TIMESTAMP(), nullable=True),
    sa.Column('file_path_fts', postgresql.TSVECTOR(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_file_areaoil'), 'file', ['areaoil'], unique=False)
    op.create_index(op.f('ix_file_dog_date'), 'file', ['dog_date'], unique=False)
    op.create_index(op.f('ix_file_dog_isp'), 'file', ['dog_isp'], unique=False)
    op.create_index(op.f('ix_file_dog_name'), 'file', ['dog_name'], unique=False)
    op.create_index(op.f('ix_file_dog_num'), 'file', ['dog_num'], unique=False)
    op.create_index(op.f('ix_file_dog_prikaz'), 'file', ['dog_prikaz'], unique=False)
    op.create_index(op.f('ix_file_dog_rep'), 'file', ['dog_rep'], unique=False)
    op.create_index(op.f('ix_file_dog_zakaz'), 'file', ['dog_zakaz'], unique=False)
    op.create_index(op.f('ix_file_f_ext'), 'file', ['f_ext'], unique=False)
    op.create_index(op.f('ix_file_f_folder'), 'file', ['f_folder'], unique=False)
    op.create_index(op.f('ix_file_f_name'), 'file', ['f_name'], unique=False)
    op.create_index(op.f('ix_file_f_path'), 'file', ['f_path'], unique=False)
    op.create_index(op.f('ix_file_f_path_md5'), 'file', ['f_path_md5'], unique=False)
    op.create_index(op.f('ix_file_f_root'), 'file', ['f_root'], unique=False)
    op.create_index(op.f('ix_file_field'), 'file', ['field'], unique=False)
    op.create_index(op.f('ix_file_lu'), 'file', ['lu'], unique=False)
    op.create_index(op.f('ix_file_lu_num'), 'file', ['lu_num'], unique=False)
    op.create_index(op.f('ix_file_ngo'), 'file', ['ngo'], unique=False)
    op.create_index(op.f('ix_file_ngp'), 'file', ['ngp'], unique=False)
    op.create_index(op.f('ix_file_ngr'), 'file', ['ngr'], unique=False)
    op.create_index(op.f('ix_file_report_author'), 'file', ['report_author'], unique=False)
    op.create_index(op.f('ix_file_report_id'), 'file', ['report_id'], unique=False)
    op.create_index(op.f('ix_file_report_name'), 'file', ['report_name'], unique=False)
    op.create_index(op.f('ix_file_report_year'), 'file', ['report_year'], unique=False)
    op.create_index(op.f('ix_file_well'), 'file', ['well'], unique=False)
    op.create_table('file_src',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('folder_src', sa.TEXT(), nullable=True),
    sa.Column('lastupdate', sa.TIMESTAMP(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_file_src_folder_src'), 'file_src', ['folder_src'], unique=True)
    # op.drop_table('spatial_ref_sys')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('spatial_ref_sys',
    sa.Column('srid', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('auth_name', sa.VARCHAR(length=256), autoincrement=False, nullable=True),
    sa.Column('auth_srid', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('srtext', sa.VARCHAR(length=2048), autoincrement=False, nullable=True),
    sa.Column('proj4text', sa.VARCHAR(length=2048), autoincrement=False, nullable=True),
    sa.CheckConstraint('(srid > 0) AND (srid <= 998999)', name='spatial_ref_sys_srid_check'),
    sa.PrimaryKeyConstraint('srid', name='spatial_ref_sys_pkey')
    )
    op.drop_index(op.f('ix_file_src_folder_src'), table_name='file_src')
    op.drop_table('file_src')
    op.drop_index(op.f('ix_file_well'), table_name='file')
    op.drop_index(op.f('ix_file_report_year'), table_name='file')
    op.drop_index(op.f('ix_file_report_name'), table_name='file')
    op.drop_index(op.f('ix_file_report_id'), table_name='file')
    op.drop_index(op.f('ix_file_report_author'), table_name='file')
    op.drop_index(op.f('ix_file_ngr'), table_name='file')
    op.drop_index(op.f('ix_file_ngp'), table_name='file')
    op.drop_index(op.f('ix_file_ngo'), table_name='file')
    op.drop_index(op.f('ix_file_lu_num'), table_name='file')
    op.drop_index(op.f('ix_file_lu'), table_name='file')
    op.drop_index(op.f('ix_file_field'), table_name='file')
    op.drop_index(op.f('ix_file_f_root'), table_name='file')
    op.drop_index(op.f('ix_file_f_path_md5'), table_name='file')
    op.drop_index(op.f('ix_file_f_path'), table_name='file')
    op.drop_index(op.f('ix_file_f_name'), table_name='file')
    op.drop_index(op.f('ix_file_f_folder'), table_name='file')
    op.drop_index(op.f('ix_file_f_ext'), table_name='file')
    op.drop_index(op.f('ix_file_dog_zakaz'), table_name='file')
    op.drop_index(op.f('ix_file_dog_rep'), table_name='file')
    op.drop_index(op.f('ix_file_dog_prikaz'), table_name='file')
    op.drop_index(op.f('ix_file_dog_num'), table_name='file')
    op.drop_index(op.f('ix_file_dog_name'), table_name='file')
    op.drop_index(op.f('ix_file_dog_isp'), table_name='file')
    op.drop_index(op.f('ix_file_dog_date'), table_name='file')
    op.drop_index(op.f('ix_file_areaoil'), table_name='file')
    op.drop_table('file')
    op.drop_index(op.f('ix_ext_product'), table_name='ext')
    op.drop_index(op.f('ix_ext_is_project'), table_name='ext')
    op.drop_index(op.f('ix_ext_ext'), table_name='ext')
    op.drop_index(op.f('ix_ext_description'), table_name='ext')
    op.drop_index(op.f('ix_ext_category'), table_name='ext')
    op.drop_table('ext')
    # ### end Alembic commands ###