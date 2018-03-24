import numpy
import json


def write(synapse_1,synapse_0):
    synapse_file = "synapses.json"
    synapse = {'synapse0':synapse_0 ,'synapse1':synapse_1

               }
    with open(synapse_file, 'w') as outfile:
        json.dump(synapse, outfile, indent=4, sort_keys=True)

def read():
    synapse_file = 'synapses.json'
    with open(synapse_file) as data_file:
        synapse = json.load(data_file)
        synapse_0 = numpy.asarray(synapse['synapse0'])
        synapse_1 = numpy.asarray(synapse['synapse1'])
    return synapse_1,synapse_0