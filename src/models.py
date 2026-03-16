# geo is based on example https://github.com/jgriffith23/postgis-tutorial/blob/master/model.py
# https://github.com/alvassin/alembic-quickstart/blob/master/staff/schema.py
# https://www.learndatasci.com/tutorials/using-databases-python-postgres-sqlalchemy-and-alembic/
# from sqlalchemy import Table, mapped_column, Integer, String, TIMESTAMP, MetaData, TEXT, BIGINT
import uuid
from datetime import datetime
from sqlalchemy import (TIMESTAMP, Boolean, Integer, String, TEXT, BigInteger, Float, func)
from sqlalchemy.dialects.postgresql import TSVECTOR
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

# from src.db.db import Base
from src.schemas import S_REPORT_TGF, S_R_AUTHOR, S_HISTORY, S_HISTORY_TASK, S_R_LIST, S_R_SUBRF, S_R_ORG, S_R_AREA, \
    S_R_FIELD, \
    S_R_LU, S_R_PI, \
    S_R_VID_RAB, S_R_MESSAGE


# import geoalchemy2


class Base(AsyncAttrs, DeclarativeBase):
    __abstract__ = True
    __table_args__ = {'schema': 'gdx2'}  # <-- Добавлено


    guid: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, comment='Глобальный идентификатор')
    name_ru: Mapped[str] = mapped_column(TEXT, index=True, nullable=True, comment='Наименование (рус)')
    created_at: Mapped[datetime] = mapped_column(server_default=func.now(), comment='Дата создания')
    updated_at: Mapped[datetime] = mapped_column(server_default=func.now(), onupdate=func.now(), comment='Дата обновления')

    # @declared_attr.directive
    # def __tablename__(cls) -> str:
    #     return cls.__name__.lower() + 's'


class M_REPORT_TGF(Base):
    """A source table"""
    __tablename__ = "report_tgf"
    __table_args__ = {'comment': 'Отчеты ТГФ'}

    # id: Mapped[int] = mapped_column(Integer, primary_key=True)
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

    # lastupdate: Mapped[datetime] = mapped_column(TIMESTAMP, default=datetime.now, nullable=True)

    def to_read_model(self) -> S_REPORT_TGF:
        return S_REPORT_TGF(
            id=self.id,
            name_ru=self.name_ru,
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
            created_at=self.created_at,
            updated_at=self.updated_at
        )


class M_HISTORY(Base):
    """A source table"""

    __tablename__: str = "history"
    __table_args__ = {'comment': 'История запросов'}

    # id: Mapped[int] = mapped_column(Integer, primary_key=True)
    url: Mapped[str] = mapped_column(TEXT, index=True, nullable=True)
    search_str: Mapped[str] = mapped_column(TEXT, index=True, nullable=True)
    addr_ip: Mapped[str] = mapped_column(String(length=255), index=True, nullable=True)
    user_name: Mapped[str] = mapped_column(String(length=255), index=True, nullable=True)
    user_login: Mapped[str] = mapped_column(String(length=255), index=True, nullable=True)

    # lastupdate: Mapped[datetime] = mapped_column(TIMESTAMP, default=datetime.now)

    def to_read_model(self) -> S_HISTORY:
        return S_HISTORY(
            id=self.id,
            name_ru=self.name_ru,
            url=self.url,
            search_str=self.search_str,
            addr_ip=self.addr_ip,
            user_name=self.user_name,
            user_login=self.user_login,
            created_at=self.created_at,
            updated_at=self.updated_at
        )


class M_HISTORY_TASK(Base):
    """A HISTORY_TASK table"""

    __tablename__ = "history_task"
    __table_args__ = {'comment': 'История задач'}

    # id: Mapped[int] = mapped_column(Integer, primary_key=True)
    task_id: Mapped[str] = mapped_column(String(length=40), index=True, nullable=True)
    task_type: Mapped[str] = mapped_column(String(length=255), index=True, nullable=True)
    task_name: Mapped[str] = mapped_column(String(length=255), index=True, nullable=True)
    time_start: Mapped[datetime] = mapped_column(TIMESTAMP, nullable=True)
    time_end: Mapped[datetime] = mapped_column(TIMESTAMP, nullable=True)
    time_duration: Mapped[datetime] = mapped_column(TIMESTAMP, nullable=True)

    # lastupdate: Mapped[datetime] = mapped_column(TIMESTAMP, default=datetime.now, nullable=True)

    def to_read_model(self) -> S_HISTORY_TASK:
        return S_HISTORY_TASK(
            id=self.id,
            name_ru=self.name_ru,
            task_id=self.task_id,
            task_type=self.task_type,
            task_name=self.task_name,
            time_start=self.time_start,
            time_end=self.time_end,
            time_duration=self.time_duration,
            created_at=self.created_at,
            updated_at=self.updated_at
        )


