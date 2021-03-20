from nltk.tokenize import TreebankWordTokenizer
from collections import Counter, OrderedDict
import nltk
import copy
import math

nltk.download('stopwords', quiet=True)

sentence = """The faster Harry got to the store, the faster and fasterHarry, the faster, would get home."""

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

# vectorize the counts

document_vector = []
doc_length = len(tokens)
for key, value in kite_counts.most_common():
    document_vector.append(value / doc_length)

# use more than one sentence/ document
# in this case, our lexicon is as large as the set of unique tokens in all documents
# and the size of the lexicon equals our dimensions

docs = ["""The faster Harry got to the store, the faster and faster Harry would get home."""]

docs.append('Harry is hairy and faster than Jill.')
docs.append('Jill is not as hairy as Harry.')

doc_tokens = []
for doc in docs:
    doc_tokens += [sorted(tokenizer.tokenize(doc.lower()))]

all_doc_tokens = sum(doc_tokens, [])
lexicon = sorted(set(all_doc_tokens))

# we make vectors with all zeros to get started
zero_vector = OrderedDict((token, 0) for token in lexicon)

doc_vectors = []
for doc in docs:
    vec = copy.copy(zero_vector)
    tokens = tokenizer.tokenize(doc.lower())
    token_counts = Counter(tokens)
    for key, value in token_counts.items():
        vec[key] = value / len(lexicon)


# simple variant of topic modeling
with open('kite_text.txt', 'r') as kite_ref:
    kite_text = kite_ref.read()
with open('kite_history.txt', 'r') as kite_ref:
    kite_history = kite_ref.read()

kite_intro = kite_text.lower()
intro_tokens = tokenizer.tokenize(kite_intro)
kite_history = kite_history.lower()
history_tokens = tokenizer.tokenize(kite_history)
intro_total = len(intro_tokens)
history_total = len(history_tokens)

intro_tf = {}
history_tf = {}
intro_counts = Counter(intro_tokens)
intro_tf['kite'] = intro_counts['kite'] / intro_total
history_counts = Counter(history_tokens)
history_tf['kite'] = history_counts['kite'] / history_total
# the counts of kite alone are not really a good measure


intro_tf['and'] = intro_counts['and'] / intro_total
history_tf['and'] = history_counts['and'] / history_total
# the documents are as much about and as they are about kite. that is not working well up to now

# maybe the inverse document frequency can help?

# find the number of documents containing the words that interest us for now
num_docs_containing_and = 0
for doc in [intro_tokens, history_tokens]:
    if 'and' in doc:
        num_docs_containing_and += 1

num_docs_containing_kite = 0
for doc in [intro_tokens, history_tokens]:
    if 'kite' in doc:
        num_docs_containing_kite += 1

num_docs_containing_china = 0
for doc in [intro_tokens, history_tokens]:
    if 'china' in doc:
        num_docs_containing_china += 1

intro_tf['china'] = intro_counts['china'] / intro_total
history_tf['china'] = history_counts['china'] / history_total

# calculate the idf scores
num_docs = 2
intro_idf = {}
history_idf = {}
intro_idf['and'] = num_docs / num_docs_containing_and
intro_idf['kite'] = num_docs / num_docs_containing_kite
intro_idf['china'] = num_docs / num_docs_containing_china
history_idf['and'] = num_docs / num_docs_containing_and
history_idf['kite'] = num_docs / num_docs_containing_kite
history_idf['china'] = num_docs / num_docs_containing_china


#combine tf and idf scores
intro_tfidf = {}
intro_tfidf['and'] = intro_tf['and'] * intro_idf['and']
intro_tfidf['kite'] = intro_tf['kite'] * intro_idf['kite']
intro_tfidf['china'] = intro_tf['china'] * intro_idf['china']

history_tfidf = {}
history_tfidf['and'] = history_tf['and'] * history_idf['and']
history_tfidf['kite'] = history_tf['kite'] * history_idf['kite']
history_tfidf['china'] = history_tf['china'] * history_idf['china']

