# geo is based on example https://github.com/jgriffith23/postgis-tutorial/blob/master/model.py
# https://github.com/alvassin/alembic-quickstart/blob/master/staff/schema.py
# https://www.learndatasci.com/tutorials/using-databases-python-postgres-sqlalchemy-and-alembic/
# from sqlalchemy import Table, mapped_column, Integer, String, TIMESTAMP, MetaData, TEXT, BIGINT
from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import (TIMESTAMP, Boolean, Integer, String, TEXT, BigInteger, Float)
from sqlalchemy.dialects.postgresql import TSVECTOR

from src.db.db import Base
from src.schemas import S_FILE, S_EXT, S_NSI_FIELD, S_NSI_LU, S_NSI_NGO, S_NSI_NGP, S_NSI_NGR, S_NSI_WELL, \
    S_NSI_AREA, S_REPORT_TGF, S_AUTHOR, S_HISTORY, S_HISTORY_TASK, S_LIST, S_SUBRF


# import geoalchemy2


class M_FILE(Base):
    """A file table, including geospatial data for each file."""

    __tablename__ = "file"
    __table_args__ = {'comment': 'Файлы'}

    id: Mapped[int] = mapped_column(primary_key=True)
    f_root: Mapped[str] = mapped_column(TEXT, index=True, nullable=True)
    f_path: Mapped[str] = mapped_column(TEXT, index=True, nullable=True)
    f_folder: Mapped[str] = mapped_column(TEXT, index=True, nullable=True)
    f_name: Mapped[str] = mapped_column(String(length=255), index=True, nullable=True)
    f_ext: Mapped[str] = mapped_column(String(length=255), index=True, nullable=True)
    f_size: Mapped[int] = mapped_column(BigInteger, nullable=True)
    f_ctime: Mapped[str] = mapped_column(TIMESTAMP, default=datetime.now, nullable=True)
    f_mtime: Mapped[str] = mapped_column(TIMESTAMP, default=datetime.now, nullable=True)
    f_atime: Mapped[str] = mapped_column(TIMESTAMP, default=datetime.now, nullable=True)
    f_path_md5: Mapped[str] = mapped_column(TEXT, index=True, nullable=True)
    f_text: Mapped[str] = mapped_column(TEXT, nullable=True)
    ngp: Mapped[str] = mapped_column(String(length=255), index=True, nullable=True)
    ngo: Mapped[str] = mapped_column(String(length=255), index=True, nullable=True)
    ngr: Mapped[str] = mapped_column(String(length=255), index=True, nullable=True)
    field: Mapped[str] = mapped_column(String(length=255), index=True, nullable=True)
    areaoil: Mapped[str] = mapped_column(String(length=255), index=True, nullable=True)
    lu: Mapped[str] = mapped_column(String(length=255), index=True, nullable=True)
    lu_num: Mapped[str] = mapped_column(String(length=255), index=True, nullable=True)
    well: Mapped[str] = mapped_column(String(length=255), index=True, nullable=True)
    lat: Mapped[float] = mapped_column(Float, nullable=True)
    lon: Mapped[float] = mapped_column(Float, nullable=True)
    report_id: Mapped[str] = mapped_column(Integer, index=True, nullable=True)
    report_name: Mapped[str] = mapped_column(TEXT, index=True, nullable=True)
    report_text: Mapped[str] = mapped_column(TEXT, nullable=True)
    report_author: Mapped[str] = mapped_column(TEXT, index=True, nullable=True)
    report_year: Mapped[int] = mapped_column(Integer, index=True, nullable=True)
    report_tgf: Mapped[str] = mapped_column(TEXT, nullable=True)
    dog_zakaz: Mapped[str] = mapped_column(TEXT, index=True, nullable=True)  # Заказчик
    dog_name: Mapped[str] = mapped_column(TEXT, index=True, nullable=True)  # Название договора
    dog_num: Mapped[str] = mapped_column(TEXT, index=True, nullable=True)  # Номер договора
    dog_date: Mapped[str] = mapped_column(TIMESTAMP, index=True, nullable=True)  # Дата договора
    dog_isp: Mapped[str] = mapped_column(TEXT, index=True, nullable=True)  # Ответственный исполнитель
    dog_rep: Mapped[str] = mapped_column(TEXT, index=True, nullable=True)  # Название отчета
    dog_prikaz: Mapped[str] = mapped_column(TEXT, index=True, nullable=True)  # Название приказа
    is_deleted: Mapped[bool] = mapped_column(Boolean, default=False, nullable=True)
    lastupdate: Mapped[datetime] = mapped_column(TIMESTAMP, default=datetime.now, nullable=True)
    file_path_fts: Mapped[str] = mapped_column(TSVECTOR, nullable=True)

    # geom = mapped_column(geoalchemy2.types.Geometry(geometry_type='POINT', srid=4326))
    # date_c: str = mapped_column(String(length=11))
    # date_m: str = mapped_column(String(length=11))
    # date_u: str = mapped_column(String(length=11))
    # fpath: str = mapped_column(TEXT)
    # the_geom = mapped_column(Geometry(...), index=True)
    def to_read_model(self) -> S_FILE:
        return S_FILE(
            id=self.id,
            f_root=self.f_root,
            f_path=self.f_path,
            f_folder=self.f_folder,
            f_name=self.f_name,
            f_ext=self.f_ext,
            f_size=self.f_size,
            f_ctime=self.f_ctime,
            f_mtime=self.f_mtime,
            f_atime=self.f_atime,
            f_path_md5=self.f_path_md5,
            f_text=self.f_text,
            ngp=self.ngp,
            ngo=self.ngo,
            ngr=self.ngr,
            field=self.field,
            areaoil=self.areaoil,
            lu=self.lu,
            lu_num=self.lu_num,
            well=self.well,
            lat=self.lat,
            lon=self.lon,
            report_id=self.report_id,
            report_name=self.report_name,
            report_text=self.report_text,
            report_author=self.report_author,
            report_year=self.report_year,
            report_tgf=self.report_tgf,
            dog_zakaz=self.dog_zakaz,
            dog_name=self.dog_name,
            dog_num=self.dog_num,
            dog_date=self.dog_date,
            dog_isp=self.dog_isp,
            dog_rep=self.dog_rep,
            dog_prikaz=self.dog_prikaz,
            is_deleted=self.is_deleted,
            lastupdate=self.lastupdate,
            file_path_fts=self.file_path_fts,
        )