class M_R_AUTHOR(Base):
    """A source table"""

    __tablename__ = "r_author"
    __table_args__ = {'comment': 'Авторы'}

    # id: Mapped[int] = mapped_column(Integer, primary_key=True)
    # name_ru: Mapped[str] = mapped_column(String(length=255), index=True, nullable=True)
    # lastupdate: Mapped[datetime] = mapped_column(TIMESTAMP, default=datetime.now, nullable=True)

    def to_read_model(self) -> S_R_AUTHOR:
        return S_R_AUTHOR(
            id=self.id,
            name_ru=self.name_ru,
            created_at=self.created_at,
            updated_at=self.updated_at
        )


class M_R_LIST(Base):
    """A source table"""

    __tablename__ = "r_list"
    __table_args__ = {'comment': 'Листы карты'}

    # id: Mapped[int] = mapped_column(Integer, primary_key=True)
    # name_ru: Mapped[str] = mapped_column(String(length=255), index=True, nullable=True)
    # lastupdate: Mapped[datetime] = mapped_column(TIMESTAMP, default=datetime.now, nullable=True)

    def to_read_model(self) -> S_R_LIST:
        return S_R_LIST(
            id=self.id,
            name_ru=self.name_ru,
            created_at=self.created_at,
            updated_at=self.updated_at
        )


class M_R_SUBRF(Base):
    """A source table"""

    __tablename__ = "r_subrf"
    __table_args__ = {'comment': 'Субъекты РФ'}

    # id: Mapped[int] = mapped_column(Integer, primary_key=True)
    # name_ru: Mapped[str] = mapped_column(String(length=255), index=True, nullable=True)
    # lastupdate: Mapped[datetime] = mapped_column(TIMESTAMP, default=datetime.now, nullable=True)

    def to_read_model(self) -> S_R_SUBRF:
        return S_R_SUBRF(
            id=self.id,
            name_ru=self.name_ru,
            created_at=self.created_at,
            updated_at=self.updated_at
        )


class M_R_ORG(Base):
    """A source table"""

    __tablename__ = "r_org"
    __table_args__ = {'comment': 'Организации'}

    # id: Mapped[int] = mapped_column(Integer, primary_key=True)
    # name_ru: Mapped[str] = mapped_column(String(length=255), index=True, nullable=True)
    # lastupdate: Mapped[datetime] = mapped_column(TIMESTAMP, default=datetime.now, nullable=True)

    def to_read_model(self) -> S_R_ORG:
        return S_R_ORG(
            id=self.id,
            name_ru=self.name_ru,
            created_at=self.created_at,
            updated_at=self.updated_at
        )


class M_R_AREA(Base):
    """A source table"""

    __tablename__ = "r_area"
    __table_args__ = {'comment': 'Площади отчетов'}

    # id: Mapped[int] = mapped_column(Integer, primary_key=True)
    # name_ru: Mapped[str] = mapped_column(String(length=255), index=True, nullable=True)
    # lastupdate: Mapped[datetime] = mapped_column(TIMESTAMP, default=datetime.now, nullable=True)

    def to_read_model(self) -> S_R_AREA:
        return S_R_AREA(
            id=self.id,
            name_ru=self.name_ru,
            created_at=self.created_at,
            updated_at=self.updated_at
        )


class M_R_FIELD(Base):
    """A source table"""

    __tablename__ = "r_field"
    __table_args__ = {'comment': 'Месторождения отчетов'}

    # id: Mapped[int] = mapped_column(Integer, primary_key=True)
    # name_ru: Mapped[str] = mapped_column(String(length=255), index=True, nullable=True)
    # lastupdate: Mapped[datetime] = mapped_column(TIMESTAMP, default=datetime.now, nullable=True)

    def to_read_model(self) -> S_R_FIELD:
        return S_R_FIELD(
            id=self.id,
            name_ru=self.name_ru,
            created_at=self.created_at,
            updated_at=self.updated_at
        )


