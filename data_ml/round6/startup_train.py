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

# 3

df = pd.read_csv('startup.csv')

X = df.iloc[:, :-1]
y = df.iloc[:, [-1]]

X_org = X

ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(drop='first'), ['State'])], remainder='passthrough')
X = ct.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

model = LinearRegression()
model.fit(X_train, y_train)

pickle.dump(model, open('model.pkl', 'wb'))
pickle.dump(ct, open('ct.pkl', 'wb'))
