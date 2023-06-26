# geo is based on example https://github.com/jgriffith23/postgis-tutorial/blob/master/model.py
# https://github.com/alvassin/alembic-quickstart/blob/master/staff/schema.py
# https://www.learndatasci.com/tutorials/using-databases-python-postgres-sqlalchemy-and-alembic/
# from sqlalchemy import Table, Column, Integer, String, TIMESTAMP, MetaData, TEXT, BIGINT
from datetime import datetime

from sqlalchemy import (TIMESTAMP, Boolean, Column, Integer,
                        String, TEXT, BigInteger, Float)
from sqlalchemy.dialects.postgresql import TSVECTOR
from src.database import Base


# import geoalchemy2


class FILE_M(Base):
    """A file table, including geospatial data for each file."""

    __tablename__ = "file"

    id: int = Column(Integer, primary_key=True)
    f_root: str = Column(TEXT, index=True, )
    f_path: str = Column(TEXT, index=True, )
    f_folder: str = Column(TEXT, index=True, )
    f_name: str = Column(String(length=255), index=True, )
    f_ext: str = Column(String(length=255), index=True, )
    f_size: int = Column(BigInteger)
    f_ctime: str = Column(TIMESTAMP, default=datetime.now)
    f_mtime: str = Column(TIMESTAMP, default=datetime.now)
    f_atime: str = Column(TIMESTAMP, default=datetime.now)
    f_path_md5: str = Column(TEXT, index=True)
    f_text: str = Column(TEXT)
    ngp: str = Column(String(length=255), index=True, )
    ngo: str = Column(String(length=255), index=True, )
    ngr: str = Column(String(length=255), index=True, )
    field: str = Column(String(length=255), index=True, )
    areaoil: str = Column(String(length=255), index=True, )
    lu: str = Column(String(length=255), index=True, )
    lu_num: str = Column(String(length=255), index=True, )
    well: str = Column(String(length=255), index=True, )
    lat: float = Column(Float)
    lon: float = Column(Float)
    report_id: str = Column(Integer, index=True, )
    report_name: str = Column(TEXT, index=True, )
    report_text: str = Column(TEXT)
    report_author: str = Column(TEXT, index=True, )
    report_year: int = Column(Integer, index=True, )
    report_tgf: str = Column(TEXT)
    dog_zakaz: str = Column(TEXT, index=True, )  # Заказчик
    dog_name: str = Column(TEXT, index=True, )  # Название договора
    dog_num: str = Column(TEXT, index=True, )  # Номер договора
    dog_date: str = Column(TIMESTAMP, index=True, )  # Дата договора
    dog_isp: str = Column(TEXT, index=True, )  # Ответственный исполнитель
    dog_rep: str = Column(TEXT, index=True, )  # Название отчета
    dog_prikaz: str = Column(TEXT, index=True, )  # Название приказа
    is_deleted: bool = Column(Boolean, default=False)
    lastupdate: datetime = Column(TIMESTAMP, default=datetime.now)
    file_path_fts: str = Column(TSVECTOR)
    # geom = Column(geoalchemy2.types.Geometry(geometry_type='POINT', srid=4326))
    # date_c: str = Column(String(length=11))
    # date_m: str = Column(String(length=11))
    # date_u: str = Column(String(length=11))
    # fpath: str = Column(TEXT)


# the_geom = Column(Geometry(...), index=True)


class FILE_SRC_M(Base):
    """A source table"""

    __tablename__ = "file_src"

    id: int = Column(Integer, primary_key=True)
    folder_src: str = Column(TEXT, index=True, unique=True)
    lastupdate: datetime = Column(TIMESTAMP, default=datetime.now)


class EXT_M(Base):
    """A source table"""

    __tablename__ = "ext"

    id: int = Column(Integer, primary_key=True)
    ext: str = Column(TEXT, index=True, unique=True)
    category: str = Column(TEXT, index=True, unique=True)
    description: str = Column(TEXT, index=True, unique=True)
    product: str = Column(TEXT, index=True, unique=True)
    is_project: str = Column(TEXT, index=True, unique=True)
    lastupdate: datetime = Column(TIMESTAMP, default=datetime.now)