class M_R_LU(Base):
    """A source table"""

    __tablename__ = "r_lu"
    __table_args__ = {'comment': 'ЛУ отчетов'}

    # id: Mapped[int] = mapped_column(Integer, primary_key=True)
    # name_ru: Mapped[str] = mapped_column(String(length=255), index=True, nullable=True)
    # lastupdate: Mapped[datetime] = mapped_column(TIMESTAMP, default=datetime.now, nullable=True)

    def to_read_model(self) -> S_R_LU:
        return S_R_LU(
            id=self.id,
            name_ru=self.name_ru,
            created_at=self.created_at,
            updated_at=self.updated_at
        )


class M_R_PI(Base):
    """A source table"""

    __tablename__ = "r_pi"
    __table_args__ = {'comment': 'Полезные ископаемые отчетов'}

    # id: Mapped[int] = mapped_column(Integer, primary_key=True)
    # name_ru: Mapped[str] = mapped_column(String(length=255), index=True, nullable=True)
    # lastupdate: Mapped[datetime] = mapped_column(TIMESTAMP, default=datetime.now, nullable=True)

    def to_read_model(self) -> S_R_PI:
        return S_R_PI(
            id=self.id,
            name_ru=self.name_ru,
            created_at=self.created_at,
            updated_at=self.updated_at
        )


class M_R_VID_RAB(Base):
    """A source table"""

    __tablename__ = "r_vid_rab"
    __table_args__ = {'comment': 'Вид работ отчетов'}

    # id: Mapped[int] = mapped_column(Integer, primary_key=True)
    # name_ru: Mapped[str] = mapped_column(String(length=255), index=True, nullable=True)
    # lastupdate: Mapped[datetime] = mapped_column(TIMESTAMP, default=datetime.now, nullable=True)

    def to_read_model(self) -> S_R_VID_RAB:
        return S_R_VID_RAB(
            id=self.id,
            name_ru=self.name_ru,
            created_at=self.created_at,
            updated_at=self.updated_at
        )


class M_R_MESSAGE(Base):
    """A source table"""

    __tablename__ = "r_message"
    __table_args__ = {'comment': 'Сообщения обратной связи'}

    # id: Mapped[int] = mapped_column(Integer, primary_key=True)
    fio: Mapped[str] = mapped_column(String(length=255), index=True, nullable=True)
    email: Mapped[str] = mapped_column(String(length=255), index=True, nullable=True)
    # name_ru: Mapped[str] = mapped_column(String(length=255), index=True, nullable=True)
    is_done: Mapped[bool] = mapped_column(Boolean, nullable=True)

    # lastupdate: Mapped[datetime] = mapped_column(TIMESTAMP, default=datetime.now, nullable=True)

    def to_read_model(self) -> S_R_MESSAGE:
        return S_R_MESSAGE(
            fio=self.fio,
            email=self.email,
            is_done=self.is_done,
            id=self.id,
            name_ru=self.name_ru,
            created_at=self.created_at,
            updated_at=self.updated_at
        )



class M_FIELD(Base):
    """Месторождения с геоданными"""
    __tablename__ = 'field'
    __table_args__ = { 'comment': 'Месторождения'   }

    id: Mapped[int] = mapped_column(primary_key=True, comment='Идентификатор (внутренний)')
    year: Mapped[int] = mapped_column(BigInteger, nullable=True, comment='Год открытия')
    tip: Mapped[str] = mapped_column(String(length=10), nullable=True, comment='Тип')
    areaoil: Mapped[float] = mapped_column(Float, nullable=True, comment='Название Площади')
    nom: Mapped[int] = mapped_column(BigInteger, nullable=True, comment='Номер')
    oil: Mapped[str] = mapped_column(String(length=254), nullable=True, comment='Нефть')
    gas: Mapped[str] = mapped_column(String(length=254), nullable=True, comment='Газ')
    condensat: Mapped[str] = mapped_column(String(length=254), nullable=True, comment='Конденсат')
    # name_ru: 'Наименование' - закомментировано, при необходимости раскомментировать
    oblast: Mapped[str] = mapped_column(String(length=254), nullable=True, comment='Область')
    stadia: Mapped[str] = mapped_column(String(length=254), nullable=True, comment='Стадия освоения')
    note: Mapped[str] = mapped_column(String(length=254), nullable=True, comment='Комментарий')
    istochnik: Mapped[str] = mapped_column(String(length=254), nullable=True, comment='Источник')
    ftype: Mapped[str] = mapped_column(String(length=8), nullable=True, comment='Тип2')


