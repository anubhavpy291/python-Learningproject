import numpy as np
from sklearn.tree import DecisionTreeRegressor,plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.datasets import fetch_california_housing
import pandas as pd
import matplotlib.pyplot as plt

housing = fetch_california_housing()
data = pd.DataFrame(housing.data,columns=housing.feature_names)
data["price"] = housing.target
data = data.head(100)
x = data.drop(columns="price")
y = data["price"]

x_train , x_test , y_train, y_test = train_test_split(x,y)
model = DecisionTreeRegressor(max_depth=1)
model.fit(x_train,y_train)
y_predict = model.predict(x_test)

plt.figure(figsize=(20, 10)) 
plot_tree(model,feature_names=x.columns,filled=True,rounded=True,fontsize=10 ) 
plt.title("Decision Tree Structure") 
plt.show()