from chatbot.models import train
import nltk
from nltk.stem.lancaster import LancasterStemmer
import os
import json
import datetime
stemmer = LancasterStemmer()


def abc(sen_id,sentence,class_id,layer_id):
    obj1 = train(sen_id=sen_id, sentence=sentence, class_id=class_id, layer_id=layer_id);
    obj1.save()

def makeBags():
        all_sentences = train.objects.all()
        sentences=[]
        classes = []
        all_words = []
        ignore_words = ['?']
        for sent in all_sentences:
             sentences.append(sent.sentence)
             if(sent.class_id not in classes):
                     classes.append(sent.class_id)

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
        all_words = list(set(all_words))

        # remove duplicates
        classes = list(set(classes))
        #return words
        # create our training data
        training_set = []
        output_set = []
        # create an empty array for our output
        output_empty = [0] * len(classes)

        # training set, bag of words for each sentence
        for sent in all_sentences:
                # initialize our bag of words
                word_bag = []
                # list of tokenized words for the pattern
                # stem each word
                pattern_words = [stemmer.stem(word.lower()) for word in sent]
                # create our bag of words array
                for w in all_words:
                        word_bag.append(1) if w in pattern_words else word_bag.append(0)

                training_set.append(word_bag)
                # output is a '0' for each tag and '1' for current tag

        # sample training/output
        return training_set