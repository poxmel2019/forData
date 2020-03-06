import codecs

def op():
    # 'D:\\mySpreadsheets\\прочитанное\\2018.txt'
    file_address = 'D:\\mySpreadsheets\\прочитанное\\2000 - 2014.txt'
    try:
        f1 = open(file_address, 'r',encoding='utf-16 le')
        text = f1.readline()
    except UnicodeDecodeError:
        f1 = open(file_address, 'r',encoding='ansi')
        text = f1.readline()
    print(text)
