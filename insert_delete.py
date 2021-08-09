# importing necessary libraries

from openpyxl import  workbook,load_workbook

# loading the workBook or Excel file
wb = load_workbook('Munaf.xlsx')
ws = wb.active


# inserting rows
ws.insert_rows(10)
ws.insert_rows(10)


# deleting rows
ws.delete_rows(10)
ws.delete_rows(10)


# inserting colums
ws.insert_cols(2)
ws.insert_cols(2)

# deleting columns
ws.delete_cols(2)

# saving the progress
wb.save('Munaf.xlsx')