import math
file = open('0042_words.txt', 'r')
words = file.readline().split(',')
i = 1

def is_triangle_number(n):
    m = math.sqrt(8*n + 1)
    return m == int(m)


def is_triangle_word(word):
    sum_char = 0
    for char in word:
        sum_char += ord(char) - 96
    return is_triangle_number(sum_char)

sum_triangle_words = 0
for word in sorted(words):
    word_without_brackets = word.split('"')[1]
    if (is_triangle_word(word_without_brackets.lower())):
        sum_triangle_words += 1 
print sum_triangle_words



