import numpy
import json


def write(synapse_1,synapse_0,layer,parent,set):
    synapse_file = "synapses"+str(layer)+str(parent)+".json"
    synapse = {'synapse0':synapse_0 ,'synapse1':synapse_1,
               'word': set
               }
    with open(synapse_file, 'w') as outfile:
        json.dump(synapse, outfile, indent=4, sort_keys=True)

def read(layer,parent):
    synapse_file = "synapses"+str(layer)+str(parent)+".json"
    with open(synapse_file) as data_file:
        synapse = json.load(data_file)
        synapse_0 = numpy.asarray(synapse['synapse0'])
        synapse_1 = numpy.asarray(synapse['synapse1'])
        words =  numpy.asarray(synapse['word'])
    return synapse_1,synapse_0,words

