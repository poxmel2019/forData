import codecs


def op1():
    global new_file
    file_addresses = ['D:\\mySpreadsheets\\прочитанное\\2016.txt',
                      'D:\\mySpreadsheets\\прочитанное\\2017.txt',
                      'D:\\mySpreadsheets\\прочитанное\\2018.txt']

    #file_addresses = 'D:\\mySpreadsheets\\прочитанное\\2016.txt'

    new_file = open('common_list.txt','w',encoding='utf-8')
    i = 0
    for x in range(0,len(file_addresses)):
        open_read_file(file_addresses[i],new_file)
        i += 1
        
    new_file.close()
    
def open_read_file(file_addresses,new_file):
    f = open(file_addresses, 'r',encoding='utf-8')
   
    f1 = f.readlines()
    
    i = 0
    for x in f1:
        
        new_file.write(x)
        print(x)
        if x == '\n': break
    #new_file.close()
    f.close()


def op():
    global x
    
    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    # 'D:\\mySpreadsheets\\прочитанное\\2018.txt'
    file_addresses = 'D:\\mySpreadsheets\\прочитанное\\2018.txt'
    f = open(file_addresses, 'r',encoding='utf-8')
    f1 = f.readlines()
    for x in f1:
        print(x[3:])
        if x == '\n': break
    f.close()
    
def handle_new_file():

    nums = []
    file = open('2018.txt','r',encoding='utf-8')
    new_file_address = 'compressList.txt'
    new_file = open(new_file_address,'w',encoding='utf-8')
    f = file.readlines()

    num = ''
    for x in f:
        if x == '\n':break
        new_file.write(x)   
        print(x)
    #print(nums)
        
    new_file.close()
    file.close()
    open_read_close_file(new_file_address)
    #print(new_file)
    
def open_read_close_file(some_file):

    file = open(some_file,'r',encoding='utf-8')
    f = file.readlines()
    for x in f:
        print(x,end='\n')
def f():
    
    word = '1. "Name of novel" - (author)'
    string = '"Холодное сердце" - Вильгельм Гауф'
    string3 = '1. Сообщение о моей смерти - Марк Твен (1)'
    novel = ''
    author = ''
    #print(word)
    #print(word.index('.'))
    #print(word.index(' '))
    #novel = word[word.index('"')+1:word.rindex('"')]
    #author = word[word.index('(')+1:word.rindex(')')]
    #novel2 =  string[string.index('"')+1:string.rindex('"')]
    novel3 = string3[string3.index('.')+2:string3.index('-')]
    novel3 = string3[string3.index('-')+2:string3.rindex('')]
    #author2 = string[string.index('')+1:string.index('\n')]
    
    #print(novel)
    #print(author)
    #print(novel2)
    #print(author2)
    print(novel3)

def handle18():

    file_address = '2018.txt'
    file = open(file_address,'r',encoding='utf-8')
    f = file.readlines()
    for x in f:
        if x == '\n': break
        print(x[x.index('.')+2:x.index('-')])
        
    file.close
def handle17():

    file_address = '2017.txt'
    file = open(file_address,'r',encoding='utf-8')
    f = file.readlines()
    for x in f:
        if x == '\n': break
        print(x[x.index('"')+1:x.rindex('"')])
        
    file.close
def handle16():

    file_address = '2018.txt'
    file = open(file_address,'r',encoding='utf-8')
    f = file.readlines()
    for x in f:
        if x == '\n': break
        print(x[x.index('"')+1:x.rindex('"')])
        
    file.close
def handleText():

    file_address = 'common_list.txt'
    file = open(file_address,'r',encoding='utf-8')
    new_file = open('common_text.txt','w',encoding='utf-8')
    f = file.readlines()
    #try:
    for x in f:
        if x == '\n': break
        try:
            print(x[x.index('"')+1:x.rindex('"')])
            new_file.write(x[x.index('"')+1:x.rindex('"')]+'\n')
        except ValueError:
            print(x[x.index('.')+2:x.index('-')])
            new_file.write(x[x.index('.')+2:x.index('-')]+'\n')
    #file.close()
    #except ValueError:
    #    for x in f:
    #        if x == '\n': break
    #        print(x[x.index('.')+2:x.index('-')])
    file.close()
def handleCL2():

    file_address = '2016.txt'
    file = open(file_address,'r',encoding='utf-8')
    f = file.readlines()
    #try:
    for x in f:
        if x == '\n': break
        try:
            print(x[x.index('(')+1:x.rindex(')')])
        except ValueError:
            print(x[x.index('-')+2:x.rindex('')])
    #file.close()
    #except ValueError:
    #    for x in f:
    #        if x == '\n': break
    #        print(x[x.index('.')+2:x.index('-')])
    file.close()
    
