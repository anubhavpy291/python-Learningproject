import numpy as np

x = np.array([1,2,3,4])
w = np.array([0.1,0.2,0.3,0.4])
b = 0.1

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

z = np.dot(x, w) + b
prediction = sigmoid(z)

print(prediction)