# class M_FILE_SRC(Base):
#     """A source table"""
#
#     __tablename__ = "file_src"
#
#     id: Mapped[int] = mapped_column(Integer, primary_key=True)
#     folder_src: Mapped[str] = mapped_column(TEXT, index=True, unique=True)
#     lastupdate: Mapped[datetime] = mapped_column(TIMESTAMP, default=datetime.now)
#
#     def to_read_model(self) -> S_FILE_SRC:
#         return S_FILE_SRC(
#             id=self.id,
#             folder_src=self.folder_src,
#             lastupdate=self.lastupdate,
#         )


class M_EXT(Base):
    """A source table"""

    __tablename__ = "ext"
    __table_args__ = {'comment': 'Расширения'}

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    ext: Mapped[str] = mapped_column(TEXT, index=True, nullable=True)
    category: Mapped[str] = mapped_column(TEXT, index=True, nullable=True)
    description: Mapped[str] = mapped_column(TEXT, index=True, nullable=True)
    product: Mapped[str] = mapped_column(TEXT, index=True, nullable=True)
    is_project: Mapped[str] = mapped_column(TEXT, index=True, nullable=True)
    lastupdate: Mapped[datetime] = mapped_column(TIMESTAMP, default=datetime.now, nullable=True)

    def to_read_model(self) -> S_EXT:
        return S_EXT(
            id=self.id,
            ext=self.ext,
            category=self.category,
            description=self.description,
            product=self.product,
            is_project=self.is_project,
            lastupdate=self.lastupdate,
        )


