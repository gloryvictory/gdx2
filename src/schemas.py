from datetime import datetime

from pydantic import BaseModel


class BaseTable(BaseModel):
    class Config:
        from_attributes = True


class S_FILE(BaseTable):
    id: int
    f_root: str
    f_path: str
    f_folder: str
    f_name: str
    f_ext: str
    f_size: int
    f_ctime: str
    f_mtime: str
    f_atime: str
    f_path_md5: str
    f_text: str
    ngp: str
    ngo: str
    ngr: str
    field: str
    areaoil: str
    lu: str
    lu_num: str
    well: str
    lat: float
    lon: float
    report_id: str
    report_name: str
    report_text: str
    report_author: str
    report_year: int
    report_tgf: str
    dog_zakaz: str
    dog_name: str
    dog_num: str
    dog_date: str
    dog_isp: str
    dog_rep: str
    dog_prikaz: str
    is_deleted: bool
    lastupdate: datetime
    file_path_fts: str


# class S_FILE_SRC(BaseTable):
#     id: int
#     folder_src: str
#     lastupdate: datetime
#
#
# class S_FILE_SRC_S_CREATE(BaseModel):
#     folder_src: str


class S_EXT(BaseTable):
    id: int
    ext: str
    category: str
    description: str
    product: str
    is_project: str
    lastupdate: datetime


class S_BaseModel_NSI(BaseTable):
    id: int
    name_ru: str
    lat: float
    lon: float
    crs: int
    hash: str
    lastupdate: datetime


class S_NSI_FIELD(S_BaseModel_NSI):
    pass


class S_NSI_LU(S_BaseModel_NSI):
    nom_lic: str


class S_NSI_NGO(S_BaseModel_NSI):
    pass


class S_NSI_NGP(S_BaseModel_NSI):
    pass


class S_NSI_NGR(S_BaseModel_NSI):
    pass


class S_NSI_WELL(S_BaseModel_NSI):
    area: str


class S_NSI_AREA(S_BaseModel_NSI):
    pass


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
    lastupdate: datetime


class S_HISTORY(BaseTable):
    id: int
    url: str
    search_str: str
    addr_ip: str
    user_name: str
    user_login: str
    lastupdate: datetime


class S_HISTORY_TASK(BaseTable):
    id: int
    task_id: str
    task_type: str
    task_name: str
    time_start: datetime
    time_end: datetime
    time_duration: datetime
    lastupdate: datetime


class S_R_AUTHOR(BaseTable):
    id: int
    name_ru: str
    lastupdate: datetime

class S_R_LIST(BaseTable):
    id: int
    name_ru: str
    lastupdate: datetime

class S_R_SUBRF(BaseTable):
    id: int
    name_ru: str
    lastupdate: datetime


class S_R_ORG(BaseTable):
    id: int
    name_ru: str
    lastupdate: datetime


class S_R_AREA(BaseTable):
    id: int
    name_ru: str
    lastupdate: datetime


class S_R_FIELD(BaseTable):
    id: int
    name_ru: str
    lastupdate: datetime


class S_R_LU(BaseTable):
    id: int
    name_ru: str
    lastupdate: datetime


class S_R_PI(BaseTable):
    id: int
    name_ru: str
    lastupdate: datetime


class S_R_VID_RAB(BaseTable):
    id: int
    name_ru: str
    lastupdate: datetime

class S_R_MESSAGE(BaseTable):
    id: int
    fio:str
    email:str
    name_ru: str
    is_done:bool
    lastupdate: datetime
class S_R_MESSAGE_POST(BaseTable):
    fio:str
    email:str
    name_ru: str


class S_FIELD(BaseTable):
    id: int
    year: int
    tip: str
    areaoil: float
    nom: int
    oil: str
    gas: str
    condensat: str
    name_ru: str
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
