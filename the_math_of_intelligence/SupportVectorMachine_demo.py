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

# plt.show()

# Initialize our SVMs weight vector with zeros (3 values)
w = np.zeros(len(X[0]))
# The learning rate
eta = 1
# how many iterations to train for
epochs = 100000
# store misclassifications so we can plot how they change over time
errors = []

for epoch in range(1, epochs):
    error = 0
    print(epoch)
    for i, x in enumerate(X):
        # misclassification
        if (y[i] * np.dot(X[i], w)) < 1:
            # misclassified update for ours weights
            w = w + eta * ((X[i] * y[i]) + (-2 * (1 / epoch) * w))
            error = 1
        else:
            # correct classification, update our weights
            w = w + eta * (-2 * (1 / epoch) * w)
    errors.append(error)

plt.plot(errors, '|')
plt.ylim(0.5, 1.5)
plt.axes().set_yticklabels([])
plt.xlabel('Epoch')
plt.ylabel('Misclassified')
plt.show()
