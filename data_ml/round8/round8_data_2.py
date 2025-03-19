import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.metrics import precision_score, recall_score
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

# 2

df = pd.read_csv('iris.csv')

X = df.iloc[:, :-2]
y = df['Species'].values

ct = ColumnTransformer(transformers=[], remainder='passthrough')
X = ct.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)

model = RandomForestClassifier(n_estimators=100, random_state=0)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

cm = confusion_matrix(y_test, y_pred)
acc = accuracy_score(y_test, y_pred)
rc = recall_score(y_test, y_pred, average='macro')
pc = precision_score(y_test, y_pred, average='macro')

plt.figure(figsize=(10, 8))
ax = plt.axes()
sns.heatmap(cm, ax=ax, annot=True)

ax.set_title(f'Random Forest Classifier\nAccuracy: {acc:.2f}, Recall: {rc:.2f}, Precision: {pc:.2f}')
ax.set_xlabel('Predicted labels')
ax.set_ylabel('True labels')

class_names = ['setosa', 'versicolor', 'virginica']
ax.set_xticklabels(class_names)
ax.set_yticklabels(class_names)

plt.show()

Xnew_original = pd.read_csv('new-iris.csv')

Xnew = ct.transform(Xnew_original)

y_pred_new = model.predict(Xnew)
y_pred_new_pros = model.predict_proba(Xnew)

print(y_pred_new)
print(y_pred_new_pros)
