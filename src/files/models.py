# geo is based on example https://github.com/jgriffith23/postgis-tutorial/blob/master/model.py
# from sqlalchemy import Table, Column, Integer, String, TIMESTAMP, MetaData, TEXT, BIGINT
from datetime import datetime

from sqlalchemy import (TIMESTAMP, Boolean, Column, ForeignKey, Integer,
                        String, Table, TEXT, BigInteger, Float)
from sqlalchemy.dialects.postgresql import TSVECTOR

from geoalchemy2 import Geometry


from src.database import Base



class FILE_M(Base):
    """A file table, including geospatial data for each file."""

    __tablename__ = "file"

    id: int = Column(Integer, primary_key=True)
    root_folder: str = Column(TEXT)
    file_path: str = Column(TEXT)
    file_folder: str = Column(TEXT)
    file_name: str = Column(String(length=255))
    file_ext: str = Column(String(length=11))
    file_size: int = Column(BigInteger)
    file_ctime: str = Column(TIMESTAMP, default=datetime.now)
    file_mtime: str = Column(TIMESTAMP, default=datetime.now)
    date_c: str = Column(String(length=11))
    date_m: str = Column(String(length=11))
    date_u: str = Column(String(length=11))
    fpath: str = Column(TEXT)
    fpath_md5: str = Column(TEXT)
    field: str = Column(String(length=255))
    areaoil: str = Column(String(length=255))
    lu: str = Column(String(length=255))
    well: str = Column(String(length=255))
    lat: float = Column(Float)
    lon: float = Column(Float)
    geo = Column(Geometry(geometry_type="POINT"))
    report_name: str = Column(TEXT)
    report_text: str = Column(TEXT)
    report_author: str = Column(TEXT)
    report_year: int = Column(Integer)
    report_tgf: str = Column(TEXT)
    is_deleted: bool = Column(Boolean, default=False)
    lastupdate: datetime = Column(TIMESTAMP, default=datetime.now)
    file_path_fts: str = Column(TSVECTOR)
