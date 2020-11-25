from collections import Counter
import os

def onegrams(file):
    with open(file, 'r') as corpus:
        text = corpus.read()
        # .casefold() is better than .lower() here
        # https://www.programiz.com/python-programming/methods/string/casefold
        normalize = text.casefold()
        words = normalize.split(' ')
        count = Counter(words)
        return count

ngram_viewer = onegrams(os.path.join('data', 'corpus.txt'))
print(ngram_viewer.most_common(100))
