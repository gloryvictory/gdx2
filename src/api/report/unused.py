# import os
# import re
# from datetime import datetime
#
# from sqlalchemy import text, insert, select
#
# from src import cfg
# from src.api.report.services import report_excel_file_read
# from src.api.report.utils import  str_clean, \
#      list_str_clean
# from src.db.db import async_session_maker
# from src.models import M_REPORT_TGF, M_R_AUTHOR, M_R_LIST, M_R_SUBRF, M_R_ORG, M_R_AREA, M_R_FIELD, M_R_LU, M_R_PI, \
#     M_R_VID_RAB
#
# async def report_update_from_file():
#     content = {"msg": "Fail"}
#     try:
#         time1 = datetime.now()
#         file_report_in = os.path.join(cfg.FOLDER_REPORT, cfg.FILE_REPORT_NAME)
#         file_report_out = os.path.join(cfg.FOLDER_BASE, cfg.FOLDER_UPLOAD, cfg.FILE_REPORT_NAME)
#         shutil.copyfile(file_report_in, file_report_out)
#         print(f"{file_report_in} is copied to {file_report_out} - OK.")
#         await report_excel_file_read(str(file_report_out))
#         await report_get_update_author()
#         await report_get_update_subrf()
#         await report_get_update_org()
#         await report_get_update_area()
#         await report_get_update_list()
#         await report_get_update_field()
#         await report_get_update_lu()
#         await report_get_update_pi()
#         await report_get_update_vid_rab()
#         await report_index_create()
#         time2 = datetime.now()
#         print(f"Обработано: {file_report_out}. Total time:  + {str(time2 - time1)}")
#         content = {"msg": "Success", "count": 1}
#         return content
#     except Exception as e:
#         content = {"msg": f"reload fail. can't... "}
#         print("Exception occurred " + str(e))
#         # fastapi_logger.exception("update_user_password")
#         return content
#
# async def report_get_update_author():
#     content = {"msg": "Fail"}
#     try:
#         authors = []
#         async with async_session_maker() as session:
#             # truncate table
#             stmt = text(f"TRUNCATE {M_R_AUTHOR.__tablename__} RESTART IDENTITY;")
#             await session.execute(stmt)
#             await session.commit()
#             #
#             res = await session.scalars(
#                 select(M_REPORT_TGF.author_name)
#                 .where(M_REPORT_TGF.author_name != '')
#                 .order_by(M_REPORT_TGF.author_name)
#             )
#             _all = res.all()
#             for author_name in _all:
#                 author_tmp = str_clean(author_name).lstrip()
#                 # print(author_tmp)
#                 if len(author_tmp) > 2:
#                     result = re.match(r'^0-9', author_tmp)
#                     result2 = re.match(r'[^\D]', author_tmp)
#                     if not result or not result2:
#                         authors.append(author_tmp)
#             authors_str = ",".join(authors)
#             authors2 = authors_str.split(",")
#             authors3 = []
#             # Обрабатываем список авторов и добавляем . если ее нет
#             for author in authors2:
#                 if not author.startswith("<openpyxl"):
#                     author_tmp1 = author.strip()
#                     if len(author_tmp1) > 3 and (not author_tmp1.endswith(".") and author_tmp1[-1].isupper()):
#                         author_tmp1 = author_tmp1 + "."
#                     authors3.append(author_tmp1)
#
#             authors_tmp2 = sorted(set(authors3))  # Получаем уникальные элементы
#             for author in authors_tmp2:
#                 if len(author) > 2:
#                     print(author)
#                     stmt = insert(M_R_AUTHOR).values(
#                         name_ru=author
#                     )
#                     await session.execute(stmt)
#                     await session.commit()
#             _cnt = len(authors_tmp2)
#             content = {"msg": "Success", "count": _cnt, "data": authors_tmp2}
#         # log.info("ngp load successfully")
#         return content
#     except Exception as e:
#         content = {"msg": "Fail", "data": f"Can't get all reports from {M_REPORT_TGF.__tablename__}... "}
#         print("Exception occurred " + str(e))
#         # fastapi_logger.exception("update_user_password")
#         return content
#
#
# async def report_get_update_list():
#     content = {"msg": "Fail"}
#     try:
#         lists = []
#         async with async_session_maker() as session:
#             # truncate table
#             stmt = text(f"TRUNCATE {M_R_LIST.__tablename__} RESTART IDENTITY;")
#             await session.execute(stmt)
#             await session.commit()
#             #
#             res = await session.scalars(
#                 select(M_REPORT_TGF.list_name)
#                 .where(M_REPORT_TGF.list_name != '')
#                 .order_by(M_REPORT_TGF.list_name)
#             )
#             _all = res.all()
#             for list_name in _all:
#                 list_tmp = list_str_clean(list_name)
#                 # print(author_tmp)
#                 if len(list_tmp) > 2:
#                     lists.append(list_tmp)
#             lists_str = ",".join(lists)
#             lists2 = lists_str.split(",")
#             lists3 = []
#             # Обрабатываем список авторов и добавляем . если ее нет
#             for author in lists2:
#                 author_tmp1 = author.strip()
#                 lists3.append(author_tmp1)
#
#             lists_tmp2 = sorted(set(lists3))  # Получаем уникальные элементы
#             for list in lists_tmp2:
#                 if len(list) > 2:
#                     stmt = insert(M_R_LIST).values(
#                         name_ru=list
#                     )
#                     await session.execute(stmt)
#                     await session.commit()
#             _cnt = len(lists_tmp2)
#             content = {"msg": "Success", "count": _cnt, "data": lists_tmp2}
#         # log.info("ngp load successfully")
#         return content
#     except Exception as e:
#         content = {"msg": "Fail", "data": f"Can't get all reports from {M_REPORT_TGF.__tablename__}... "}
#         print("Exception occurred " + str(e))
#         # fastapi_logger.exception("update_user_password")
#         return content
#
#
# async def report_get_update_subrf():
#     content = {"msg": "Fail"}
#     try:
#         subrfs = []
#         async with async_session_maker() as session:
#             # truncate table
#             stmt = text(f"TRUNCATE {M_R_SUBRF.__tablename__} RESTART IDENTITY;")
#             await session.execute(stmt)
#             await session.commit()
#             #
#             res = await session.scalars(
#                 select(M_REPORT_TGF.subrf_name)
#                 .where(M_REPORT_TGF.subrf_name != '')
#                 .order_by(M_REPORT_TGF.subrf_name)
#             )
#             _all = res.all()
#             for subrf_name in _all:
#                 subrf_tmp = str_clean(subrf_name).lstrip()
#                 if len(subrf_tmp) > 2:
#                     subrfs.append(subrf_tmp)
#             subrfs_str = ",".join(subrfs)
#             subrfs2 = subrfs_str.split(",")
#             subrfs3 = []
#             # Обрабатываем список авторов и добавляем . если ее нет
#             for subrf in subrfs2:
#                 if not subrf.startswith("<openpyxl"):
#                     subrf_tmp1 = subrf.strip()
#                     subrfs3.append(subrf_tmp1)
#
#             subrfs_tmp2 = sorted(set(subrfs3))  # Получаем уникальные элементы
#             for subrf in subrfs_tmp2:
#                 if len(subrf) > 2:
#                     stmt = insert(M_R_SUBRF).values(
#                         name_ru=subrf
#                     )
#                     await session.execute(stmt)
#                     await session.commit()
#             _cnt = len(subrfs_tmp2)
#             content = {"msg": "Success", "count": _cnt, "data": subrfs_tmp2}
#         # log.info("ngp load successfully")
#         return content
#     except Exception as e:
#         content = {"msg": "Fail", "data": f"Can't get all reports from {M_REPORT_TGF.__tablename__}... "}
#         print("Exception occurred " + str(e))
#         # fastapi_logger.exception("update_user_password")
#         return content
#
#
# async def report_get_update_org():
#     content = {"msg": "Fail"}
#     try:
#         orgs = []
#         async with async_session_maker() as session:
#             # truncate table
#             stmt = text(f"TRUNCATE {M_R_ORG.__tablename__} RESTART IDENTITY;")
#             await session.execute(stmt)
#             await session.commit()
#             #
#             res = await session.scalars(
#                 select(M_REPORT_TGF.org_name)
#                 .where(M_REPORT_TGF.org_name != '')
#                 .order_by(M_REPORT_TGF.org_name)
#             )
#             _all = res.all()
#             for org_name in _all:
#                 org_tmp = str_clean(org_name).lstrip()
#                 if len(org_tmp) > 2:
#                     orgs.append(org_tmp)
#             orgs_str = ",".join(orgs)
#             orgs2 = orgs_str.split(",")
#             orgs3 = []
#             # Обрабатываем список авторов и добавляем . если ее нет
#             for org in orgs2:
#                 org_tmp1 = org.strip()
#                 if not org_tmp1.startswith("<openpyxl"):
#                     orgs3.append(org_tmp1)
#
#             orgs_tmp2 = sorted(set(orgs3))  # Получаем уникальные элементы
#             for org in orgs_tmp2:
#                 if len(org) > 2:
#                     stmt = insert(M_R_ORG).values(
#                         name_ru=org
#                     )
#                     await session.execute(stmt)
#                     await session.commit()
#             _cnt = len(orgs_tmp2)
#             content = {"msg": "Success", "count": _cnt, "data": orgs_tmp2}
#         # log.info("ngp load successfully")
#         return content
#     except Exception as e:
#         content = {"msg": "Fail", "data": f"Can't get all reports from {M_REPORT_TGF.__tablename__}... "}
#         print("Exception occurred " + str(e))
#         # fastapi_logger.exception("update_user_password")
#         return content
#
#
# async def report_get_update_area():
#     content = {"msg": "Fail"}
#     try:
#         areas = []
#         async with async_session_maker() as session:
#             # truncate table
#             stmt = text(f"TRUNCATE {M_R_AREA.__tablename__} RESTART IDENTITY;")
#             await session.execute(stmt)
#             await session.commit()
#             #
#             res = await session.scalars(
#                 select(M_REPORT_TGF.areaoil)
#                 .where(M_REPORT_TGF.areaoil != '')
#                 .order_by(M_REPORT_TGF.areaoil)
#             )
#             _all = res.all()
#             for area_name in _all:
#                 area_tmp = str_clean(area_name).lstrip()
#                 if len(area_tmp) > 2:
#                     areas.append(area_tmp)
#             areas_str = ",".join(areas)
#             areas2 = areas_str.split(",")
#             areas3 = []
#             for area in areas2:
#                 area_tmp1 = area.strip()
#                 if not area_tmp1.startswith("<openpyxl"):
#                     areas3.append(area_tmp1)
#
#             areas_tmp2 = sorted(set(areas3))  # Получаем уникальные элементы
#             for area in areas_tmp2:
#                 if len(area) > 2:
#                     stmt = insert(M_R_AREA).values(
#                         name_ru=area
#                     )
#                     await session.execute(stmt)
#                     await session.commit()
#             _cnt = len(areas_tmp2)
#             content = {"msg": "Success", "count": _cnt, "data": areas_tmp2}
#         # log.info("ngp load successfully")
#         return content
#     except Exception as e:
#         content = {"msg": "Fail", "data": f"Can't get all reports from {M_REPORT_TGF.__tablename__}... "}
#         print("Exception occurred " + str(e))
#         # fastapi_logger.exception("update_user_password")
#         return content
#
#
# async def report_get_update_field():
#     content = {"msg": "Fail"}
#     try:
#         fields = []
#         async with async_session_maker() as session:
#             # truncate table
#             stmt = text(f"TRUNCATE {M_R_FIELD.__tablename__} RESTART IDENTITY;")
#             await session.execute(stmt)
#             await session.commit()
#             #
#             res = await session.scalars(
#                 select(M_REPORT_TGF.field)
#                 .where(M_REPORT_TGF.field != '')
#                 .order_by(M_REPORT_TGF.field)
#             )
#             _all = res.all()
#             for field_name in _all:
#                 field_tmp = str_clean(field_name).lstrip()
#                 if len(field_tmp) > 2:
#                     fields.append(field_tmp)
#             fields_str = ",".join(fields)
#             fields2 = fields_str.split(",")
#             fields3 = []
#             for field in fields2:
#                 field_tmp1 = field.strip()
#                 if not field_tmp1.startswith("<openpyxl"):
#                     fields3.append(field_tmp1)
#
#             fields_tmp2 = sorted(set(fields3))  # Получаем уникальные элементы
#             for field in fields_tmp2:
#                 if len(field) > 2:
#                     stmt = insert(M_R_FIELD).values(
#                         name_ru=field
#                     )
#                     await session.execute(stmt)
#                     await session.commit()
#             _cnt = len(fields_tmp2)
#             content = {"msg": "Success", "count": _cnt, "data": fields_tmp2}
#         # log.info("ngp load successfully")
#         return content
#     except Exception as e:
#         content = {"msg": "Fail", "data": f"Can't get all reports from {M_REPORT_TGF.__tablename__}... "}
#         print("Exception occurred " + str(e))
#         # fastapi_logger.exception("update_user_password")
#         return content
#
#
# async def report_get_update_lu():
#     content = {"msg": "Fail"}
#     try:
#         lus = []
#         async with async_session_maker() as session:
#             # truncate table
#             stmt = text(f"TRUNCATE {M_R_LU.__tablename__} RESTART IDENTITY;")
#             await session.execute(stmt)
#             await session.commit()
#             #
#             res = await session.scalars(
#                 select(M_REPORT_TGF.lu)
#                 .where(M_REPORT_TGF.lu != '')
#                 .order_by(M_REPORT_TGF.lu)
#             )
#             _all = res.all()
#             for lu_name in _all:
#                 lu_tmp = str_clean(lu_name).lstrip()
#                 if len(lu_tmp) > 2:
#                     lus.append(lu_tmp)
#             lus_str = ",".join(lus)
#             lus2 = lus_str.split(",")
#             lus3 = []
#             for lu in lus2:
#                 lu_tmp1 = lu.strip()
#                 if not lu_tmp1.startswith("<openpyxl"):
#                     lus3.append(lu_tmp1)
#
#             lus_tmp2 = sorted(set(lus3))  # Получаем уникальные элементы
#             for lu in lus_tmp2:
#                 if len(lu) > 2:
#                     stmt = insert(M_R_LU).values(
#                         name_ru=lu
#                     )
#                     await session.execute(stmt)
#                     await session.commit()
#             _cnt = len(lus_tmp2)
#             content = {"msg": "Success", "count": _cnt, "data": lus_tmp2}
#         # log.info("ngp load successfully")
#         return content
#     except Exception as e:
#         content = {"msg": "Fail", "data": f"Can't get all reports from {M_REPORT_TGF.__tablename__}... "}
#         print("Exception occurred " + str(e))
#         # fastapi_logger.exception("update_user_password")
#         return content
#
#
# async def report_get_update_pi():
#     content = {"msg": "Fail"}
#     try:
#         pis = []
#         async with async_session_maker() as session:
#             # truncate table
#             stmt = text(f"TRUNCATE {M_R_PI.__tablename__} RESTART IDENTITY;")
#             await session.execute(stmt)
#             await session.commit()
#             #
#             res = await session.scalars(
#                 select(M_REPORT_TGF.pi_name)
#                 .where(M_REPORT_TGF.pi_name != '')
#                 .order_by(M_REPORT_TGF.pi_name)
#             )
#             _all = res.all()
#             for pi_name in _all:
#                 pi_tmp = str_clean(pi_name).lstrip()
#                 if len(pi_tmp) > 2:
#                     pis.append(pi_tmp)
#             pis_str = ",".join(pis)
#             pis2 = pis_str.split(",")
#             pis3 = []
#             for pi in pis2:
#                 pi_tmp1 = pi.strip()
#                 if not pi_tmp1.startswith("<openpyxl"):
#                     pis3.append(pi_tmp1)
#
#             pis_tmp2 = sorted(set(pis3))  # Получаем уникальные элементы
#             for pi in pis_tmp2:
#                 if len(pi) > 2:
#                     stmt = insert(M_R_PI).values(
#                         name_ru=pi
#                     )
#                     await session.execute(stmt)
#                     await session.commit()
#             _cnt = len(pis_tmp2)
#             content = {"msg": "Success", "count": _cnt, "data": pis_tmp2}
#         # log.info("ngp load successfully")
#         return content
#     except Exception as e:
#         content = {"msg": "Fail", "data": f"Can't get all reports from {M_REPORT_TGF.__tablename__}... "}
#         print("Exception occurred " + str(e))
#         # fastapi_logger.exception("update_user_password")
#         return content
#
#
# async def report_get_update_vid_rab():
#     content = {"msg": "Fail"}
#     try:
#         vid_rabs = []
#         async with async_session_maker() as session:
#             # truncate table
#             stmt = text(f"TRUNCATE {M_R_VID_RAB.__tablename__} RESTART IDENTITY;")
#             await session.execute(stmt)
#             await session.commit()
#             #
#             res = await session.scalars(
#                 select(M_REPORT_TGF.vid_rab)
#                 .where(M_REPORT_TGF.vid_rab != '')
#                 .order_by(M_REPORT_TGF.vid_rab)
#             )
#             _all = res.all()
#             for vid_rab_name in _all:
#                 vid_rab_tmp = str_clean(vid_rab_name).lstrip()
#                 if len(vid_rab_tmp) > 2:
#                     vid_rabs.append(vid_rab_tmp)
#             vid_rabs_str = ",".join(vid_rabs)
#             vid_rabs2 = vid_rabs_str.split(",")
#             vid_rabs3 = []
#             for vid_rab in vid_rabs2:
#                 vid_rab_tmp1 = vid_rab.strip()
#                 if not vid_rab_tmp1.startswith("<openpyxl"):
#                     vid_rabs3.append(vid_rab_tmp1)
#
#             vid_rabs_tmp2 = sorted(set(vid_rabs3))  # Получаем уникальные элементы
#             for vid_rab in vid_rabs_tmp2:
#                 if len(vid_rab) > 2:
#                     stmt = insert(M_R_VID_RAB).values(
#                         name_ru=vid_rab
#                     )
#                     await session.execute(stmt)
#                     await session.commit()
#             _cnt = len(vid_rabs_tmp2)
#             content = {"msg": "Success", "count": _cnt, "data": vid_rabs_tmp2}
#         # log.info("ngp load successfully")
#         return content
#     except Exception as e:
#         content = {"msg": "Fail", "data": f"Can't get all reports from {M_REPORT_TGF.__tablename__}... "}
#         print("Exception occurred " + str(e))
#         # fastapi_logger.exception("update_user_password")
#         return content
#
#