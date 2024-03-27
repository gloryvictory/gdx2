"""Init

Revision ID: fae1af10a620
Revises: 
Create Date: 2023-08-10 23:06:00.685366

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'fae1af10a620'
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
    sa.PrimaryKeyConstraint('id'),
    comment='Расширения'
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
    sa.PrimaryKeyConstraint('id'),
    comment='Файлы'
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
    op.create_table('nsi_area',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name_ru', sa.String(length=255), nullable=True),
    sa.Column('lat', sa.Float(), nullable=True),
    sa.Column('lon', sa.Float(), nullable=True),
    sa.Column('crs', sa.Integer(), nullable=True),
    sa.Column('hash', sa.String(length=255), nullable=True),
    sa.Column('lastupdate', sa.TIMESTAMP(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    comment='НСИ Площади'
    )
    op.create_index(op.f('ix_nsi_area_name_ru'), 'nsi_area', ['name_ru'], unique=False)
    op.create_table('nsi_field',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name_ru', sa.String(length=255), nullable=True),
    sa.Column('lat', sa.Float(), nullable=True),
    sa.Column('lon', sa.Float(), nullable=True),
    sa.Column('crs', sa.Integer(), nullable=True),
    sa.Column('hash', sa.String(length=255), nullable=True),
    sa.Column('lastupdate', sa.TIMESTAMP(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    comment='НСИ Месторождения'
    )
    op.create_index(op.f('ix_nsi_field_name_ru'), 'nsi_field', ['name_ru'], unique=False)
    op.create_table('nsi_lu',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name_ru', sa.String(length=255), nullable=True),
    sa.Column('nom_lic', sa.String(length=255), nullable=True),
    sa.Column('lat', sa.Float(), nullable=True),
    sa.Column('lon', sa.Float(), nullable=True),
    sa.Column('crs', sa.Integer(), nullable=True),
    sa.Column('hash', sa.String(length=255), nullable=True),
    sa.Column('lastupdate', sa.TIMESTAMP(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    comment='НСИ Лицензионные участки'
    )
    op.create_index(op.f('ix_nsi_lu_name_ru'), 'nsi_lu', ['name_ru'], unique=False)
    op.create_index(op.f('ix_nsi_lu_nom_lic'), 'nsi_lu', ['nom_lic'], unique=False)
    op.create_table('nsi_ngo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name_ru', sa.String(length=255), nullable=True),
    sa.Column('lat', sa.Float(), nullable=True),
    sa.Column('lon', sa.Float(), nullable=True),
    sa.Column('crs', sa.Integer(), nullable=True),
    sa.Column('hash', sa.String(length=255), nullable=True),
    sa.Column('lastupdate', sa.TIMESTAMP(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    comment='НСИ Нефтегазоносные области'
    )
    op.create_index(op.f('ix_nsi_ngo_name_ru'), 'nsi_ngo', ['name_ru'], unique=False)
    op.create_table('nsi_ngp',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name_ru', sa.String(length=255), nullable=True),
    sa.Column('lat', sa.Float(), nullable=True),
    sa.Column('lon', sa.Float(), nullable=True),
    sa.Column('crs', sa.Integer(), nullable=True),
    sa.Column('hash', sa.String(length=255), nullable=True),
    sa.Column('lastupdate', sa.TIMESTAMP(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    comment='НСИ Нефтегазоносные провинции'
    )
    op.create_index(op.f('ix_nsi_ngp_name_ru'), 'nsi_ngp', ['name_ru'], unique=False)
    op.create_table('nsi_ngr',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name_ru', sa.String(length=255), nullable=True),
    sa.Column('lat', sa.Float(), nullable=True),
    sa.Column('lon', sa.Float(), nullable=True),
    sa.Column('crs', sa.Integer(), nullable=True),
    sa.Column('hash', sa.String(length=255), nullable=True),
    sa.Column('lastupdate', sa.TIMESTAMP(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    comment='НСИ Нефтегазоносные районы'
    )
    op.create_index(op.f('ix_nsi_ngr_name_ru'), 'nsi_ngr', ['name_ru'], unique=False)
    op.create_table('nsi_well',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name_ru', sa.String(length=255), nullable=True),
    sa.Column('area', sa.String(length=255), nullable=True),
    sa.Column('lat', sa.Float(), nullable=True),
    sa.Column('lon', sa.Float(), nullable=True),
    sa.Column('crs', sa.Integer(), nullable=True),
    sa.Column('hash', sa.String(length=255), nullable=True),
    sa.Column('lastupdate', sa.TIMESTAMP(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    comment='НСИ Скважины'
    )
    op.create_index(op.f('ix_nsi_well_area'), 'nsi_well', ['area'], unique=False)
    op.create_index(op.f('ix_nsi_well_name_ru'), 'nsi_well', ['name_ru'], unique=False)
    op.create_table('report_tgf',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('folder_root', sa.TEXT(), nullable=True),
    sa.Column('folder_link', sa.TEXT(), nullable=True),
    sa.Column('folder_short', sa.TEXT(), nullable=True),
    sa.Column('folder_name', sa.TEXT(), nullable=True),
    sa.Column('rgf', sa.String(length=255), nullable=True),
    sa.Column('tgf_hmao', sa.String(length=255), nullable=True),
    sa.Column('tgf_ynao', sa.String(length=255), nullable=True),
    sa.Column('tgf_kras', sa.String(length=255), nullable=True),
    sa.Column('tgf_ekat', sa.String(length=255), nullable=True),
    sa.Column('tgf_omsk', sa.String(length=255), nullable=True),
    sa.Column('tgf_novo', sa.String(length=255), nullable=True),
    sa.Column('tgf_more', sa.String(length=255), nullable=True),
    sa.Column('tgf_tmn', sa.String(length=255), nullable=True),
    sa.Column('tgf', sa.String(length=255), nullable=True),
    sa.Column('report_name', sa.TEXT(), nullable=True),
    sa.Column('author_name', sa.TEXT(), nullable=True),
    sa.Column('year_str', sa.String(length=255), nullable=True),
    sa.Column('year_int', sa.Integer(), nullable=True),
    sa.Column('territory_name', sa.TEXT(), nullable=True),
    sa.Column('comments', sa.TEXT(), nullable=True),
    sa.Column('lat', sa.Float(), nullable=True),
    sa.Column('lon', sa.Float(), nullable=True),
    sa.Column('report_fts', postgresql.TSVECTOR(), nullable=True),
    sa.Column('lastupdate', sa.TIMESTAMP(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    comment='Отчеты ТГФ'
    )
    op.create_index(op.f('ix_report_tgf_author_name'), 'report_tgf', ['author_name'], unique=False)
    op.create_index(op.f('ix_report_tgf_comments'), 'report_tgf', ['comments'], unique=False)
    op.create_index(op.f('ix_report_tgf_folder_link'), 'report_tgf', ['folder_link'], unique=False)
    op.create_index(op.f('ix_report_tgf_folder_name'), 'report_tgf', ['folder_name'], unique=False)
    op.create_index(op.f('ix_report_tgf_folder_root'), 'report_tgf', ['folder_root'], unique=False)
    op.create_index(op.f('ix_report_tgf_folder_short'), 'report_tgf', ['folder_short'], unique=False)
    op.create_index(op.f('ix_report_tgf_report_name'), 'report_tgf', ['report_name'], unique=False)
    op.create_index(op.f('ix_report_tgf_rgf'), 'report_tgf', ['rgf'], unique=False)
    op.create_index(op.f('ix_report_tgf_territory_name'), 'report_tgf', ['territory_name'], unique=False)
    op.create_index(op.f('ix_report_tgf_tgf'), 'report_tgf', ['tgf'], unique=False)
    op.create_index(op.f('ix_report_tgf_tgf_ekat'), 'report_tgf', ['tgf_ekat'], unique=False)
    op.create_index(op.f('ix_report_tgf_tgf_hmao'), 'report_tgf', ['tgf_hmao'], unique=False)
    op.create_index(op.f('ix_report_tgf_tgf_kras'), 'report_tgf', ['tgf_kras'], unique=False)
    op.create_index(op.f('ix_report_tgf_tgf_more'), 'report_tgf', ['tgf_more'], unique=False)
    op.create_index(op.f('ix_report_tgf_tgf_novo'), 'report_tgf', ['tgf_novo'], unique=False)
    op.create_index(op.f('ix_report_tgf_tgf_omsk'), 'report_tgf', ['tgf_omsk'], unique=False)
    op.create_index(op.f('ix_report_tgf_tgf_tmn'), 'report_tgf', ['tgf_tmn'], unique=False)
    op.create_index(op.f('ix_report_tgf_tgf_ynao'), 'report_tgf', ['tgf_ynao'], unique=False)
    op.create_index(op.f('ix_report_tgf_year_int'), 'report_tgf', ['year_int'], unique=False)
    op.create_index(op.f('ix_report_tgf_year_str'), 'report_tgf', ['year_str'], unique=False)
    op.create_table('history',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('url', sa.TEXT(), nullable=True),
    sa.Column('search_str', sa.TEXT(), nullable=True),
    sa.Column('addr_ip', sa.String(length=255), nullable=True),
    sa.Column('user_name', sa.String(length=255), nullable=True),
    sa.Column('user_login', sa.String(length=255), nullable=True),
    sa.Column('lastupdate', sa.TIMESTAMP(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    comment='История запросов'
    )
    op.create_index(op.f('ix_history_addr_ip'), 'history', ['addr_ip'], unique=False)
    op.create_index(op.f('ix_history_search_str'), 'history', ['search_str'], unique=False)
    op.create_index(op.f('ix_history_url'), 'history', ['url'], unique=False)
    op.create_index(op.f('ix_history_user_login'), 'history', ['user_login'], unique=False)
    op.create_index(op.f('ix_history_user_name'), 'history', ['user_name'], unique=False)
    # op.drop_table('spatial_ref_sys')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    # op.create_table('spatial_ref_sys',
    # sa.Column('srid', sa.INTEGER(), autoincrement=False, nullable=False),
    # sa.Column('auth_name', sa.VARCHAR(length=256), autoincrement=False, nullable=True),
    # sa.Column('auth_srid', sa.INTEGER(), autoincrement=False, nullable=True),
    # sa.Column('srtext', sa.VARCHAR(length=2048), autoincrement=False, nullable=True),
    # sa.Column('proj4text', sa.VARCHAR(length=2048), autoincrement=False, nullable=True),
    # sa.CheckConstraint('srid > 0 AND srid <= 998999', name='spatial_ref_sys_srid_check'),
    # sa.PrimaryKeyConstraint('srid', name='spatial_ref_sys_pkey')
    # )
    op.drop_index(op.f('ix_history_user_name'), table_name='history')
    op.drop_index(op.f('ix_history_user_login'), table_name='history')
    op.drop_index(op.f('ix_history_url'), table_name='history')
    op.drop_index(op.f('ix_history_search_str'), table_name='history')
    op.drop_index(op.f('ix_history_addr_ip'), table_name='history')
    op.drop_table('history')
    op.drop_index(op.f('ix_report_tgf_year_str'), table_name='report_tgf')
    op.drop_index(op.f('ix_report_tgf_year_int'), table_name='report_tgf')
    op.drop_index(op.f('ix_report_tgf_tgf_ynao'), table_name='report_tgf')
    op.drop_index(op.f('ix_report_tgf_tgf_tmn'), table_name='report_tgf')
    op.drop_index(op.f('ix_report_tgf_tgf_omsk'), table_name='report_tgf')
    op.drop_index(op.f('ix_report_tgf_tgf_novo'), table_name='report_tgf')
    op.drop_index(op.f('ix_report_tgf_tgf_more'), table_name='report_tgf')
    op.drop_index(op.f('ix_report_tgf_tgf_kras'), table_name='report_tgf')
    op.drop_index(op.f('ix_report_tgf_tgf_hmao'), table_name='report_tgf')
    op.drop_index(op.f('ix_report_tgf_tgf_ekat'), table_name='report_tgf')
    op.drop_index(op.f('ix_report_tgf_tgf'), table_name='report_tgf')
    op.drop_index(op.f('ix_report_tgf_territory_name'), table_name='report_tgf')
    op.drop_index(op.f('ix_report_tgf_rgf'), table_name='report_tgf')
    op.drop_index(op.f('ix_report_tgf_report_name'), table_name='report_tgf')
    op.drop_index(op.f('ix_report_tgf_folder_short'), table_name='report_tgf')
    op.drop_index(op.f('ix_report_tgf_folder_root'), table_name='report_tgf')
    op.drop_index(op.f('ix_report_tgf_folder_name'), table_name='report_tgf')
    op.drop_index(op.f('ix_report_tgf_folder_link'), table_name='report_tgf')
    op.drop_index(op.f('ix_report_tgf_comments'), table_name='report_tgf')
    op.drop_index(op.f('ix_report_tgf_author_name'), table_name='report_tgf')
    op.drop_table('report_tgf')
    op.drop_index(op.f('ix_nsi_well_name_ru'), table_name='nsi_well')
    op.drop_index(op.f('ix_nsi_well_area'), table_name='nsi_well')
    op.drop_table('nsi_well')
    op.drop_index(op.f('ix_nsi_ngr_name_ru'), table_name='nsi_ngr')
    op.drop_table('nsi_ngr')
    op.drop_index(op.f('ix_nsi_ngp_name_ru'), table_name='nsi_ngp')
    op.drop_table('nsi_ngp')
    op.drop_index(op.f('ix_nsi_ngo_name_ru'), table_name='nsi_ngo')
    op.drop_table('nsi_ngo')
    op.drop_index(op.f('ix_nsi_lu_nom_lic'), table_name='nsi_lu')
    op.drop_index(op.f('ix_nsi_lu_name_ru'), table_name='nsi_lu')
    op.drop_table('nsi_lu')
    op.drop_index(op.f('ix_nsi_field_name_ru'), table_name='nsi_field')
    op.drop_table('nsi_field')
    op.drop_index(op.f('ix_nsi_area_name_ru'), table_name='nsi_area')
    op.drop_table('nsi_area')
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
