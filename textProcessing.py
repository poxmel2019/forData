import codecs


def op1():
    
    file_addresses = ['D:\\mySpreadsheets\\прочитанное\\2016.txt',
                      'D:\\mySpreadsheets\\прочитанное\\2017.txt',
                      'D:\\mySpreadsheets\\прочитанное\\2018.txt']

    #file_addresses = 'D:\\mySpreadsheets\\прочитанное\\2016.txt'

    i = 0
    for x in range(0,len(file_addresses)):
        open_read_file(file_addresses[i])
        i += 1

def open_read_file(file_addresses):
    f = open(file_addresses, 'r',encoding='utf-8')
    f1 = f.readlines()
    for x in f1:
        if x == '\n': break
        print(x)
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
    
    
