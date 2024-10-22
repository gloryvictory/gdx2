from dotenv import load_dotenv
import os
from time import strftime  # Load just the strftime Module from Time

load_dotenv()

API_VERSION = "/api/v1"

SERVER_HOST = os.getenv("GDX2_SERVER_HOST", "0.0.0.0")
SERVER_PORT = os.getenv("GDX2_SERVER_PORT", 8001)

DEVENV = os.getenv("DEVENV", "dev")

DB_DSN_ENV = ""
if DEVENV.startswith("dev"):
    DB_DSN_ENV = os.getenv("GDX2_DB_DSN", "postgresql://gdx2:gdx2pwd@localhost:5432/gdx2?sslmode=disable")
    FOLDER_BASE = os.getenv("FOLDER_BASE", "C:\\Glory\\Projects\\Python\\zsniigg\\gdx2\\src")  # C:\\zsniigg\\gdx2\\src
    FOLDER_REPORT = os.getenv("FOLDER_REPORT", "D:\\zsniigg\\")  # \\\\r57-vfs02\\archiv002
else:
    DB_DSN_ENV = os.getenv("GDX2_DB_DSN", "postgresql://gdx2:gdx2pwd@r48-vldb02.zsniigg.local:5432/gdx2?sslmode=disable")
    FOLDER_BASE = os.getenv("FOLDER_BASE", "C:\\zsniigg\\gdx2\\src")  #
    FOLDER_REPORT = os.getenv("FOLDER_REPORT", "\\\\r57-vfs02\\archiv002")  #

DB_SCHEMA = os.getenv("GDX2_SCHEMA", "gdx2map")
DB_DSN = DB_DSN_ENV.replace("postgresql://", "postgresql+asyncpg://")
DB_DSN2 = DB_DSN_ENV.replace("postgresql://", "postgresql+psycopg2://")

REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = os.getenv("REDIS_PORT", "6379")
REDIS_URL = f"redis://{REDIS_HOST}:{REDIS_PORT}"
REDIS_DB = f"{REDIS_URL}/0"
REDIS_BACKEND = REDIS_DB
REDIS_BROKER = REDIS_DB


NUMBER_PROCESS = os.getenv("NUMBER_PROCESS", "1")

DATETIME_CURRENT = str(strftime("%Y-%m-%d-%H-%M-%S"))

FILE_LOG_NAME = 'gdx2'
FILE_LOG = DATETIME_CURRENT + '_' + FILE_LOG_NAME + '.log'
FILE_LOG_FORMAT = '%(asctime)s %(levelname)s %(message)s'
FILE_REPORT_NAME = 'КАТАЛОГ_ОТЧЕТОВ.xlsx'
FILE_REPORT_SRC_NAME_PART = 'volarch'


FOLDER_OUT = 'log'

FOLDER_UPLOAD = 'upload'
FOLDER_GEOJSON_OUT = 'geojson'
FOLDER_DATA = 'data'


CONVENTION = {
    'all_column_names': lambda constraint, table: '_'.join([
        column.name for column in constraint.columns.values()
    ]),
    'ix': 'ix__%(table_name)s__%(all_column_names)s',
    'uq': 'uq__%(table_name)s__%(all_column_names)s',
    'ck': 'ck__%(table_name)s__%(constraint_name)s',
    'fk': (
        'fk__%(table_name)s__%(all_column_names)s__'
        '%(referred_table_name)s'
    ),
    'pk': 'pk__%(table_name)s'
}

CRS_OUT = 4326  # 4326 - WGS 84


NGP_FILE_GEOJSON_IN = 'NGP.geojson' # 'mest.geojson'
NGP_FILE_GEOJSON_OUT = 'NGP.geojson'
NGP_NAME_FIELD = 'province'
NGP_FILE_LOG = NGP_FILE_GEOJSON_IN + '.log'

NGO_FILE_GEOJSON_IN = 'NGO.geojson' # 'mest.geojson'
NGO_FILE_GEOJSON_OUT = 'NGO.geojson'
NGO_NAME_FIELD = 'region'
NGO_FILE_LOG = NGO_FILE_GEOJSON_IN + '.log'

NGR_FILE_GEOJSON_IN = 'NGR.geojson' # 'mest.geojson'
NGR_FILE_GEOJSON_OUT = 'NGR.geojson'
NGR_NAME_FIELD = 'district'
NGR_FILE_LOG = NGR_FILE_GEOJSON_IN + '.log'

LU_FILE_GEOJSON_IN = 'LU.geojson' # 'mest.geojson'
LU_FILE_GEOJSON_OUT = 'LU.geojson'
LU_FILE_LOG = LU_FILE_GEOJSON_IN + '.log'
LU_NAME_FIELD = 'name'
LU_NOM_LIC_FIELD = 'nom_lic'

WELL_FILE_GEOJSON_IN = 'WELL.geojson' # 'mest.geojson'
WELL_FILE_GEOJSON_OUT = 'WELL.geojson'
WELL_FILE_LOG = WELL_FILE_GEOJSON_IN + '.log'
WELL_NAME_FIELD = 'well_name'
WELL_NAME_AREA_FIELD = 'pl'

FIELDS_FILE_GEOJSON_IN = 'FIELDS.geojson' # 'mest.geojson'
FIELDS_FILE_GEOJSON_OUT = 'FIELDS.geojson'
FIELDS_NAME_FIELD = 'name_ru'
FIELDS_FILE_LOG = FIELDS_FILE_GEOJSON_IN + '.log'

AREA_FILE_LOG = 'AREA.log'
AREA_FILE_GEOJSON_OUT = 'AREA.geojson'


FILE_FTS_INDEX = 'file_path_fts_idx'
REPORT_FTS_INDEX = 'report_path_fts_idx'

MSG_OK = "OK"
MSG_ERROR = "ERROR"

print(f"DEVENV: {DEVENV}")
print(f"SERVER_HOST: {SERVER_HOST}")
print(f"SERVER_PORT: {SERVER_PORT}")
print(f"DB_DSN: {DB_DSN}")
print(f"DB_DSN2 for alembic: {DB_DSN2}")
print(f"http://{SERVER_HOST}:{SERVER_PORT}/docs")





# print(f"DEVENV: {DEVENV}")

# if DEVENV.startswith("dev"):
#     DB_HOST = os.getenv("DB_HOST", "localhost")
# else:
#     DB_HOST = os.getenv("DB_HOST", "r48-vldb02.zsniigg.local")
# # DB_HOST = os.getenv("DB_HOST", "r48-vldb02.zsniigg.local")
#
# DB_PORT = os.getenv("DB_PORT", 5432)
# DB_NAME = os.getenv("DB_NAME", "gdx2")
# DB_SCHEMA = os.getenv("DB_SCHEMA", "gdx2")
# DB_USER = os.getenv("DB_USER", "gdx2")
# DB_PASS = os.getenv("DB_PASS", "gdx2pwd")
# DB_DSN = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
# # DB_DSN_ASYNCIO = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
# DB_DSN2 = f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
# print(DATABASE_URL)
# FOLDER_BASE = os.getenv("FOLDER_BASE", "C:\\Glory\\Projects\\Python\\zsniigg\\gdx2\\src") # C:\\zsniigg\\gdx2\\src
# FOLDER_REPORT = os.getenv("FOLDER_REPORT", "D:\\zsniigg\\") # \\\\r57-vfs02\\archiv002
# redis://username:password@hostname:port/db

# if DEVENV.startswith("dev"):
#
# else:
