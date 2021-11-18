import string

def text(text):
    d = {}
    text = text.lower()
    text2 = text.split()
    for value in set(text2):
        d[value] = text2.count(value)
    top = sorted(d.items(), key=lambda x: x[1], reverse=True)
    print("Топ-10 слов:")
    for i in range(10):
        print(str(i+1) + ". Слово " + str(top[i][0]) + " повторяется " + str(top[i][1]) + " раз(а)")
    return d


f = open('top_words.txt', 'r')
text1 = ' '.join(f.readlines())
text(text1)
f.close()