from src import cfg
from src.files.models import FILES_M
import asyncpg


async def files_get_all_count():
    content = {"msg": f"Unknown error"}
    # log = set_logger(settings.WELL_FILE_LOG)
    try:
        all_count = await FILES_M.objects.count()
        # log.info(f"count load successfuly: {all_count}")
        content = {"msg": "Success", "count": all_count}
        return content
    except Exception as e:
        str_err = "Exception occurred " + str(e)
        content = {"msg": f"reload fail. can't read count from table {FILES_M.Meta.tablename}", "err": str(e)}
        print(str_err)
        # log.info(str_err)
    return content