class M_NSI_FIELD(Base):
    """A source table"""
    __tablename__ = "nsi_field"
    __table_args__ = {'comment': 'НСИ Месторождения'}

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name_ru: Mapped[str] = mapped_column(String(length=255), index=True, nullable=True)
    lat: Mapped[float] = mapped_column(Float, nullable=True)  # ormar.Float(precision=21, scale=18)
    lon: Mapped[float] = mapped_column(Float, nullable=True)  # ormar.Float(precision=21, scale=18)
    crs: Mapped[int] = mapped_column(Integer, nullable=True)
    hash: Mapped[str] = mapped_column(String(length=255), nullable=True)
    lastupdate: Mapped[datetime] = mapped_column(TIMESTAMP, default=datetime.now, nullable=True)

    def to_read_model(self) -> S_NSI_FIELD:
        return S_NSI_FIELD(
            id=self.id,
            name_ru=self.name_ru,
            lat=self.lat,
            lon=self.lon,
            crs=self.crs,
            hash=self.hash,
            lastupdate=self.lastupdate,
        )


class M_NSI_LU(Base):
    """A source table"""
    __tablename__ = "nsi_lu"
    __table_args__ = {'comment': 'НСИ Лицензионные участки'}

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name_ru: Mapped[str] = mapped_column(String(length=255), index=True, nullable=True)
    nom_lic: Mapped[str] = mapped_column(String(length=255), index=True, nullable=True)
    lat: Mapped[float] = mapped_column(Float, nullable=True)  # ormar.Float(precision=21, scale=18)
    lon: Mapped[float] = mapped_column(Float, nullable=True)  # ormar.Float(precision=21, scale=18)
    crs: Mapped[int] = mapped_column(Integer, nullable=True)
    hash: Mapped[str] = mapped_column(String(length=255), nullable=True)
    lastupdate: Mapped[datetime] = mapped_column(TIMESTAMP, default=datetime.now, nullable=True)

    def to_read_model(self) -> S_NSI_LU:
        return S_NSI_LU(
            id=self.id,
            name_ru=self.name_ru,
            nom_lic=self.nom_lic,
            lat=self.lat,
            lon=self.lon,
            crs=self.crs,
            hash=self.hash,
            lastupdate=self.lastupdate,
        )


class M_NSI_NGO(Base):
    """A source table"""
    __tablename__ = "nsi_ngo"
    __table_args__ = {'comment': 'НСИ Нефтегазоносные области'}

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name_ru: Mapped[str] = mapped_column(String(length=255), index=True, nullable=True)
    lat: Mapped[float] = mapped_column(Float, nullable=True)  # ormar.Float(precision=21, scale=18)
    lon: Mapped[float] = mapped_column(Float, nullable=True)  # ormar.Float(precision=21, scale=18)
    crs: Mapped[int] = mapped_column(Integer, nullable=True)
    hash: Mapped[str] = mapped_column(String(length=255), nullable=True)
    lastupdate: Mapped[datetime] = mapped_column(TIMESTAMP, default=datetime.now, nullable=True)

    def to_read_model(self) -> S_NSI_NGO:
        return S_NSI_NGO(
            id=self.id,
            name_ru=self.name_ru,
            lat=self.lat,
            lon=self.lon,
            crs=self.crs,
            hash=self.hash,
            lastupdate=self.lastupdate,
        )


class M_NSI_NGP(Base):
    """A source table"""
    __tablename__ = "nsi_ngp"
    __table_args__ = {'comment': 'НСИ Нефтегазоносные провинции'}

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name_ru: Mapped[str] = mapped_column(String(length=255), index=True, nullable=True)
    lat: Mapped[float] = mapped_column(Float, nullable=True)  # ormar.Float(precision=21, scale=18)
    lon: Mapped[float] = mapped_column(Float, nullable=True)  # ormar.Float(precision=21, scale=18)
    crs: Mapped[int] = mapped_column(Integer, nullable=True)
    hash: Mapped[str] = mapped_column(String(length=255), nullable=True)
    lastupdate: Mapped[datetime] = mapped_column(TIMESTAMP, default=datetime.now, nullable=True)

    def to_read_model(self) -> S_NSI_NGP:
        return S_NSI_NGP(
            id=self.id,
            name_ru=self.name_ru,
            lat=self.lat,
            lon=self.lon,
            crs=self.crs,
            hash=self.hash,
            lastupdate=self.lastupdate,
        )


class M_NSI_NGR(Base):
    """A source table"""
    __tablename__ = "nsi_ngr"
    __table_args__ = {'comment': 'НСИ Нефтегазоносные районы'}

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name_ru: Mapped[str] = mapped_column(String(length=255), index=True, nullable=True)
    lat: Mapped[float] = mapped_column(Float, nullable=True)  # ormar.Float(precision=21, scale=18)
    lon: Mapped[float] = mapped_column(Float, nullable=True)  # ormar.Float(precision=21, scale=18)
    crs: Mapped[int] = mapped_column(Integer, nullable=True)
    hash: Mapped[str] = mapped_column(String(length=255), nullable=True)
    lastupdate: Mapped[datetime] = mapped_column(TIMESTAMP, default=datetime.now, nullable=True)

    def to_read_model(self) -> S_NSI_NGR:
        return S_NSI_NGR(
            id=self.id,
            name_ru=self.name_ru,
            lat=self.lat,
            lon=self.lon,
            crs=self.crs,
            hash=self.hash,
            lastupdate=self.lastupdate,
        )


class M_NSI_WELL(Base):
    """A source table"""
    __tablename__ = "nsi_well"
    __table_args__ = {'comment': 'НСИ Скважины'}

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name_ru: Mapped[str] = mapped_column(String(length=255), index=True, nullable=True)
    area: Mapped[str] = mapped_column(String(length=255), index=True, nullable=True)
    lat: Mapped[float] = mapped_column(Float, nullable=True)  # ormar.Float(precision=21, scale=18)
    lon: Mapped[float] = mapped_column(Float, nullable=True)  # ormar.Float(precision=21, scale=18)
    crs: Mapped[int] = mapped_column(Integer, nullable=True)
    hash: Mapped[str] = mapped_column(String(length=255), nullable=True)
    lastupdate: Mapped[datetime] = mapped_column(TIMESTAMP, default=datetime.now, nullable=True)

    def to_read_model(self) -> S_NSI_WELL:
        return S_NSI_WELL(
            id=self.id,
            name_ru=self.name_ru,
            area=self.area,
            lat=self.lat,
            lon=self.lon,
            crs=self.crs,
            hash=self.hash,
            lastupdate=self.lastupdate,
        )


class M_NSI_AREA(Base):
    """A source table"""
    __tablename__ = "nsi_area"
    __table_args__ = {'comment': 'НСИ Площади'}

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name_ru: Mapped[str] = mapped_column(String(length=255), index=True, nullable=True)
    lat: Mapped[float] = mapped_column(Float, nullable=True)  # ormar.Float(precision=21, scale=18)
    lon: Mapped[float] = mapped_column(Float, nullable=True)  # ormar.Float(precision=21, scale=18)
    crs: Mapped[int] = mapped_column(Integer, nullable=True)
    hash: Mapped[str] = mapped_column(String(length=255), nullable=True)
    lastupdate: Mapped[datetime] = mapped_column(TIMESTAMP, default=datetime.now, nullable=True)

    def to_read_model(self) -> S_NSI_AREA:
        return S_NSI_AREA(
            id=self.id,
            name_ru=self.name_ru,
            lat=self.lat,
            lon=self.lon,
            crs=self.crs,
            hash=self.hash,
            lastupdate=self.lastupdate,
        )


