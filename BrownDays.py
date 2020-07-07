import nltk
from nltk.corpus import brown

categories = ['news', 'romance']
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday',
        'Sunday']

cfd_days = nltk.ConditionalFreqDist((category, word)
                                    for category in categories
                                    for word in brown.words(categories=category)
                                    if word in days)

cfd_days.tabulate(samples=days)
cfd_days.plot()
