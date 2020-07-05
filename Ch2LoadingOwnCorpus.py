from nltk.corpus import PlaintextCorpusReader

corpus_root = '../../NLTKCorpusTest'
wordlists = PlaintextCorpusReader(corpus_root, '.*')
print(wordlists.fileids())
for file in wordlists.fileids():
    wholeFile = ' '.join(wordlists.words(file))
    print(wholeFile)