class M_REPORT_TGF(Base):
    """A source table"""
    __tablename__ = "report_tgf"
    __table_args__ = {'comment': 'Отчеты ТГФ'}

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    folder_root: Mapped[str] = mapped_column(TEXT, index=True, nullable=True)
    folder_link: Mapped[str] = mapped_column(TEXT, index=True, nullable=True)
    folder_short: Mapped[str] = mapped_column(TEXT, index=True, nullable=True)
    folder_name: Mapped[str] = mapped_column(TEXT, index=True, nullable=True)
    rgf: Mapped[str] = mapped_column(String(length=255), index=True, nullable=True)
    tgf_hmao: Mapped[str] = mapped_column(String(length=255), index=True, nullable=True)
    tgf_ynao: Mapped[str] = mapped_column(String(length=255), index=True, nullable=True)
    tgf_kras: Mapped[str] = mapped_column(String(length=255), index=True, nullable=True)
    tgf_ekat: Mapped[str] = mapped_column(String(length=255), index=True, nullable=True)
    tgf_omsk: Mapped[str] = mapped_column(String(length=255), index=True, nullable=True)
    tgf_novo: Mapped[str] = mapped_column(String(length=255), index=True, nullable=True)
    tgf_tomsk: Mapped[str] = mapped_column(String(length=255), index=True, nullable=True)
    tgf_more: Mapped[str] = mapped_column(String(length=255), index=True, nullable=True)
    tgf_tmn: Mapped[str] = mapped_column(String(length=255), index=True, nullable=True)
    tgf_kurgan: Mapped[str] = mapped_column(String(length=255), index=True, nullable=True)
    tgf: Mapped[str] = mapped_column(String(length=255), index=True, nullable=True)
    report_name: Mapped[str] = mapped_column(TEXT, index=True, nullable=True)
    author_name: Mapped[str] = mapped_column(TEXT, index=True, nullable=True)
    year_str: Mapped[str] = mapped_column(String(length=255), index=True, nullable=True)
    year_int: Mapped[int] = mapped_column(Integer, index=True, nullable=True)
    territory_name: Mapped[str] = mapped_column(TEXT, index=True, nullable=True)

    subrf_name: Mapped[str] = mapped_column(TEXT, index=True, nullable=True)
    list_name: Mapped[str] = mapped_column(TEXT, index=True, nullable=True)
    part_name: Mapped[str] = mapped_column(TEXT, index=True, nullable=True)
    areaoil: Mapped[str] = mapped_column(TEXT, index=True, nullable=True)
    field: Mapped[str] = mapped_column(TEXT, index=True, nullable=True)
    lu: Mapped[str] = mapped_column(TEXT, index=True, nullable=True)
    pi_name: Mapped[str] = mapped_column(TEXT, index=True, nullable=True)
    fin_name: Mapped[str] = mapped_column(TEXT, index=True, nullable=True)
    org_name: Mapped[str] = mapped_column(TEXT, index=True, nullable=True)
    zsniigg_report: Mapped[str] = mapped_column(String(length=255), index=True, nullable=True)
    inf_report: Mapped[str] = mapped_column(String(length=255), index=True, nullable=True)
    vid_rab: Mapped[str] = mapped_column(TEXT, index=True, nullable=True)

    comments: Mapped[str] = mapped_column(TEXT, index=True, nullable=True)
    lat: Mapped[float] = mapped_column(Float, nullable=True)  # ormar.Float(precision=21, scale=18)
    lon: Mapped[float] = mapped_column(Float, nullable=True)  # ormar.Float(precision=21, scale=18)
    is_alive: Mapped[bool] = mapped_column(Boolean, nullable=True)  #
    report_fts: Mapped[str] = mapped_column(TSVECTOR, nullable=True)
    lastupdate: Mapped[datetime] = mapped_column(TIMESTAMP, default=datetime.now, nullable=True)

    def to_read_model(self) -> S_REPORT_TGF:
        return S_REPORT_TGF(
            id=self.id,
            folder_root=self.folder_root,
            folder_link=self.folder_link,
            folder_short=self.folder_short,
            folder_name=self.folder_name,
            rgf=self.rgf,
            tgf_hmao=self.tgf_hmao,
            tgf_ynao=self.tgf_ynao,
            tgf_kras=self.tgf_kras,
            tgf_ekat=self.tgf_ekat,
            tgf_omsk=self.tgf_omsk,
            tgf_novo=self.tgf_novo,
            tgf_tomsk=self.tgf_tomsk,
            tgf_more=self.tgf_more,
            tgf_tmn=self.tgf_tmn,
            tgf_kurgan=self.tgf_kurgan,
            tgf=self.tgf,
            report_name=self.report_name,
            author_name=self.author_name,
            year_str=self.year_str,
            year_int=self.year_int,
            territory_name=self.territory_name,
            subrf_name=self.subrf_name,
            list_name=self.list_name,
            part_name=self.part_name,
            areaoil=self.areaoil,
            field=self.field,
            lu=self.lu,
            pi_name=self.pi_name,
            fin_name=self.fin_name,
            org_name=self.org_name,
            zsniigg_report=self.zsniigg_report,
            inf_report=self.inf_report,
            vid_rab=self.vid_rab,
            comments=self.comments,
            lat=self.lat,
            lon=self.lon,
            is_alive=self.is_alive,
            report_fts=self.report_fts,
            lastupdate=self.lastupdate,
        )


