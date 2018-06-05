import numpy as np
from matplotlib import pyplot as plt

# Input data - Of the form [X value, Y value, Bias term]
X = np.array([
    [-2, 4, -1],
    [4, 1, -1],
    [1, 6, -1],
    [2, 4, -1],
    [6, 2, -1],
])

# Associated output labels - First 2 examples are labeled '-1' and last 3 are labeled '+1'
y = np.array([-1, -1, 1, 1, 1])

# plot them in 2D graph
for d, sample in enumerate(X):

    if d < 2:
        plt.scatter(sample[0], sample[1], s=120, marker='_', linewidths=2)
    else:
        plt.scatter(sample[0], sample[1], s=120, marker='+', linewidths=2)
