import os
from zipfile import ZipFile

from pypdf import PdfReader
from xlrd import open_workbook

from script_os import TMP_DIR

# with ZipFile("tmp/hello.zip") as zip_file:
#     print(zip_file.namelist())
#     text = zip_file.read('Hello.txt')
#     print(text)
#     zip_file.extract('Hello.txt', path="tmp")

def zipdir(path, ziph):
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), path))


if not os.path.exists(os.path.join(os.path.curdir, 'hw')):  # проверяем существует ли папка
    os.mkdir(os.path.join(os.path.curdir, 'hw'))  # создаем папку если её нет
with ZipFile(os.path.join(os.path.curdir, 'hw/homework.zip'), 'w') as zip_file:
    zipdir(os.path.join(TMP_DIR, "files_to_archive"), zip_file)

with ZipFile(os.path.join(os.path.curdir, 'hw/homework.zip'), 'r') as zip_file:
    print(zip_file.namelist())
    for file in zip_file.namelist():
        if file.endswith(".pdf"):
            reader = PdfReader(zip_file.open(file))
            print(reader.pages[0].extract_text())
        elif file.endswith(".xls"):
            workbook = open_workbook(file_contents=zip_file.read(file))
            print(workbook.nsheets)
            print(workbook.sheet_names())
            sheet = workbook.sheet_by_index(0)
            print(sheet.nrows)
            print(sheet.ncols)

