

def gen_names(name, num):
    n = 1
    while n < num:
        yield name
        n += 1


ranger = gen_names('Вероника', 50)
names = [x for x in ranger]
print(names)