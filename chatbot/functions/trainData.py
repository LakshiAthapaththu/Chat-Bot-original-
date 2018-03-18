from chatbot.models import train,sets
import nltk
from nltk.stem.lancaster import LancasterStemmer
import os
import json
import datetime
import numpy
stemmer = LancasterStemmer()
from chatbot.functions.general_functions import derivative,sigmoid

def makeBags(setObj):
    #setObject = sets.objects.filter(set_id=set_id)
    parent = setObj.parent_id
    layer = setObj.layer_id_of
    fetched_sentences = train.objects.all()
    classes = []
    all_sets = sets.objects.all()
    class_bags=[]
    for setobj in all_sets:
        if(setobj.layer_id_of == layer and setobj.parent_id == parent):
            classes.append(setobj)
    all_sentences = []
    for sentence_obj in fetched_sentences:
        setobject = sentence_obj.set_id
        if(setobject.parent_id == parent and setobject.layer_id_of == layer):
            all_sentences.append(sentence_obj)
    sentences = []
    all_words = []
    ignore_words = ['?']
    for sent in all_sentences:
        sentences.append(sent.sentence)

    # loop through each sentence in our training data
    for pattern in sentences:
        # tokenize each word in the sentence
        w = nltk.word_tokenize(pattern)
        # add to our words list
        all_words.extend(w)
        # add to documents in our corpus
        # add to our classes list

    # stem and lower each word and remove duplicates
    words = [stemmer.stem(w.lower()) for w in all_words if w not in ignore_words]
    words = list(set(words))

    # remove duplicates
    classes = list(set(classes))
    # return words
    # create our training data
    training_set = []
    output_set = []
    # create an empty array for our output
    #output_empty = [0] * len(classes)
    # training set, bag of words for each sentence
    for sent in all_sentences:
        # initialize our bag of words
        relavant_set_obj_all = sets.objects.filter(set_id=sent.set_id.set_id)
        relavant_set_obj = ''
        for o in relavant_set_obj_all:
            relavant_set_obj = o
        word_bag = []
        class_bag = []
        # list of tokenized words for the pattern
        # stem each word
        pattern_words = nltk.word_tokenize(sent.sentence)
        sentence_words = [stemmer.stem(w.lower()) for w in pattern_words if w not in ignore_words]
        # stem each word
        # create our bag of words array
        for w in words:
            word_bag.append(1) if w in sentence_words else word_bag.append(0)
        for clas in classes:
            if(clas.class_id_of == relavant_set_obj.class_id_of):
                class_bag.append(1)
            else:
                class_bag.append(0)
        classnames =[]
        for i in classes:
            classnames.append(i.class_id_of.class_id)
        training_set.append(word_bag)
        class_bags.append(class_bag)
        #training_set.append(classnames)
        #training_set.append(all_words)
        TrainObj = train.objects.filter(sentence_id = sent.sentence_id)
        TrainObj.update(word_bag = word_bag)
        TrainObj.update(class_bag = class_bag)
    # sample training/output
    x=trainData(setobj,classnames,training_set,class_bags)
    return x

def trainData(setObj,classes,trainingset,class_bags,hidden_neurons=10, alpha=1, epochs=500,dropout_percent=0.5):
    numpy.random.seed(1)

    #randomly select weights
    last_mean_error = 1
    # randomly initialize our weights with mean 0
    synapse_0 = 2 * numpy.random.random((len(trainingset[0]), hidden_neurons)) - 1
    #matrix with 16 rows(number of words) 10 colomns (middle layer nuerons)
    synapse_1 = 2 * numpy.random.random((hidden_neurons, len(classes))) - 1

    prev_synapse_0_weight_update = numpy.zeros_like(synapse_0)
    prev_synapse_1_weight_update = numpy.zeros_like(synapse_1)
    #contain all 0s
    synapse_0_direction_count = numpy.zeros_like(synapse_0)
    synapse_1_direction_count = numpy.zeros_like(synapse_1)
    #contain all 0s
    synapse_0_direction_count = numpy.zeros_like(synapse_0)
    synapse_1_direction_count = numpy.zeros_like(synapse_1)
    for j in iter(range(epochs + 1)):
        layer_0 = numpy.array(trainingset)
        layer_1 = sigmoid(numpy.dot(layer_0, synapse_0))
        layer_2 = sigmoid(numpy.dot(layer_1, synapse_1))
        layer_2_error = numpy.array(class_bags) - layer_2
        #get the error
        if numpy.mean(numpy.abs(layer_2_error)) < last_mean_error:
            #print("delta after " + str(j) + " iterations:" + str(np.mean(np.abs(layer_2_error))))
            last_mean_error = numpy.mean(numpy.abs(layer_2_error))
        else:
            #print("break:", np.mean(np.abs(layer_2_error)), ">", last_mean_error)
            break

        # in what direction is the target value?
        # were we really sure? if so, don't change too much.
        layer_2_delta = layer_2_error * derivative(layer_2)
        # how much did each l1 value contribute to the l2 error (according to the weights)?
        layer_1_error = layer_2_delta.dot(synapse_1.transpose())
        # in what direction is the target l1?
        # were we really sure? if so, don't change too much.
        layer_1_delta = layer_1_error * derivative(layer_1)
        synapse_1_weight_update = (layer_1.T.dot(layer_2_delta))
        synapse_0_weight_update = (layer_0.T.dot(layer_1_delta))
        if (j > 0):
            synapse_0_direction_count += numpy.abs(
                ((synapse_0_weight_update > 0) + 0) - ((prev_synapse_0_weight_update > 0) + 0))
            synapse_1_direction_count += numpy.abs(
                ((synapse_1_weight_update > 0) + 0) - ((prev_synapse_1_weight_update > 0) + 0))

        synapse_1 += alpha * synapse_1_weight_update
        synapse_0 += alpha * synapse_0_weight_update

        prev_synapse_0_weight_update = synapse_0_weight_update
        prev_synapse_1_weight_update = synapse_1_weight_update
    synapse0=synapse_0.tolist()
    synapse1=synapse_1.tolist()

    return synapse0,synapse1
