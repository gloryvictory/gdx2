import uuid
from datetime import datetime

from pydantic import BaseModel


class BaseTable(BaseModel):
    guid:  uuid.UUID
    name_ru: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


# class BaseTableData(BaseModel):
#     class Config:
#         from_attributes = True


class S_REPORT_TGF(BaseTable):
    id: int
    folder_root: str
    folder_link: str
    folder_short: str
    folder_name: str
    rgf: str
    tgf_hmao: str
    tgf_ynao: str
    tgf_kras: str
    tgf_ekat: str
    tgf_omsk: str
    tgf_novo: str
    tgf_tomsk: str
    tgf_more: str
    tgf_tmn: str
    tgf_kurgan: str
    tgf: str
    report_name: str
    author_name: str
    year_str: str
    year_int: int
    territory_name: str
    subrf_name: str
    list_name: str
    part_name: str
    areaoil: str
    field: str
    lu: str
    pi_name: str
    fin_name: str
    org_name: str
    zsniigg_report: str
    inf_report: str
    vid_rab: str
    comments: str
    lat: float
    lon: float
    is_alive: bool
    report_fts: str


class S_HISTORY(BaseTable):
    id: int
    url: str
    search_str: str
    addr_ip: str
    user_name: str
    user_login: str


class S_HISTORY_TASK(BaseTable):
    task_id: str
    task_type: str
    task_name: str
    time_start: datetime
    time_end: datetime
    time_duration: datetime


class S_R_AUTHOR(BaseTable):
    pass

class S_R_LIST(BaseTable):
    pass

class S_R_SUBRF(BaseTable):
    pass


class S_R_ORG(BaseTable):
    pass


class S_R_AREA(BaseTable):
    pass


class S_R_FIELD(BaseTable):
    pass


class S_R_LU(BaseTable):
    pass


class S_R_PI(BaseTable):
    pass


class S_R_VID_RAB(BaseTable):
    pass


class S_R_MESSAGE(BaseTable):
    fio:str
    email:str
    is_done:bool


class S_R_MESSAGE_POST(BaseTable):
    fio:str
    email:str


class S_FIELD(BaseTable):
    id: int
    year: int
    tip: str
    areaoil: float
    nom: int
    oil: str
    gas: str
    condensat: str
    oblast: str
    stadia: str
    note: str
    istochnik: str
    ftype: str


class S_LU(BaseTable):
    id: int
    areaoil: float
    area_lic: str
    year: int
    nom_zsngp: int
    nom_list: str
    nom: int
    data_start: str
    data_end: str
    vid: str
    ftype: str
    name_rus: str
    anumber: str
    sostiyanie: str
    priznak: str
    nom_lic: str
    head_nedro: str
    oblast: str
    zngp: str
    nedropolz: str
    nedropol: str
    nom_urfo: int
    authority: str


class S_STA(BaseTable):
    id: int
    web_uk_id: str
    vid_iz: str
    tgf: str
    n_uk_tgf: str
    n_uk_rosg: str
    name_otch: str
    name_otch1: str
    avts: str
    god_nach: str
    god_end: str
    org_isp: str
    in_n_tgf: str
    in_n_rosg: str
    nom_1000: str
    method: str
    scale: str


class S_STL(BaseTable):
    id: int
    web_uk_id: str
    vid_iz: str
    tgf: str
    n_uk_tgf: str
    n_uk_rosg: str
    name_otch: str
    name_otch1: str
    avts: str
    god_nach: str
    god_end: str
    org_isp: str
    in_n_tgf: str
    in_n_rosg: str
    nom_1000: str
    method: str
    scale: str


class S_STP(BaseTable):
    id: int
    web_uk_id: str
    vid_iz: str
    tgf: str
    n_uk_tgf: str
    n_uk_rosg: str
    name_otch: str
    name_otch1: str
    avts: str
    god_nach: str
    god_end: str
    org_isp: str
    in_n_tgf: str
    in_n_rosg: str
    nom_1000: str
    method: str
    scale: str
