import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.metrics import precision_score, recall_score
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

df = pd.read_csv('diabetes.csv')
nans = df.isna().sum()
X = df.iloc[:, :-1]
y = df['Outcome'].values

ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(drop='first'), [])], remainder='passthrough')
X = ct.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = LogisticRegression()
model.fit(X_train_scaled, y_train)

y_pred = model.predict(X_test_scaled)
y_pred_pros = model.predict_proba(X_test_scaled)

cm = confusion_matrix(y_test, y_pred)
acc = accuracy_score(y_test, y_pred)
pc = precision_score(y_test, y_pred)
rc = recall_score(y_test, y_pred)

print(f'cm: {cm}')
print(f'acc: {acc}')
print(f'pc: {pc}')
print(f'rc: {rc}')

tn, fp, fn, tp = cm.ravel()
ax = plt.axes()
sns.heatmap(cm, ax = ax, annot=True, fmt='g', cbar=False)
ax.set_title(f'LogReg (acc: {acc:.2f}, recall: {rc:.2f}, precision: {pc:.2f}')
plt.show()

Xnew = pd.read_csv('diabetes-new.csv')

Xnew = ct.transform(Xnew)

y_pred_new = model.predict(Xnew)
y_pred_new_pros = model.predict_proba(Xnew)

print(y_pred_new)
print(y_pred_new_pros)
