from openpyxl import load_workbook
# Import relevant modules fomr `openpyxl.utils`
from openpyxl.utils import get_column_letter, column_index_from_string

def f():
    # open workbook
    wb = load_workbook('test1.xlsx')
    print(wb.get_sheet_names)

    # open sheet
    sheet = wb['Sheet1']
    print(sheet.title)

    anotherSheet = wb.active
    print(anotherSheet)

    # Retrieve the value of a certain cell
    print(sheet['A1'].value)

    #Select element 'B2' of your sheet
    c = sheet['B2']
    print(c.value)

    # Retrieve the row number of your element
    print(c.row)
    
    # Retrieve the column letter of your element
    print(c.column)

    # Retrieve the coordinates of the cell
    print(c.coordinate)

    # Retrieve cell value
    print(sheet.cell(row=1,column=2).value)

    # Print out values in column 2
    for i in range(1,4):
        print(i, sheet.cell(row=i, column=2).value)

    # Return 'A'
    print(get_column_letter(1))

    # Return '1'
    print(column_index_from_string('A'))

    # Retrieve the maximum amount of rows
    print(sheet.max_row)

    # Retrieve the maximum amount of columns
    print(sheet.max_column)

    # Print row per row
    for cell_object in sheet['A1':'C3']:
        for cell in cell_object:
            print(cell.coordinate, cell.value)
        print('--- END ---')
    
            
    
    
