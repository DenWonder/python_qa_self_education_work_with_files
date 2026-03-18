import os.path

from xlrd import open_workbook

from script_os import TMP_DIR

workbook = open_workbook(os.path.join(TMP_DIR, "file_example_XLS_50.xls"))
print(workbook.nsheets)
print(workbook.sheet_names())
sheet = workbook.sheet_by_index(0)
print(sheet.nrows)
print(sheet.ncols)
print(sheet.cell_value(rowx=9, colx=3))

for rx in range(sheet.nrows):
    print(sheet.row(rx))