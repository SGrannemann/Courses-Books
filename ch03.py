from nltk.tokenize import TreebankWordTokenizer
from collections import Counter
import nltk
nltk.download('stopwords', quiet=True)

sentence = """The faster Harry got to the store, the faster Harry, the faster, would get home."""

tokenizer = TreebankWordTokenizer()
tokens = tokenizer.tokenize(sentence.lower())

bag_of_words = Counter(tokens)

times_harry_appears = bag_of_words['harry']
num_unique_words = len(bag_of_words)
tf = times_harry_appears / num_unique_words

# beginning of the example with texts about kites
with open('kite_text.txt', 'r') as kite_ref:
    kite_text = kite_ref.read()

tokens = tokenizer.tokenize(kite_text.lower())
token_counts = Counter(tokens)

# ditch the stopwords
stopwords = nltk.corpus.stopwords.words('english')
tokens = [token for token in tokens if token not in stopwords]
kite_counts = Counter(tokens)
print(kite_counts)