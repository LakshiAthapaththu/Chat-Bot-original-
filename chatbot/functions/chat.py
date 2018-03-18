import numpy

from chatbot.functions.general_functions import sigmoid
from .input_processing import give_word_bag,get_all_words
from .trainData import trainData
def think(sentence, layer,parent,synapse_0,synapse_1):
    x = give_word_bag(sentence.lower(), get_all_words(layer,parent),layer,parent)
    l0 = numpy.array(x)
    # matrix multiplication of input and hidden layer

    l1 = sigmoid(numpy.dot(x, synapse_0))
    # output layer
    l2 = sigmoid(numpy.dot(l1, synapse_1))
    return l2

def clasify(sentence,layer,parent,synapse_0,synapse_1,classes):
    l2 = think(sentence,layer,parent,synapse_0,synapse_1)
    ERROR_THRESHOLD = 0.2
    results = [[i, r] for i, r in enumerate(l2) if r > ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)
    return_results = [[classes[r[0]], r[1]] for r in results]
    return l2,results,return_results
