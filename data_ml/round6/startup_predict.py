import pandas as pd
import pickle
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

# 3

with open('model.pkl', 'rb') as file:
    model = pickle.load(file)
with open('ct.pkl', 'rb') as file:
    ct = pickle.load(file)

new_df_ct = pd.read_csv('new_company_ct.csv')
X = new_df_ct.iloc[:, :]
y = new_df_ct.iloc[:, [-1]]
X_org = X
X = ct.transform(X)
prediction = model.predict(X)
print('T3 ennustus ct.transform', prediction)
