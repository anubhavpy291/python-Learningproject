import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import pandas as pd
df = pd.read_csv("studnet.csv")

x = df[["YearsExperience"]].to_numpy()
y = df[["Salary"]].to_numpy()
x_train , x_test , y_train, y_test = train_test_split(x,y,test_size=0.4,random_state=42) 
model = LinearRegression()
model.fit(x_train,y_train)
predict = model.predict(x_test)
error = mean_squared_error(y_test,predict)
plt.scatter(x_test, y_test, color="blue", label="Data")

plt.plot(x_test,predict , color="red", label="Regression Line")

plt.grid(True)
plt.show()