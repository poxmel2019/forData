import openpyxl as opx

texts1 = []
texts2 = []

def f():

    # Read txt file
    file = open('451.txt','r',encoding='utf-8')
    file_list = file.readlines()
    file.close()
    
    for x in file_list:
        try:
            texts1.append(x[x.index(' '):x.rindex('.')].strip())
        except ValueError:
            texts1.append(x[:x.rindex('.')].strip())            

    # Read excel file
    wb = opx.load_workbook('books.xlsx')
    sheet1 = wb['Лист1']
    _row = 4
    
    for x in range(4,724):
        texts2.append(sheet1.cell(row=_row,column=3).value)
        _row += 1

    wb.close()

    # Work with arrays
    i = 0
    for x in texts2:
        if x.endswith('\n'):
            texts2[i] = texts2[i][:-1]
        i += 1

    match_texts = []
    m_t = set(match_texts)
    count = 0
    for x in texts1:
        for y in texts2:
            if x == y:
                #match_texts.append(x)
                m_t.add(x)
                #count += 1

    #print(match_texts)
    #print(count)
    print(m_t)
    print(len(m_t))
    print(type(m_t))
            

    


    
 
    
    
        
    
