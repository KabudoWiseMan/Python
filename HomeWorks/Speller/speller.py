#!/usr/bin/env python
#
from string import whitespace, punctuation
from sys import argv

text = open(argv[2], 'r')
dictionary = open(argv[1], 'r')

dict_words = [line.strip() for line in dictionary.readlines()]
dictionary.close()
word = ''
row = 1
col = 1
for char in text.read():
    if char == '\n':
        if word  and word not in dict_words and word.isalpha():
            print("{0}, {1}    {2}".format(row, col, word))
        word = ''
        row += 1
        col = 1
    elif (char in whitespace or char == '\ufeff' or
          char != "\'" and char in punctuation):
        if word and word not in dict_words and word.isalpha():
            print("{0}, {1}    {2}".format(row, col, word))
        word = ''
        col += 1
    else:
        word += char.lower()

text.close()
