def f(day, month, year):
    '''
    Функция проверяет введённую дату на правдивость.
    '''

    monthbig = [1,3,5,7,8,10,12]
    monthsmall = [4,6,9,11]
    day_now = 19
    month_now = 10
    year_now = 2021
    if (year_now > 0 and month > 0 and day > 0 and month < 13 and day < 32) and (year <= year_now):
        if (year < year_now) or (year == year_now and month < month_now) or (year == year_now and month == month_now and day <= day_now):
            if day < 31 and month in monthsmall:
                return True
            elif day < 32 and month in monthbig:
                return True
            elif month == 2:
                if (day == 29 and year%4 == 0) or day < 29:
                    return "дата верна"
    return "дата неверна"

print(f(29, 2 ,2021))

# help(f)


# Help on function f in module __main__:

# f(d, m, y)
#     Функция проверяет введённую дату на правдивость.
