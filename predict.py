import numpy as np
import matplotlib.pyplot as plot
data = np.array([
    [0,0],
    [1,0],
    [2,1],
    [3,2],
    [4,3],
    [5,4]

])
x = data[:,0]
y = data[:,1]
b = 0.1
w = 0.1
lr = 0.1

def sigmoid(x):
    return 1 / (1 + np.exp(-x))
def sigmoid_dervivation(x):
    return x * (1-x)
for i in range(100000):
    z = x * w + b

    prediction = z
    loss = np.mean((y - prediction)**2)

    error = y - prediction
    delta = error * sigmoid_dervivation(prediction)

    gradiant_w = np.mean(x * delta)
    gradiant_b = np.mean(delta)
    w += lr * gradiant_w
    b += lr * gradiant_b

i = int(input("elo_diff: "))
pred = i*w+b
print(pred )

#x = data[:,0]
#y = data[:,1]

# statics 

#m = ((x - x.mean()) * (y - y.mean())).sum() / ((x - x.mean()) ** 2).sum()
#b = (y.mean() - m * x.mean())

#input
#elo_diff = 39

# y = m + input * b

#chance = m  + elo_diff * b
#print(f"chances: {round(chance)}%")