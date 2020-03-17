def to_handle_text():
    
    file_address = 'common_list.txt'
    file = open(file_address,'r',encoding='utf-8')
    new_file = open('common_text.txt','w',encoding='utf-8')
    f = file.readlines()
    for x in f:
        if x == '\n': break
        try:
            print(x[x.index('"')+1:x.rindex('"')])
            new_file.write(x[x.index('"')+1:x.rindex('"')]+'\n')
        except ValueError:
            print(x[x.index('.')+2:x.index('-')])
            new_file.write(x[x.index('.')+2:x.index('-')]+'\n')

    file.close()
def to_handle_author():
    
    global f, authors, years
    file_address = 'common_list.txt'
    file = open(file_address,'r',encoding='utf-8')
    new_file = open('common_author.txt','w',encoding='utf-8')
    years_file = open('commont_year.txt','w',encoding='utf-8')
    f = file.readlines()
    i = 0
    authors = []
    years = []
    years_count = 0
    year20 = '2017'
    while (i < len(f)-1):
        if (i < 130):
            authors.append(f[i][f[i].index('(')+1:f[i].rindex('')])
            #print(authors[i][0:authors[i].index(')')])
            new_file.write(authors[i][0:authors[i].index(')')]+'\n')
            years.append('2016')
            years_file.write(years[i])
        else:
            if '(' not in f[i]:
                f[i] = f[i] + '(f)'
            authors.append(f[i][f[i].index(' - ')+2:f[i].index('(')].strip())
            years_count += 1
            if years_count >= 80:
                year20 = '2018'
            years.append(year20)
            years_file.write(years[i])
            #print(authors[i][:f[i].index('(')])
            new_file.write(authors[i][:f[i].index('(')]+'\n')    
        i += 1
    file.close()
    new_file.close()
    years_file.close()

    show_list(years)
    
def to_handle_00():
    global authors, x, texts, years, error_count, authors2
    file_address = '2000-2014.txt'
    file = open(file_address,'r',encoding='utf-8')
    file_list = file.readlines()
    years = []
    authors = [[],[],[],[]]
    authors2 = []
    texts = [[],[],[],[]]
    texts2 = []

    error_count = 0
    i = 0

    for x in file_list:
        try:
            texts2.append(x[x.index('"'):x.index('",')])
        except ValueError:
            try:
                texts2.append(x[x.index('"'):x.rindex('"')])
            except ValueError:
                continue

    show_list(texts2)
    for x in file_list:
        if x.startswith('20'): years.append(x)

    #show_list(years)
    
    i = 0
    error_count = 0
    for x in file_list:
        try:authors[i].append(x[x.index('.')+1:x.index('"')].strip())
        except ValueError:
            error_count += 1;
            if error_count in (4,7,10): i += 1
            continue
        

    show_list(authors)

def handle15():

    global x, authors
    file_address = '2015.txt'
    handled_file = open(file_address,'r',encoding='utf-8')
    file_list = handled_file.readlines()

    authors = []

    for x in file_list:
        if x == '(303)\n':break
        try:
            authors.append(x[x.index(')')+1:x.index('"')].strip())
        except ValueError:
            continue
        print(x)
    
    show_list(authors)

def to_handle_string():

    global string, quotes_pos, txts, odd, even, j, i
    string = '1) Антон Чехов "Который из трёх","Попрыгунья", "Хороший конец", "Один из многих", "Счастье", "Доктор", "Мститель", "Беглец", "У знакомых", "Интриги", "Ионыч"'
    i = 0
    quotes_pos = []
    txts = []
    for x in string:
        if x == '"': quotes_pos.append(i)
        i += 1
    print(quotes_pos)
    

    j = 0
    odd = []
    even = []
    
    for x in quotes_pos:
        if j % 2 == 0:
            odd.append(x)
        else:
            even.append(x)
        j += 1

    print(odd)
    print(even)

    j = 0
    for x in range(0,len(odd)):
        txts.append(string[odd[j]+1:even[j]])
        j += 1

    print(txts)
        
   
        



def show_list(some_list):
    for x in some_list:
        print(x)

    
        
    



        
    
    
        
    
        
    
    
