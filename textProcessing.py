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
        new_file.write(x.strip())   
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
    
    
        
    
