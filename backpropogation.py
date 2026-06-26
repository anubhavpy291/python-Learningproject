import numpy as np

x = 1
y = 2
w = 0.1
lr = 0.1
b = 0.1

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def sigmoid_derivative(z):
    return z * (1 - z)
def freeforword():
    z = (x * w) + b
    return sigmoid(z)

for i in range(1000):
    predaction = freeforword()
    error = y - predaction
    delta = error * sigmoid_derivative(predaction)
    gradient_W = x * delta
    grediant_b = delta
    w += lr * gradient_W
    b += lr * grediant_b
print(freeforword())