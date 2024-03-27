"""add org and author

Revision ID: a3f4bdc6a94c
Revises: 1793b015268d
Create Date: 2024-03-27 21:05:26.592166

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a3f4bdc6a94c'
down_revision = '1793b015268d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('r_author',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('author_name', sa.String(length=255), nullable=True),
    sa.Column('lastupdate', sa.TIMESTAMP(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    comment='Авторы'
    )
    op.create_index(op.f('ix_r_author_author_name'), 'r_author', ['author_name'], unique=False)
    op.create_table('r_org',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('org_name', sa.String(length=255), nullable=True),
    sa.Column('lastupdate', sa.TIMESTAMP(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    comment='Организации'
    )
    op.create_index(op.f('ix_r_org_org_name'), 'r_org', ['org_name'], unique=False)
    op.drop_index('ix_list_list_name', table_name='r_list')
    op.create_index(op.f('ix_r_list_list_name'), 'r_list', ['list_name'], unique=False)
    op.drop_index('ix_subrf_subrf_name', table_name='r_subrf')
    op.create_index(op.f('ix_r_subrf_subrf_name'), 'r_subrf', ['subrf_name'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_r_subrf_subrf_name'), table_name='r_subrf')
    op.create_index('ix_subrf_subrf_name', 'r_subrf', ['subrf_name'], unique=False)
    op.drop_index(op.f('ix_r_list_list_name'), table_name='r_list')
    op.create_index('ix_list_list_name', 'r_list', ['list_name'], unique=False)
    op.create_table('spatial_ref_sys',
    sa.Column('srid', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('auth_name', sa.VARCHAR(length=256), autoincrement=False, nullable=True),
    sa.Column('auth_srid', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('srtext', sa.VARCHAR(length=2048), autoincrement=False, nullable=True),
    sa.Column('proj4text', sa.VARCHAR(length=2048), autoincrement=False, nullable=True),
    sa.CheckConstraint('srid > 0 AND srid <= 998999', name='spatial_ref_sys_srid_check'),
    sa.PrimaryKeyConstraint('srid', name='spatial_ref_sys_pkey')
    )
    op.drop_index(op.f('ix_r_org_org_name'), table_name='r_org')
    op.drop_table('r_org')
    op.drop_index(op.f('ix_r_author_author_name'), table_name='r_author')
    op.drop_table('r_author')
    # ### end Alembic commands ###