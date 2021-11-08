import datetime
while True:
    date_ = input('Input the date in standard format DD/MM/YY: ')
    if date_ == ('q'):
        print('goodbye!')
        quit()

    day , month, year = date_.split('/')

    d = int(day)
    m = int(month)
    y = int(year)

    def checkfake(d):
        if not(0 < d < 32):
            print('дата не корректна')
            quit()
    def checkmonth(m):
        if not(0 < m < 13):
            print('дата не корректна')
            quit()
    def checkyear(y):
        if not(y > 0):
            print('дата не корректна')
            quit()
    def february(d, m):
        if m == 2 and d == 29:
            n = input('Это високосный год?')
            if n != 'y':
                print('дата не корректна')
                quit()

    def April(d):
        if m==1 and 0 < d < 31:
            print('дата не корректна')
            quit()
    def June(d):
        if m==1 and 0 < d < 31:
            print('дата не корректна')
            quit()
    def September(d):
        if m==1 and 0 < d < 31:
            print('дата не корректна')
            quit()

    def November(d):
            if m == 1 and 0 < d < 31:
                print('дата не корректна')
            quit()


    checkfake(d)
    checkmonth(m)
    checkyear(y)
    february(d, m)

    print('дата корректна', day, month, year)