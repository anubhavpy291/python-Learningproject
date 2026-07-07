import numpy as np
from sklearn.linear_model import LogisticRegression
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris


iris = load_iris()
x = iris.data
y = iris.target
model = LogisticRegression(max_iter=100)


x_train , x_test , y_train , y_test = train_test_split(x,y,test_size=0.4,random_state=42)
model.fit(x_train,y_train)
predict = model.predict(x_test)

plt.scatter(x,y,color="red")
plt.plot(x_test,predict,color="blue")
plt.grid(True)
plt.show()

