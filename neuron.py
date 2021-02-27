# inputs * weights + bias
import numpy as np

class Neuron:
    def __init__(self, inputs=[], weights=[], bias=0 ):
        self.inputs = inputs
        self.weights = weights
        self.bias = bias
        self.output = 0
    
    def compute(self):
        self.output = np.dot(self.weights, self.inputs) + self.bias
        return(self.output)

