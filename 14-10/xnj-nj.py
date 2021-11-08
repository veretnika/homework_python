import operator
import string

str_ = 'Parity of a number refers to whether it contains an odd or even number of 1-bits. The number has “odd parity”, if it contains odd number of 1-bits and is “even parity” if it contains even number of 1-bits. Main idea of the below solution is – Loop while n is not 0 and in loop unset one of the set bits and invert parity.Accordingly, there are two variants of parity bits: even parity bit and odd parity bit. In the case of even parity, for a given set of bits, the occurrences of bits whose value is 1 are counted. If that count is odd, the parity bit value is set to 1, making the total count of occurrences of 1s in the whole set (including the parity bit) an even number. If the count of 1s in a given set of bits is already even, the parity bits value is 0. In the case of odd parity, the coding is reversed. For a given set of bits, if the count of bits with a value of 1 is even, the parity bit value is set to 1 making the total count of 1s in the whole set (including the parity bit) an odd number. If the count of bits with a value of 1 is odd, the count is already odd so the parity bits value is 0.'

b = str_.split()


def clean_text(words_list):
    result = []
    for word in words_list:
        new_word = ''
        has_punch_mark = False
        for ch in string.punctuation:
            if ch in word:
                has_punch_mark = True
                pos = word.find(ch)
                if pos == len(word) - 1:
                    new_word = word[:pos]
                else:
                    new_word = word[:pos] + word[pos + 1:]
        if not has_punch_mark:
               new_word = word
               result.append(new_word.lower())
    return result
a = clean_text(b)
def count_words(words):
       words_set = set(words)
       words_dict = {}
       for word in words_set:
              words_dict[word] = words.count(word)
       return words_dict

c = sorted(count_words(a).items(), key=lambda x : x[1], reverse=True)
d = list(c)[:10]
for word, num in d:
    print(word, ': ', num)