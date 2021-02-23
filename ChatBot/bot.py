import nltk
from nltk.stem.lancaster import LancasterStemmer
import numpy
import tflearn
from tensorflow.python.framework import ops
import random
import json
import pickle
# TODO: de scos warnings de aici si de lasat doar in gui.py
import warnings

warnings.filterwarnings("ignore")

stemmer = LancasterStemmer()

with open("Resources/learning.json") as file:
    data = json.load(file)

# Creating a pickle file to save the lists (words, labels, training and output)
try:
    with open("Resources/essential_lists.pickle", "rb") as f:
        words, labels, training, output = pickle.load(f)
except Exception:
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
    with open("Resources/essential_lists.pickle", "wb") as f:
        pickle.dump((words, labels, training, output), f)

# Creating the model using tensorflow
ops.reset_default_graph()

net = tflearn.input_data(shape=[None, len(training[0])])
# adding a fully connected layer to our neural network (net) - 8 neurons for that "hidden layer"
net = tflearn.fully_connected(net, 8)
# new "hidden layer" with 8 neurons
net = tflearn.fully_connected(net, 8)
# activation softmax to get probabilities for each output
net = tflearn.fully_connected(net, len(output[0]), activation="softmax")
net = tflearn.regression(net)

model = tflearn.DNN(net)

try:
    model.load("Resources/model_files/model.tflearn")
except Exception:
    model.fit(training, output, n_epoch=1000, batch_size=8, show_metric=True)
    model.save("Resources/model_files/model.tflearn")


def bag_of_words(s, new_words):
    new_bag = [0 for _ in range(len(new_words))]

    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]

    for se in s_words:
        for i, w in enumerate(words):
            # if the current word is equal to the word in our sentence
            if w == se:
                new_bag[i] = 1

    return numpy.array(new_bag)


def chat():
    print("Start talking w the bot! (type quit to stop)")
    while True:
        inp = input("You: ")
        if inp.lower() == "quit":
            break

        results = model.predict([bag_of_words(inp, words)])
        # get the index of the greatest value in the "results" list
        results_index = numpy.argmax(results)
        tag = labels[results_index]
        for intents in data["intents"]:
            if intents['tag'] == tag:
                responses = intents['responses']

        print(random.choice(responses))


chat()