class M_AUTHOR(Base):
    """A source table"""

    __tablename__ = "author"
    __table_args__ = {'comment': 'Авторы'}

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    author_name: Mapped[str] = mapped_column(String(length=255), index=True, nullable=True)
    lastupdate: Mapped[datetime] = mapped_column(TIMESTAMP, default=datetime.now, nullable=True)

    def to_read_model(self) -> S_AUTHOR:
        return S_AUTHOR(
            id=self.id,
            author_name=self.author_name,
            lastupdate=self.lastupdate,
        )


class M_LIST(Base):
    """A source table"""

    __tablename__ = "r_list"
    __table_args__ = {'comment': 'Листы карты'}

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    list_name: Mapped[str] = mapped_column(String(length=255), index=True, nullable=True)
    lastupdate: Mapped[datetime] = mapped_column(TIMESTAMP, default=datetime.now, nullable=True)

    def to_read_model(self) -> S_LIST:
        return S_LIST(
            id=self.id,
            list_name=self.list_name,
            lastupdate=self.lastupdate,
        )

class M_SUBRF(Base):
    """A source table"""

    __tablename__ = "r_subrf"
    __table_args__ = {'comment': 'Субъекты РФ'}

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    subrf_name: Mapped[str] = mapped_column(String(length=255), index=True, nullable=True)
    lastupdate: Mapped[datetime] = mapped_column(TIMESTAMP, default=datetime.now, nullable=True)

    def to_read_model(self) -> S_SUBRF:
        return S_SUBRF(
            id=self.id,
            subrf_name=self.subrf_name,
            lastupdate=self.lastupdate,
        )


class M_HISTORY(Base):
    """A source table"""

    __tablename__: str = "history"
    __table_args__ = {'comment': 'История запросов'}

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    url: Mapped[str] = mapped_column(TEXT, index=True, nullable=True)
    search_str: Mapped[str] = mapped_column(TEXT, index=True, nullable=True)
    addr_ip: Mapped[str] = mapped_column(String(length=255), index=True, nullable=True)
    user_name: Mapped[str] = mapped_column(String(length=255), index=True, nullable=True)
    user_login: Mapped[str] = mapped_column(String(length=255), index=True, nullable=True)
    lastupdate: Mapped[datetime] = mapped_column(TIMESTAMP, default=datetime.now)

    def to_read_model(self) -> S_HISTORY:
        return S_HISTORY(
            id=self.id,
            url=self.url,
            search_str=self.search_str,
            addr_ip=self.addr_ip,
            user_name=self.user_name,
            user_login=self.user_login,
            lastupdate=self.lastupdate,
        )


class M_HISTORY_TASK(Base):
    """A HISTORY_TASK table"""

    __tablename__ = "history_task"
    __table_args__ = {'comment': 'История задач'}

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    task_id: Mapped[str] = mapped_column(String(length=40), index=True, nullable=True)
    task_type: Mapped[str] = mapped_column(String(length=255), index=True, nullable=True)
    task_name: Mapped[str] = mapped_column(String(length=255), index=True, nullable=True)
    time_start: Mapped[datetime] = mapped_column(TIMESTAMP, nullable=True)
    time_end: Mapped[datetime] = mapped_column(TIMESTAMP, nullable=True)
    time_duration: Mapped[datetime] = mapped_column(TIMESTAMP, nullable=True)
    lastupdate: Mapped[datetime] = mapped_column(TIMESTAMP, default=datetime.now, nullable=True)

    def to_read_model(self) -> S_HISTORY_TASK:
        return S_HISTORY_TASK(
            id=self.id,
            task_id=self.task_id,
            task_type=self.task_type,
            task_name=self.task_name,
            time_start=self.time_start,
            time_end=self.time_end,
            time_duration=self.time_duration,
            lastupdate=self.lastupdate,
        )