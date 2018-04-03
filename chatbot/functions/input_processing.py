import numpy
import time
from chatbot.models import  train, sets
import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()
#............remove this
def get_all_words(layer,parent):
    ignore_words =['?'] #add more into this
    all_words = []
    all_sentences = train.objects.all()
    layer_ids=[]
    for sent in all_sentences:
        layer_ids.append(sent.set_id.layer_id_of.layer_id)
        if(sent.set_id.layer_id_of.layer_id == layer and sent.set_id.parent_id == parent):
            sentence =nltk.word_tokenize(sent.sentence)
            all_words.extend(sentence)

    words = [stemmer.stem(w.lower()) for w in all_words if w not in ignore_words]
    words = list(set(words))
    return words

def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [stemmer.stem(word.lower()) for word in sentence_words]
    return sentence_words
    #tokenize the sentence and give tokenized set of words.


def give_word_bag(sentence, words):
    sentence_words = clean_up_sentence(sentence)
    # bag of words
    bag = [0] * len(words)
    for s in sentence_words:
        for i, w in enumerate(words):
            if w == s:
                bag[i] = 1

    return (numpy.array(bag),sentence_words)