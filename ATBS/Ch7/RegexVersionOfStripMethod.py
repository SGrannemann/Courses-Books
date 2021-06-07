#!/usr/bin/env python3

import re
word = '    test   '
word2 = 'aaatestaaa'


def regExStrip(word, symbol=None):
    print(word)
    string = re.escape(symbol) if symbol else r'\s'
    stripRegExObject = re.compile(r'^[{0}]*|[{0}]*$'.format(string))
    return stripRegExObject.sub(r'', word)


stripped_word = regExStrip(word)
print(stripped_word)

stripped_word_2 = regExStrip(word2, 'a')
print(stripped_word_2)
