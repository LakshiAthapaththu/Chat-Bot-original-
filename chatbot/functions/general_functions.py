import numpy
import time

def sigmoid (x):
    output = 1/(1+numpy.exp(-x))
    return output
    #for a given x value get a corresponding y value of sigmoid function

def derivative(output):
    return output*(1-output)
    #for given output return the corresponding derivative value

