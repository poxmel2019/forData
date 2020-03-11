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
    
    global f, authors
    file_address = 'common_list.txt'
    file = open(file_address,'r',encoding='utf-8')
    new_file = open('common_author.txt','w',encoding='utf-8')
    f = file.readlines()
    i = 0
    authors = []
    while (i < len(f)-1):
        if (i < 130):
            authors.append(f[i][f[i].index('(')+1:f[i].rindex('')])
            print(authors[i][0:authors[i].index(')')])
            new_file.write(authors[i][0:authors[i].index(')')]+'\n')
        else:
            if '(' not in f[i]:
                f[i] = f[i] + '(f)'
            authors.append(f[i][f[i].index(' - ')+2:f[i].index('(')].strip())
            print(authors[i][:f[i].index('(')])
            new_file.write(authors[i][:f[i].index('(')]+'\n')    
        i += 1
    file.close()
    new_file.close()
    



        
    
    
        
    
        
    
    
