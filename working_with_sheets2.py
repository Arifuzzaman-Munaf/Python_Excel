# importing necessary libraries

from openpyxl import Workbook,load_workbook

# loading the workBook or Excel file
wb = Workbook()

# printing the deafult name of the sheet when we create workbook
ws = wb.active
print(ws)

# setting the title of worksheet as 'Data'
ws.title = 'Data'

# appending data to worksheet
for i in range(20):
    ws.append(['I', 'am', 'working', 'with', 'openpyxl'])

# saving the progress
wb.save('Munaf.xlsx')