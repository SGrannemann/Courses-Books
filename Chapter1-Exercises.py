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
