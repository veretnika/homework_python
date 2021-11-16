def f(day, month, year):
    '''
    Функция проверяет введённую дату на правдивость.
    '''
    if year > 0 and year < 2022:
        if month == 'январь' or month == 'март' or month == 'май' or month == 'июль' or month == 'август' or month == 'октябрь' or month == 'декабрь':
            if day > 0 and day < 32:
                print("Ваша дата существует")
            else:
                print('Дата не существует')
        elif month == 'апрель' or month == 'июнь' or month == 'сентябрь' or month == 'ноябрь': 
            if day > 0 and day < 31:
                print("Ваша дата существует")
            else:
                print('Дата не существует')
        elif month == 'февраль':
            if year % 4 == 0:
                if day > 0 and day < 30:
                    print("Ваша дата существует")
                else:
                    print('Дата не существует')
            else:
                    print('Дата не существует')
        else:
            print('Дата не существует')
    else:
        print('Дата не существует')

f(29,"февраль", 1988)
help(f)

# Help on function f in module __main__:

# f(day, month, year)
#     Функция проверяет введённую дату на правдивость.

