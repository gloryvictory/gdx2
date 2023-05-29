from datetime import datetime

from pydantic import BaseModel


class FILES_S(BaseModel):
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


