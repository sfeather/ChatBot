import nltk
from nltk.stem.lancaster import LancasterStemmer
import numpy
import tflearn
import tensorflow
import random
import json
# TODO: de scos warnings de aici si de lasat doar in gui.py
import warnings
warnings.filterwarnings("ignore")


stemmer = LancasterStemmer()

with open("Resources/learning.json") as file:
    data = json.load(file)

# print(data["intents"])

# words are tokens from "patterns" strings
words = []
# labels is equivalent to "tags"
labels = []
# docs is equivalent to "patterns"
# for this we use 2 lists called docs_a and docs_b
# docs_p is the "pattern" and docs_t is the "tag" of the pattern
# so that each entrance of docs_p corresponds to an entry of docs_t
docs_p = []
docs_t = []

# Reading from .json file
for intent in data["intents"]:
    for pattern in intent["patterns"]:
        tokenized_words = nltk.word_tokenize(pattern)
        words.extend(tokenized_words)
        docs_p.append(pattern)
        docs_t.append(intent["tag"])

    if intent["tag"] not in labels:
        labels.append(intent["tag"])

words = [stemmer.stem(w.lower()) for w in words]
# remove all the duplicates using set and then sort the newly created list
words = sorted(list(set(words)))
# print(labels)
print(words)
# print(docs_p)
# print(docs_t)
