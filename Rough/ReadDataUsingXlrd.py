import xlrd

# wb=xlrd.open_workbook("C:/Users/Guest User/PycharmProjects/POM_Practice1/data/data.xlsx")
# ws=wb.sheet_by_name("Sheet1")
# row_count = ws.nrows
# col_count = ws.ncols

# print("col count ",col_count)

# Reading 1st column data
# for i in range(row_count):
#     val= ws.cell_value(i,0)
#     print(val)

# Reading 2nd row data
# for i in range(col_count):
#     val= ws.cell_value(1,i)
#     print(val)

# Reading entire data
# for i in range(row_count):
#     for j in range(col_count):
#         val= ws.cell_value(i,j)
#         print(val)

# Reading data corresponding to Password
# for i in range(row_count):
#     for j in range(col_count):
#         if (ws.cell_value(i,j)=='PASSWORD'):
#             val= ws.cell_value(i+1,j)
#     break
# print(val)


# TO PRINT VALUE CORRESPONDING TO USERNAME & PASSWORD IN THE PARTICULAR SHEET

def get_val(Sheet_Name,In):

    wb = xlrd.open_workbook("C:/Users/Guest User/PycharmProjects/POM_Practice1/data/data.xlsx")
    ws = wb.sheet_by_name(Sheet_Name)
    row_count = ws.nrows
    col_count = ws.ncols
    for i in range(row_count):
        for j in range(col_count):
            if (ws.cell_value(i, j) == In ):
                val= ws.cell_value(i+1,j)
        break
    return val

return_val = get_val("Sheet1","USERNAME")
print(return_val)

return_val = get_val("Sheet1","PASSWORD")
print(return_val)

