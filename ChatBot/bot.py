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
        docs_p.append(tokenized_words)
        docs_t.append(intent["tag"])

    if intent["tag"] not in labels:
        labels.append(intent["tag"])

words = [stemmer.stem(w.lower()) for w in words if w not in "?"]
# remove all the duplicates using set and then sort the newly created list
words = sorted(list(set(words)))
# sort the labels as well
labels = sorted(labels)

# create a frequency words vector 0 = !exists and 1 = exists (bag of words)
training = []
output = []
out_empty = [0 for _ in range(len(labels))]

# actually creating it (the bag of words)
for x, doc in enumerate(docs_p):
    bag = []
    tokenized_words = [stemmer.stem(w) for w in doc]
    for w in words:
        if w in tokenized_words:
            bag.append(1)
        else:
            bag.append(0)

    output_row = out_empty[:]
    output_row[labels.index(docs_t[x])] = 1

    training.append(bag)
    output.append(output_row)

training = numpy.array(training)
output = numpy.array(output)

# Creating the model using tensorflow

net = tflearn.input_data(shape=[None, len(training[0])])
# adding a fully connected layer to our neural network (net) - 8 neurons for that "hidden layer"
net = tflearn.fully_connected(net, 8)
# new "hidden layer" with 8 neurons
net = tflearn.fully_connected(net, 8)
# activation softmax to get probabilities for each output
net = tflearn.fully_connected(net, len(output[0]), activation="softmax")
net = tflearn.regression(net)

model = tflearn.DNN(net)

# print(labels)
print(words)
# print(docs_p)
# print(docs_t)
