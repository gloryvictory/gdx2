import os.path
import re

from src import cfg
from src.utils.mystrings import strip_last, str_cleanup, removing_leading_whitespaces


def str_tgf_format(str_in: str):
    if len(str_in) > 1:
        return str_in
    else:
        return ''


def str_get_full_path_with_format(str_in: str):
    if len(str_in) and str_in.startswith('\\'):
        if str_in.endswith('\\'):
            str_tmp = str_in.removesuffix('\\')
            return str_tmp
        else:
            return str_in
    else:
        return ''


def str_get_last_folder(str_in: str):
    if len(str_in) and str_in.startswith('\\'):
        str_arr = str_in.rsplit('\\', 1)
        if len(str_arr):
            str_tmp = str(str_arr[1])
        else:
            str_tmp = ""
        return str_tmp
    else:
        return ''


# удаляем \\R57-vfs01\volarch и пр...
def str_get_folder(str_in: str):
    if len(str_in) and str_in.startswith('\\'):
        str_arr = str_in.split("\\")
        del str_arr[0:4]  # удаляем \\R57-vfs01\volarch и пр...
        if len(str_arr):
            str_tmp = str(os.path.join(*str_arr))
        else:
            str_tmp = ""
        return str_tmp
    else:
        return ''


# получаем \\R57-vfs01\volarch и пр...
def str_get_folder_src(str_in: str):
    if len(str_in) and str_in.startswith('\\'):
        str_arr = str_in.split("\\")
        del str_arr[4:len(str_arr)]  # получаем \\R57-vfs01\volarch и пр...
        if len(str_arr):
            str_tmp = '\\' + '\\' + str(os.path.join(*str_arr))
        else:
            str_tmp = ""
        return str_tmp
    else:
        return ''


def str_get_rgf(tgf_kurgan: str, tgf_tmn: str, tgf_more: str, tgf_tomsk: str, tgf_novo: str, tgf_omsk: str, tgf_ekat: str, tgf_kras: str, tgf_ynao: str, tgf_hmao: str, rgf: str):
    tgf = 'Отсутствует'
    if len(tgf_kurgan):
        tgf = 'КурганТГФ'
        return tgf
    if len(tgf_tmn):
        tgf = 'ТюмТГФ'
        return tgf
    if len(tgf_more):
        tgf = 'МорскойТГФ'
        return tgf
    if len(tgf_tomsk):
        tgf = 'ТомскТГФ'
        return tgf
    if len(tgf_novo):
        tgf = 'НовосибТГФ'
        return tgf
    if len(tgf_omsk):
        tgf = 'ОмскТГФ'
        return tgf
    if len(tgf_ekat):
        tgf = 'ЕкатерТГФ'
        return tgf
    if len(tgf_kras):
        tgf = 'КраснТГФ'
        return tgf
    if len(tgf_ynao):
        tgf = 'ЯНТГФ'
        return tgf
    if len(tgf_hmao):
        tgf = 'ХМТГФ'
        return tgf
    if len(rgf):
        tgf = 'РГФ'
        return tgf
    return tgf


def str_clean(str_in: str):
    str_tmp = str_cleanup(str_in)
    str_tmp = removing_leading_whitespaces(str_tmp)
    # str_tmp = cleanupstring(str_tmp)

    str_tmp = str_tmp.lstrip() \
                  .rstrip() \
                  .replace("Авторы:", "") \
                  .replace("Леонов А.П.", "Леонов А.П.,") \
                  .replace("Ляхов С.В.", "Ляхов С.В.,") \
                  .replace("Чунихина Л.Д.", "Чунихина Л.Д.,") \
                  .replace("Херувимова Е.В.", "Херувимова Е.В.,") \
                  .replace("Брадучан Ю.В.", "Брадучан Ю.В.,") \
                  .replace("Дьяконова Ю.А", "Дьяконова Ю.А.,") \
                  .replace("Кос.И.М.", "Кос И.М.,") \
                  .replace("ЗАО НПК «Форум»", " ") \
                  .replace("и др.", ",") \
                  .replace(" др.", ",") \
                  .replace(" др", ",") \
                  .replace("отв. исполнитель", "") \
                  .replace("г.", "") \
                  .replace("0", "") \
                  .replace("1", "") \
                  .replace("2", "") \
                  .replace("3", "") \
                  .replace("4", "") \
                  .replace("5", "") \
                  .replace("6", "") \
                  .replace("7", "") \
                  .replace("8", "") \
                  .replace("9", "") \
                  .replace("0", "") \
                  .replace("/", "") \
                  .replace("\n", "") \
                  .replace("-", "") \
                  .replace(" и ", ",") \
                  .replace("  ", "") \
                  .replace(")", "") \
                  .replace("(", ",") \
                  .replace(" - ", ",") \
                  .replace(" Есть ", ",") \
                  .replace("\xa0", ",") \
                  .replace("_x001E_", "") \
                  .replace("\t", "") \
                  .replace("  ", "") \
                  .replace(", ", ",") \
                  .replace("; ", ", ") \
                  .replace(";",",") \
                  .replace(",,,", ",") \
                  .replace(",,", ",") \
                  .replace("См_____", " ") \
                  .replace("См____", " ") \
                  .replace(". ", ".") \
                  .lstrip() \
                  .rstrip() \
                  .strip() + ','
    # .replace(". и", ".") \
    # if str_tmp.startswith(" "):
    #     str_tmp = str_tmp.replace(" ", "")
    if str_tmp.endswith(" "):
        str_tmp = strip_last(str_tmp)

    if len(str_tmp):
        result = re.match("\s", str_tmp)
        if result:
            str_tmp = str_tmp.strip()
    return str_tmp
