import numpy as np
import matplotlib.pyplot as plot
x = np.array([1,2,3,4,5,6,7,8])
y = x[:] * 10
w = 0.1
lr = 0.01
b = 0.1

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def sigmoid_derivative(z):
    return z * (1 - z)
def freeforword(x):
    z = (x * w) + b
    return z

for i in range(100000):
    predaction = freeforword(x)
    error = y - predaction
    delta = error
    gradient_W = np.mean(x * delta)
    grediant_b = np.mean(delta)
    w += lr * gradient_W
    b += lr * grediant_b
while True:
    inp = int(input("enter: "))
    p = freeforword(inp)
    print(p)
    
    plot.figure(figsize=(8,5))

    # Training data
    plot.scatter(x, y, color="blue", label="Training Data")

    # Learned line
    plot.plot(x, p, color="red", label="Prediction")

    # User input
    plot.scatter(inp, p, color="green", s=120, label="Your Input")

    plot.legend()
    plot.grid(True)
    plot.show()