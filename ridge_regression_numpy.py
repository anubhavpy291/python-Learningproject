import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_regression
x,y = make_regression(n_samples=10,n_features=2,noise=1,random_state=42)
w = np.random.randn(2,1)
b = 0 
lamda_ = 1
lr = 0.01
echops = 100

n = len(x)

for i in range(echops):
    z = x @ w + b
    error = z - y
    mse = np.mean(error**2)
    
    ridge_panilty = lamda_ * np.sum(w**2)
    lose = mse + ridge_panilty
    dw = (2/n) * (x.T @ error) + 2 * lamda_ * w

    db = (2/n) * np.sum(error)

    w -= lr * dw
    b -= lr * db

plt.scatter(x,y)
plt.plot(x,x @ w + b)
plt.show()