class M_LU(Base):
    """Лицензионные участки с геоданными"""
    __tablename__ = 'lu'
    __table_args__ = { 'comment': 'Лицензионные участки'  }

    id: Mapped[int] = mapped_column(primary_key=True)
    areaoil: Mapped[float] = mapped_column(Float, nullable=True, comment='Площадь')
    area_lic: Mapped[str] = mapped_column(String(length=10), nullable=True, comment='Площадь ЛУ')
    year: Mapped[int] = mapped_column(BigInteger, nullable=True, comment='Год')
    nom_zsngp: Mapped[int] = mapped_column(BigInteger, nullable=True, comment='Номер (ЗСНГП)')
    nom_list: Mapped[str] = mapped_column(String(length=12), nullable=True, comment='Номер Листа карты')
    nom: Mapped[int] = mapped_column(BigInteger, nullable=True, comment='Номер')
    data_start: Mapped[str] = mapped_column(TIMESTAMP, nullable=True, comment='Дата начала')
    data_end: Mapped[str] = mapped_column(TIMESTAMP, index=True, nullable=True, comment='Дата конца')
    vid: Mapped[str] = mapped_column(String(length=50), nullable=True, comment='Вид')
    ftype: Mapped[str] = mapped_column(String(length=5), nullable=True, comment='Тип2')
    name_rus: Mapped[str] = mapped_column(String(length=100), nullable=True, comment='Наименование')
    anumber: Mapped[str] = mapped_column(String(length=10), nullable=True, comment='Номер лицензии')
    sostiyanie: Mapped[str] = mapped_column(String(length=50), nullable=True, comment='Состояние')
    priznak: Mapped[str] = mapped_column(String(length=50), nullable=True, comment='Признак')
    nom_lic: Mapped[str] = mapped_column(String(length=50), nullable=True, comment='Номер Лицензии (полный)')
    head_nedro: Mapped[str] = mapped_column(String(length=100), nullable=True, comment='ВИНК')
    oblast: Mapped[str] = mapped_column(String(length=100), nullable=True, comment='Область')
    zngp: Mapped[str] = mapped_column(String(length=10), nullable=True, comment='ЗСНГП')
    nedropolz: Mapped[str] = mapped_column(String(length=150), nullable=True,
                                           comment='Недропользователь (полное наименование)')
    nedropol: Mapped[str] = mapped_column(String(length=100), nullable=True,
                                          comment='Недропользователь (короткое наименование)')
    nom_urfo: Mapped[int] = mapped_column(BigInteger, nullable=True, comment='Номер в УРФО')
    authority: Mapped[str] = mapped_column(String(length=254), nullable=True, comment='Субъект РФ')


class M_STA(Base):
    """Отчеты: полигоны"""
    __tablename__ = 'sta'
    __table_args__ = { 'comment': 'Отчеты (полигоны)' }

    # id: 'Идентификатор (внутренний)' - наследуется из Base
    web_uk_id: Mapped[str] = mapped_column(String(length=18), nullable=True, comment='№')
    vid_iz: Mapped[str] = mapped_column(String(length=26), nullable=True, comment='Вид')
    tgf: Mapped[str] = mapped_column(String(length=31), nullable=True, comment='ТГФ')
    n_uk_tgf: Mapped[str] = mapped_column(String(length=8), nullable=True, comment='№ ТГФ')
    n_uk_rosg: Mapped[str] = mapped_column(String(length=6), nullable=True, comment='№ РГФ')
    name_otch: Mapped[str] = mapped_column(String(length=254), nullable=True, comment='Отчет')
    name_otch1: Mapped[str] = mapped_column(String(length=254), nullable=True, comment='Отчет (дополнительно)')
    avts: Mapped[str] = mapped_column(String(length=254), nullable=True, comment='Автор')
    god_nach: Mapped[str] = mapped_column(String(length=4), nullable=True, comment='Год начала')
    god_end: Mapped[str] = mapped_column(String(length=4), nullable=True, comment='Год окончания')
    org_isp: Mapped[str] = mapped_column(String(length=193), nullable=True, comment='Организация исполнитель')
    in_n_tgf: Mapped[str] = mapped_column(String(length=9), nullable=True, comment='инв. № ТГФ')
    in_n_rosg: Mapped[str] = mapped_column(String(length=10), nullable=True, comment='инв. № РГФ')
    nom_1000: Mapped[str] = mapped_column(String(length=4), nullable=True, comment='Лист')
    method: Mapped[str] = mapped_column(String(length=13), nullable=True, comment='Метод')
    scale: Mapped[str] = mapped_column(String(length=26), nullable=True, comment='Масштаб')


