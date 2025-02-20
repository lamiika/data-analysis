import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
import pickle
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

# 4
df = pd.read_csv('housing.csv')

X = pd.concat([df.iloc[:, :-5], df.iloc[:, -3], df.iloc[:, -1]])
y = df.iloc[:, [-2]]

X_org = X

ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(drop='first'), ['ocean_proximity'])], remainder='passthrough')
X = ct.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
difference = y_pred - y_test

coef = model.coef_
inter = model.intercept_
print(f'y = {coef} x + {inter}')

R2 = r2_score(y_test, y_pred)
MAE = mean_absolute_error(y_test, y_pred)
MSE = mean_squared_error(y_test, y_pred)
RMSE = np.sqrt(MSE)

print(f'R2: {R2}')
print(f'MAE: {MAE}')
print(f'RMSE: {RMSE}')

with open('housing-model.pkl', 'wv') as file:
    pickle.dump(model, file)
with open('housing-ct.pkl', 'wv') as file:
    pickle.dump(ct, file)
