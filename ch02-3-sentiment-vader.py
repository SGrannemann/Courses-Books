from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
sa = SentimentIntensityAnalyzer()

corpus = ['Absolutely perfect! Love it! :-) :-) :-)', 'Horrible! Completely useless. :(', 'It was OK. Some good and some bad things.']

for doc in corpus:
    scores = sa.polarity_scores(doc)
    print('{:+}: {}'.format(scores['compound'], doc))