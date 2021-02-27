# Softmax function also known as softargmax
# takes as input a vector z of K real numbers and normalizes it into a probability distribution
# consisting of K probabilities proportional to the exponentials of the input numbers
# That is, prior to applying softmax, some vector components could be negative, 
# or greater than one; and might not sum to 1; but after applying softmax, 
# each component will be in the interval (0,1), and the components will add up to 1, 
# so that they can be interpreted as probabilities. 
# Furthermore, the larger input components will correspond to larger probabilities.

class Softmax:
    
    
    @staticmethod
    def compute(z: list) -> list:
        pass
