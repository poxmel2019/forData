from openpyxl import load_workbook
from openpyxl import Workbook
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

def f1():
    # D:\mySpreadsheets
    global i, j, texts
    wb = load_workbook('D:\\mySpreadsheets\\books.xlsx')
    sheet = wb['Лист1']
    needed_cell = sheet['C53']
    #print(needed_cell.value)

    texts = []
    authors = []

    i = 0
    coordinates = [['C53','C55'],['D53','D55']]
    for i in range(0,2):
        for cell_object in sheet[coordinates[i][0]:coordinates[i][1]]:
            for cell in cell_object:
                if i == 0:
                    texts.append(cell.value)
                elif i == 1:
                    authors.append(cell.value)
        i += 1

    print(texts)
    print(authors)


    file = open('D:\\pyda\\прочитанное\\2020.txt','a',encoding='utf-8')
    #f = file.readlines()
    file.write('\n')
    i = 0
    for x in range(0,len(texts)):
        file.write(texts[i] + ' - ' + authors[i] + '\n')
        i += 1
    file.close()

def f():

    #wb = Workbook('D:\\mySpreadsheets\\books.xlsx')
    wb = load_workbook('D:\\mySpreadsheets\\books.xlsx')
    ws = wb.active
    #sheet = ws['Лист1']
    ws['C56'] = 'text'
    ws['D56'] = 'author'
    wb.save('D:\\mySpreadsheets\\books.xlsx')
    ws.cell(row=2)
def f2():

    global i, j, authors_list
    texts = open('common_text.txt','r',encoding='utf-8')
    authors = open('common_author.txt','r',encoding='utf-8')
    texts_list = texts.readlines()
    authors_list = authors.readlines()
    wb = load_workbook('D:\\mySpreadsheets\\books.xlsx')
    ws = wb.active
    sheet = wb['Лист1']
    
    #print(ws.cell(row=292,column=3).value)
    i = 4
    for x in range(i,292):
        ws.cell(row=i,column=3).value = texts_list[i-4]
        i += 1

    j = 4
    for y in range(j,292):
        ws.cell(row=j,column=4).value = authors_list[j-4]
        j += 1
       
    texts.close()
    authors.close()
    wb.save('D:\\mySpreadsheets\\books.xlsx')

def f3():

    global years_list
    year_file = open('common_year.txt','r')
    years_list = year_file.readlines()

    j = 0
    for x in years_list:
        years_list[j] = years_list[j][:x.index('\n')] 
        j += 1

    wb = load_workbook('D:\\mySpreadsheets\\books.xlsx')
    sheet = wb['Лист1']

    i = 4
    for x in range(i,292):
        #sheet.cell(row=i,column=5).value = years_list[i-4][:years_list[i-4].index('\n')]
        sheet.cell(row=i,column=5).value = years_list[i-4]
        i += 1

    year_file.close()
    wb.save('D:\\mySpreadsheets\\books.xlsx')
    
        

    
    
        
            
    
    
