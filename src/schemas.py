from pydantic.main import BaseModel


class BaseModel_NSI(BaseModel):
    id: int
    name_ru: str
    lat: float
    lon: float
    # crs: int
    # hash: str

