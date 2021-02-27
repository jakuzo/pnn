# ReLU - Rectified Linear Unit. A deceptively simple equation: y = max(0, x).
# Despite its name an appearance, it's not linear and provides the same benefits as
# sigmoid but with better performance.

# Pros
# Avoids and rectifies vanishing gradient problem.
# Fast and efficient

# Cons
# Should only be used within Hidden layers of Network models
# Fragile gradients can lead to dead Neurons.
# See dying ReLU problem
# Can blow up activations.

import numpy as np

class ReLU:
    # f(x) = max(0, x)
    @staticmethod
    def compute(x: float) -> float:
        return np.max([0, x])
    
    # f'(x) = 1 if x > 0 otherwise 0
    @staticmethod
    def derivative(x: float) -> float:
        return 1.0 if x > 0 else 0