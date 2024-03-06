import os
import re

import openpyxl
import sqlalchemy
from fastapi import UploadFile, File
from sqlalchemy import text, insert, select, func
from sqlalchemy.orm import Session

from src import cfg
from src.api.report.utils import str_get_folder, str_get_full_path_with_format, str_tgf_format, str_clean, \
    str_get_last_folder, str_get_folder_src
from src.db.db import async_session_maker
from src.models import M_REPORT_TGF
from src.utils.mystrings import str_cleanup


async def report_all_objects():
    content = {"msg": "Fail"}
    try:
        # content = {"msg": "Success", "count": 111111}
        # async with async_session_maker() as session:
        #     #  НГП
        #     res = await session.scalars(
        #         select(M_NSI_NGP)
        #         .order_by(M_NSI_NGP.name_ru)
        #     )
        #     _all = res.all()
        #     _cnt = len(all_data)
        #     cnt = cnt + _cnt
        #     content = {"msg": "Success", "count": cnt, "data": all_data}
        # log.info("ngp load successfully")
        return content
    except Exception as e:
        content = {"msg": f"reload fail. can't... "}
        print("Exception occurred " + str(e))
        # fastapi_logger.exception("update_user_password")
        return content


async def report_upload_file(file: UploadFile = File(...)):
    content = {"msg": f"Unknown error"}
    try:
        if not os.path.isdir(cfg.FOLDER_UPLOAD):
            os.mkdir(cfg.FOLDER_UPLOAD)
        file_in = file.filename
        file_out = file.filename.replace(" ", "-")

        file_name = os.path.join(os.getcwd(), cfg.FOLDER_UPLOAD, file_out)

        if os.path.exists(file_name):
            os.remove(file_name)
            print(f"{file_name} - deleted !")

        contents = file.file.read()
        with open(file_name, 'wb') as f:
            f.write(contents)

        # adoc_hist = ADOC_HISTORY_M(file_in=file_in, file_out=file_out, file_out_path=file_name)
        # await adoc_hist.upsert()

        all_count = 1
        content = {"msg": "Success", "count": all_count, "filename": file.filename}

        # await adoc_excel_file_read(file_name)
        return content
    except Exception as e:
        str_err = "Exception occurred " + str(e)
        content = {"msg": f"Error. There was an error uploading the file", "err": str(e)}
        print(str_err)
        # log.info(str_err)
    finally:
        file.file.close()

    return content


#
async def report_update():
    content = {"msg": "Fail"}
    try:
        content = {"msg": "Success", "count": 1}
        file_report_in = os.path.join(cfg.FOLDER_BASE, cfg.FOLDER_UPLOAD, cfg.FILE_REPORT_NAME)
        await report_excel_file_read(str(file_report_in))
        return content
    except Exception as e:
        content = {"msg": f"reload fail. can't... "}
        print("Exception occurred " + str(e))
        # fastapi_logger.exception("update_user_password")
        return content


