import numpy as np
from sklearn.linear_model import RidgeCV
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error
st = StandardScaler()

housing = fetch_california_housing()
data = pd.DataFrame(housing.data,columns=housing.feature_names)
data["prices"] = housing.target
data = data.head(500)

x = data.drop(columns="prices")
y = data["prices"]
print(x)
print(y)

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=42)

x_train_scaled = st.fit_transform(x_train)
x_test_scaled = st.transform(x_test)
alpha = [0.1,1.0,10.0,100.0]
model = RidgeCV(alphas=alpha)
model.fit(x_train_scaled,y_train)
y_predict = model.predict(x_test_scaled)

print(mean_squared_error(y_test,y_predict))
print(mean_absolute_error(y_test,y_predict))