class M_STL(Base):
    """Отчеты: линии"""
    __tablename__ = 'stl'
    __table_args__ = { 'comment': 'Отчеты (линии)'  }

    web_uk_id: Mapped[str] = mapped_column(String(length=18), nullable=True, comment='№')
    vid_iz: Mapped[str] = mapped_column(String(length=26), nullable=True, comment='Вид')
    tgf: Mapped[str] = mapped_column(String(length=31), nullable=True, comment='ТГФ')
    n_uk_tgf: Mapped[str] = mapped_column(String(length=6), nullable=True, comment='№ ТГФ')
    n_uk_rosg: Mapped[str] = mapped_column(String(length=6), nullable=True, comment='№ РГФ')
    name_otch: Mapped[str] = mapped_column(String(length=254), nullable=True, comment='Отчет')
    name_otch1: Mapped[str] = mapped_column(String(length=108), nullable=True, comment='Отчет (дополнительно)')
    avts: Mapped[str] = mapped_column(String(length=179), nullable=True, comment='Автор')
    god_nach: Mapped[str] = mapped_column(String(length=4), nullable=True, comment='Год начала')
    god_end: Mapped[str] = mapped_column(String(length=4), nullable=True, comment='Год окончания')
    org_isp: Mapped[str] = mapped_column(String(length=192), nullable=True, comment='Организация исполнитель')
    in_n_tgf: Mapped[str] = mapped_column(String(length=6), nullable=True, comment='инв. № ТГФ')
    in_n_rosg: Mapped[str] = mapped_column(String(length=6), nullable=True, comment='инв. № РГФ')
    nom_1000: Mapped[str] = mapped_column(String(length=4), nullable=True, comment='Лист')
    method: Mapped[str] = mapped_column(String(length=13), nullable=True, comment='Метод')
    scale: Mapped[str] = mapped_column(String(length=26), nullable=True, comment='Масштаб')


class M_STP(Base):
    """Отчеты: точки"""
    __tablename__ = 'stp'
    __table_args__ = { 'comment': 'Отчеты (точки)'  }

    web_uk_id: Mapped[str] = mapped_column(String(length=18), nullable=True, comment='№')
    vid_iz: Mapped[str] = mapped_column(String(length=26), nullable=True, comment='Вид')
    tgf: Mapped[str] = mapped_column(String(length=31), nullable=True, comment='ТГФ')
    n_uk_tgf: Mapped[str] = mapped_column(String(length=5), nullable=True, comment='№ ТГФ')
    n_uk_rosg: Mapped[str] = mapped_column(String(length=6), nullable=True, comment='№ РГФ')
    name_otch: Mapped[str] = mapped_column(String(length=254), nullable=True, comment='Отчет')
    name_otch1: Mapped[str] = mapped_column(String(length=254), nullable=True, comment='Отчет (дополнительно)')
    avts: Mapped[str] = mapped_column(String(length=161), nullable=True, comment='Автор')
    god_nach: Mapped[str] = mapped_column(String(length=4), nullable=True, comment='Год начала')
    god_end: Mapped[str] = mapped_column(String(length=4), nullable=True, comment='Год окончания')
    org_isp: Mapped[str] = mapped_column(String(length=190), nullable=True, comment='Организация исполнитель')
    in_n_tgf: Mapped[str] = mapped_column(String(length=7), nullable=True, comment='инв. № ТГФ')
    in_n_rosg: Mapped[str] = mapped_column(String(length=6), nullable=True, comment='инв. № РГФ')
    nom_1000: Mapped[str] = mapped_column(String(length=4), nullable=True, comment='Лист')
    method: Mapped[str] = mapped_column(String(length=13), nullable=True, comment='Метод')
    scale: Mapped[str] = mapped_column(String(length=26), nullable=True, comment='Масштаб')