async def report_excel_file_read(file_in: str):
    print(f"File input {file_in}")
    # Define variable to load the wookbook
    wookbook = openpyxl.load_workbook(file_in)

    # Define variable to read the active sheet:
    worksheet = wookbook.active

    # Iterate the loop to read the cell values
    # worksheet.max_row
    # worksheet.max_column
    # 18 колонок
    cnt = 0
    min_row = 2
    max_row = worksheet.max_row
    min_col = 1
    max_col = 30
    engine = sqlalchemy.create_engine(cfg.DB_DSN2)

    try:
        authors = []
        # create session and add objects
        with Session(engine) as session:
            session.query(M_REPORT_TGF).delete()
            session.commit()
            for value in worksheet.iter_rows(min_row=min_row, max_row=max_row, min_col=min_col, max_col=max_col,
                                             values_only=True):
                print(f"{cnt}")
                cnt = cnt + 1
                folder_root = ''
                folder_link = ''
                folder_short = ''
                folder_name = ''
                rgf = ''
                tgf_hmao = ''
                tgf_ynao = ''
                tgf_kras = ''
                tgf_ekat = ''
                tgf_omsk = ''
                tgf_novo = ''
                tgf_tomsk = ''
                tgf_more = ''
                tgf_tmn = ''
                tgf_kurgan = ''
                tgf = ''
                report_name = ''
                author_name = ''
                year_str = ''
                year_int = 0
                territory_name = ''
                subrf_name = ''
                list_name = ''
                part_name = ''
                areaoil = ''
                field = ''
                lu = ''
                pi_name = ''
                fin_name = ''
                org_name = ''
                zsniigg_report = ''
                inf_report = ''
                vid_rab = ''

                comments = ''

                if value[0]:  # Путь полный
                    folder_root = str_get_full_path_with_format(str(value[0]))
                    folder_link = str_get_folder_src(folder_root)  # Гиперссылка
                    folder_short = str_get_folder(folder_root)
                    folder_name = str_get_last_folder(folder_root)
                    print(folder_root)
                    print(folder_link)
                    # print(folder_short)
                    # print(folder_name)

                if value[1]:  # Инв. номер РГФ
                    rgf = str_tgf_format(str(value[1]))
                    print(rgf)
                if value[2]:
                    tgf_hmao = str_tgf_format(str(value[2]))
                    # print(tgf_hmao)
                if value[3]:
                    tgf_ynao = str_tgf_format(str(value[3]))
                    # print(tgf_ynao)
                if value[4]:
                    tgf_kras = str_tgf_format(str(value[4]))
                    # print(tgf_kras)
                if value[5]:
                    tgf_ekat = str_tgf_format(str(value[5]))
                    # print(tgf_ekat)
                if value[6]:
                    tgf_omsk = str_tgf_format(str(value[6]))
                    # print(tgf_omsk)
                if value[7]:
                    tgf_novo = str_tgf_format(str(value[7]))
                    # print(tgf_novo)
                if value[8]:
                    tgf_tomsk = str_tgf_format(str(value[8]))
                    # print(tgf_tomsk)
                if value[9]:
                    tgf_more = str_tgf_format(str(value[9]))
                    # print(tgf_more)
                if value[10]:
                    tgf_tmn = str_tgf_format(str(value[10]))
                    # print(tgf_tmn)
                if value[11]:
                    tgf_kurgan = str_tgf_format(str(value[11]))
                    # print(tgf_kurgan)
                if value[12]:
                    tgf = str_tgf_format(str(value[12]))
                    print(tgf)

                if value[13]:  # Отчет
                    str_tmp1 = str(value[13]).strip().replace("_x001E_", "")
                    report_name = str_cleanup(str_tmp1)
                    # print(report_name)
                #
                if value[14]:  # Авторы
                    author_name = str(value[14]).strip()
                    # print(author_name)
                    # author_tmp = str_clean(author_name)
                #     if len(author_tmp) > 2:
                #         result = re.match(r'^0-9', author_tmp)
                #         result2 = re.match(r'[^\D]', author_tmp)
                #         if not result or not result2:
                #             authors.append(author_tmp)
                #
                if value[15]:  # Год
                    year_str = str(value[15]).strip()
                    year_tmp = year_str.split()
                    if len(year_tmp):  # разбираем такое 2009   2009   2010
                        year_int = int(year_tmp[0])  # забираем первый год
                        # print(year_int)
                if value[16]:  # Территория
                    territory_name = str(value[16]).strip()
                    # print(territory_name)
                if value[17]:  # Субъект РФ
                    subrf_name = str(value[17]).strip()
                    # print(subrf_name)

                if value[18]:  # Листы
                    list_name = str(value[18]).strip()
                    # print(list_name)

                if value[19]:  # № партии
                    part_name = str(value[19]).strip()
                    # print(part_name)
                if value[20]:  # Площадь
                    areaoil = str(value[20]).strip()
                    # print(areaoil)

                if value[21]:  # Месторождение
                    field = str(value[21]).strip()
                    # print(field)

                if value[22]:  # ЛУ
                    lu = str(value[22]).strip()
                    # print(lu)

                if value[23]:  # ПИ
                    pi_name = str(value[23]).strip()
                    # print(pi_name)

                if value[24]:  # Источник финансирования
                    fin_name = str(value[24]).strip()
                    # print(fin_name)

                if value[25]:  # Организация
                    org_name = str(value[25]).strip()
                    # print(org_name)

                if value[26]:  # Отчет ЗапСибНИИГГ
                    zsniigg_report = str(value[26]).strip()
                    # print(zsniigg_report)

                if value[27]:  # Информационный отчет
                    inf_report = str(value[27]).strip()
                    # print(inf_report)

                if value[28]:  # Вид работ
                    vid_rab = str(value[28]).strip()
                    # print(vid_rab)

                if value[29]:  # Комментарии
                    comments = str(value[29]).strip()
                    print(comments)

                stmt = insert(M_REPORT_TGF).values(
                    folder_root=folder_root,
                    folder_link=folder_link,
                    folder_short=folder_short,
                    folder_name=folder_name,
                    rgf=rgf,
                    tgf_hmao=tgf_hmao,
                    tgf_ynao=tgf_ynao,
                    tgf_kras=tgf_kras,
                    tgf_ekat=tgf_ekat,
                    tgf_omsk=tgf_omsk,
                    tgf_novo=tgf_novo,
                    tgf_tomsk=tgf_tomsk,
                    tgf_more=tgf_more,
                    tgf_tmn=tgf_tmn,
                    tgf_kurgan=tgf_kurgan,
                    tgf=tgf,
                    report_name=report_name,
                    author_name=author_name,
                    year_str=year_str,
                    year_int=year_int,
                    territory_name=territory_name,
                    subrf_name=subrf_name,
                    list_name=list_name,
                    part_name=part_name,
                    areaoil=areaoil,
                    field=field,
                    lu=lu,
                    pi_name=pi_name,
                    fin_name=fin_name,
                    org_name=org_name,
                    zsniigg_report=zsniigg_report,
                    inf_report=inf_report,
                    vid_rab=vid_rab,
                    comments=comments,
                )
                session.execute(stmt)
                session.commit()

            # await ADOC_M(
            #     folder_root=folder_root,
            #     folder_link=folder_link,
            #     folder_short=folder_short,
            #     folder_name=folder_name,
            #     rgf=rgf,
            #     tgf_hmao=tgf_hmao,
            #     tgf_ynao=tgf_ynao,
            #     tgf_kras=tgf_kras,
            #     tgf_ekat=tgf_ekat,
            #     tgf_omsk=tgf_omsk,
            #     tgf_novo=tgf_novo,
            #     tgf_more=tgf_more,
            #     tgf_tmn=tgf_tmn,
            #     tgf=tgf,
            #     report_name=report_name,
            #     author_name=author_name,
            #     year_str=year_str,
            #     year_int=year_int,
            #     territory_name=territory_name,
            #     comments=comments
            # ).save()

        # authors_str = ",".join(authors)
        # authors2 = authors_str.split(",")
        # authors_tmp2 = sorted(set(authors2))
        # for author in authors_tmp2:
        #     if len(author) > 2:
        #         await AUTHOR_M(author_name=author).save()

    except Exception as e:
        str_err = "Exception occurred " + str(e)
        content = {"msg": f"ERROR!!! cnt is {cnt}", "err": str(e)}
        print(str_err)
