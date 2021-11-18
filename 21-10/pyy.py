import sqlite3
from os import listdir
from os.path import isfile, join

current_db = ''
def call(user_a):
    if user_a == '1':
        print('DB`s list: ')
        ld = listdir("/home/sirius/homework_python/21-10/Databases/")
        print(ld)
        onlyfiles = [f for f in ld if isfile(join("/home/sirius/homework_python/21-10/Databases/", f))]
        [print(i + 1, ':', onlyfiles) for i, onlyfiles in zip(range(len(onlyfiles)), onlyfiles)]
        global p
        p = input('Enter the name of the DB: ')
        print('Or press q for Exit')
        if p == 'q':
            print('Sayonara!')
            quit()
        else:
            global current_db
            try:
                current_db = ld[int(p) - 1]
            except Exception as err:
                print(err)

def showall():
    sqliteConnection = sqlite3.connect('Databases/{}'.format(current_db))
    cursor = sqliteConnection.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    rows = (cursor.fetchall())
    print('Tables list:')
    [[print(element) for element in row] for row in rows]
    sqliteConnection.close()

def table_select():
    sqliteConnection = sqlite3.connect('Databases/{}'.format(current_db))
    cursor = sqliteConnection.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    rows = (cursor.fetchall())
    print('Tables list:')
    [[print(element) for element in row] for row in rows]
    global t
    t = input('Enter the name of the table to work with: ')
    sqliteConnection.close()

def delete():
    sqliteConnection = sqlite3.connect('Databases/{}'.format(current_db))
    cursor = sqliteConnection.cursor()
    de = input('Enter ID you want to purge: ')
    delete2 = """DELETE from {} where id = {};""".format(t, de)
    cursor.execute(delete2)
    sqliteConnection.commit()
    sqliteConnection.close()

def edit(id, brand, value):
        sqliteConnection = sqlite3.connect('Databases/{}'.format(current_db))
        cursor = sqliteConnection.cursor()
    #sqlite_update_query = """Update middle set id = %d and brand = "%s" where value = "%s\""""
        sqlite_update_query = """Update {} set value = "{:s}", brand = "{:s}" where id = {:d}""".format(t, value, brand, id)
        columnValues = value, brand, id
        cursor.execute(sqlite_update_query)
        sqliteConnection.commit()
        print("Updated successfully")
        sqliteConnection.commit()
        cursor.close()
def readSqliteTable():
        sqliteConnection = sqlite3.connect('Databases/{}'.format(current_db))
        cursor = sqliteConnection.cursor()
        sqlite_select_query = """SELECT * from {}""".format(t)
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        print("Total rows are:  ", len(records))
        for row in records:
            print("ID: ", row[0])
            print("frut: ", row[1])
            print("color: ", row[2])
        cursor.close()
        sqliteConnection.close()
def choice():
    print('1.Start working with DB', '\n2.Exit')
    user_a = input()
    if user_a == '1':
        call(user_a)
    if user_a == 2:
        print('пока!')
        quit()
def operations():
    print('You`re working with:', p)
    print('Table:', t)
    print('1.Edit','\n2.Show','\n3.Change Table','\n4.Switch DB','\n5.Show table','\n6.Delete ID','\n0.Exit')
    user_a = input()
    if user_a == '1':
        print('Enter ID:')
        id = int(input('Your ID: '))
        print('Enter frut: ')
        frut = input('Your frut: ')
        print('Enter Value:')
        color = input('Your color: ')
        edit(id, frut, color)
        readSqliteTable()
    if user_a == '2':
        readSqliteTable()
    if user_a == '3':
        table_select()
    if user_a == '4':
        user_a = '1'
        call(user_a)
    if user_a == '5':
        showall()
    if user_a == '6':
        delete()
    if user_a == '0':
        print('спасибо!')
        quit()

choice()
table_select()
while True:
    operations()