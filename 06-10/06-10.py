def p():
    d = {}
    while True:
        print('введите свое имя(для выхода нажмите q):')
        b = input()
        if b == 'q':
            print(d)
            break
        else:
            print('введите номер:')
            a = int(input())
            d[b] = a
    return 0
p()