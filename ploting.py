import numpy as np
import matplotlib.pyplot as plot

# Feature: Weight in 1000s of pounds
X = np.array([
    3.50,
    3.69,
    3.44,
    3.43,
    4.34,
    4.42,
    2.37
])

# Label: Miles per gallon
y = np.array([
    18,
    15,
    18,
    16,
    15,
    14,
    24
])
w = -4.6
lr = 0.01
b = 34
z = None
z = w * X + b
s = 1/(1+np.exp(-z))
mae = np.sum(np.absolute(y-z))
mse = np.mean((y-z) ** 2)

plot.plot(z)
plot.plot(s)
plot.scatter(X,y)
plot.grid()
plot.show()