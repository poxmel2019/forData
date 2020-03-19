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
    authors = []
    authors2 = []
    texts = []
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

    global text, texts, x, y, authors, texts
    file_address = '2015.txt'
    
    handled_file = open(file_address,'r',encoding='utf-8')
    file_list = handled_file.readlines()

    authors = []
    texts = []
    text = []
    text_string = ''

    authors_texts = []

    # Append authors
    for x in file_list:
        if x == '(303)\n':break
        try:
            authors.append(x[x.index(')')+1:x.index('"')].strip())
        except ValueError:
            continue
        #print(x)

    # Append texts
    i = 0
    j = 0
    for y in file_list:
        if y == '(303)\n': break
        if i >= 3:
            if '"' in y:
                text = to_handle_string(y)
                texts.append(text)
                authors_texts.append(authors[j])
                j += 1
        
        i += 1
    #show_list(authors)
    #show_list(texts)
    show_list(authors_texts)
def to_handle_string(string):

    #global j, quotes_pos, txts, odd, even, x, k, z
    quotes_pos = []
    txts = []
    k = 0
    for z in string:
        if z == '"':
            quotes_pos.append(k)            
        k += 1
   
    odd = []
    even = []
    
    j = 0
    for z in quotes_pos:
        if j % 2 == 0:
            odd.append(quotes_pos[j])
        else:
            even.append(quotes_pos[j])
        j += 1
        
    i = 0
    for z in range(0,len(odd)):
        txts.append(string[odd[i]+1:even[i]])
        i += 1

    return txts

def show_list(some_list):
    for x in some_list:
        print(x)
def f15():
    
    #file_address = '2015.txt'
    
    handled_file = open(file_address,'r',encoding='utf-8')
    file_list = handled_file.readlines()

    texts = []
    authors = []
    text = []
    texts2 = []
    authors2 = []
    years = []

    i = 0
 
    for x in file_list:
        
        if x == '(303)\n': break
        if i >= 3:
            if '"' in x:
                text = to_handle_string(x)
                added_author = x[x.index(')')+1:x.index('"')].strip()
                for y in text:
                    texts2.append(y)
                    authors2.append(added_author)
                    
                authors.append(added_author)
                texts.append(text)
                years.append('2015')
                
                
        i += 1
def handle1214():

    file_addresses = ['2000-2011.txt','2012.txt','2013.txt','2014.txt']
    #handled_file = open(file_addresses[3],'r',encoding='utf-8')
    #file_list = handled_file.readlines()

    years = []
    authors = []
    texts = []
   
    data_list = []

    i = 0
    for x in range(i,len(file_addresses)):
        handled_file = open(file_addresses[i],'r',encoding='utf-8')
        file_list = handled_file.readlines()
        handled_file.close()
        data_list = handle_fl(file_list)
        j = 0
        for x in data_list:
            for y in x:
                if j == 0: texts.append(y)
                elif j == 1: authors.append(y)
                elif j == 2: years.append(y)
            j += 1
            
        
        i += 1

    data_list = [texts,authors,years]

    return data_list     
        

def handle_fl(file_list):

    authors = []
    authors2 = []
    texts = []
    texts2 = []
    text = []
    years = []
    years2 = []
    i = 0
    year = None
    for x in file_list:
        if i == 0:
            year = x
            years.append(year.lstrip('\n'))
        if '"' in x:
            added_author = x[x.index('.')+2:x.index('"')].strip()
            authors.append(added_author)
            text = to_handle_string(x)
            for y in text:
                texts2.append(y)
                years2.append(year[:len(year)-1])
                authors2.append(added_author)
            texts.append(text)
        i += 1

    data_list = [texts2,authors2,years2]
    return data_list
    
  
    
    



    




    
    



        
    
    
        
    
        
    
    
