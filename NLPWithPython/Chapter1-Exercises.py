# I skipped some exercises because they use very basic Python functionality
# i am already familiar with

import nltk
from nltk.book import *

# Exercise 4: How many words are in text2 ? how many distinct words?
words = len(text2)
print(words)
distinct_words = len(set(text2))
print(distinct_words)

# Exercise 6: Produce a dispersion plot of the four main protagonists in Sense and Sensibility
# This is text 2
#text2.dispersion_plot(['Elinor', 'Marianne', 'Edward', 'Willoughby'])

# Exercise 7: Find the collocations in text5
text5.collocations()

# Exercise 11: Make multiple lists of words. What is the relationship between
# len(list1 + list2) and len(list1) + len(list2)?
string1 = "Roses are red, this poem is choppy, passing by value is passing by copy."
string2 = "Niemand hat die Absicht eine Mauer zu bauen."

list1 = string1.split()
list2 = string2.split()
print(list1)
print(list2)
print(len(list1 + list2))
print(len(list1) + len(list2))

# Exercise 14: Find all indexes of the occurrences of 'the' in sent3
indices = [i for i, v in enumerate(sent3) if v == 'the']

# Exercise 15: Find all words in text5 that start with 'b' and
# sort them alphabetically
words_starting_with_b = sorted([word for word in set(text5) if word.startswith('b')])

# Exercise 21: Extract last two words of text2
text2[-2:]

# Exercise 22: find all 4 letter words in text5 and use a frequency distribution
# to show them in order of decreasing frequency
max_four = [word for word in text5 if len(word) == 4]
fdist = FreqDist(max_four)

# Exercise 23: use a combination of for and if statements to print all uppercase
# words of text6

for word in text6:
    if word.isupper():
        print(word)

# Exercise 24: Write expressions for finding all words in text6 that meet
# the conditions shown below:
# ending in ize:
ize = [word for word in text6 if words.endswith('ize')]

# containing the letter z
z = [word for word in text6 if 'z' in word]

# containing the sequence of letters pt
pt = [word for word in text6 if 'pt' in word]

# title case
text6_titleCaseWords = [word for word in text6 if word.istitle()]

# Exercise 25: print all words beginning with sh in the list sent.
# print all words longer than four characters.

sent = ['she', 'sells', 'sea', 'shells', 'by', 'the', 'sea', 'shore']
# begins with sh
for word in sent:
    if word.startswith('sh'):
        print(word)

# longer than 4 characters
for word in sent:
    if len(word) > 4:
        print(word)

# or bundled together:
for word in sent:
    if word.startswith('sh') or len(word) > 4:
        print(word)

# Exercise 27: Define a function vocab_size(text) that returns the vocabulary
# size of the text

def vocab_size(text):
    return len(set(text))


# Exercise 28: Define a function percent(word, text) that calculates how often
# a given word occurs in a text as a percentage.

def percent(word, text):
    return 100 * text.count(word) / len(text)
