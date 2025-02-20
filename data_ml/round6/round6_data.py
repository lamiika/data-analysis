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

# 1
df = pd.read_csv('startup.csv')

print(df['State'].unique())
nans = df.isna().sum()

X = df.iloc[:, :-1]
y = df.iloc[:, [-1]]

dummies = pd.get_dummies(df, drop_first=True)

X_org = X

ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(drop='first'), ['State'])], remainder='passthrough')
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

# 2
new_df = pd.read_csv('new_company.csv')
dummies_new = pd.get_dummies(new_df, drop_first=True)

prediction = model.predict(dummies_new)
print('T2 ennustus dummies', prediction)

new_df_ct = pd.read_csv('new_company_ct.csv')
X = new_df_ct.iloc[:, :]
y = new_df_ct.iloc[:, [-1]]
X_org = X
X = ct.transform(X)
prediction = model.predict(X)
print('T2 ennustus ct.transform', prediction)
