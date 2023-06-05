from datetime import datetime

from pydantic import BaseModel


class BaseTable(BaseModel):
    class Config:
        orm_mode = True


class FILE_S(BaseTable):
    id: int
    root_folder: str
    file_path: str
    file_folder: str
    file_name: str
    file_ext: str
    file_size: str
    file_ctime: str
    file_mtime: str
    date_c: str
    date_m: str
    date_u: str
    date_m: str
    fpath: str
    fpath_md5: str
    field: str
    areaoil: str
    lu: str
    well: str
    lat: float
    lon: float
    report_name: str
    report_text: str
    report_author: str
    report_year: int
    report_tgf: str
    is_deleted: bool
    lastupdate: datetime


class FILE_SRC_S(BaseTable):
    id: int
    folder_src: str
    lastupdate: datetime


class FILE_SRC_S_CREATE(BaseTable):
    folder_src: str
