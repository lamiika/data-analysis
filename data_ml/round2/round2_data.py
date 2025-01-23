import pandas as pd
from datetime import datetime, timedelta
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

# Tehtävä 1

df_emp = pd.read_csv('employees.csv', header=0, sep=',', decimal='.', dtype={'phone1':str, 'phone2':str})

df_dep = pd.read_csv('departments.csv')

emp_desc = df_emp.describe()

temp_emp = df_emp[['salary', 'gender']]
#temp_emp = temp_emp.iloc[1:]
emp_corr = temp_emp.corr()

print(df_emp['lname'].unique())

print(df_emp['salary'].nlargest(5))

df = pd.merge(df_emp, df_dep, how='inner', left_on='dep', right_on='dep')
df.drop(columns=['image'], inplace=True)

# Tehtävä 2

# emp_count = df.shape[0]
emp_count = df['lname'].count()
print("Työntekijöiden määrä", emp_count)

w_count = df[df['gender'] == 1].count().iloc[0]
m_count = df[df['gender'] == 0].count().iloc[0]
print("Naiset määrä: ", w_count, " miehet määrä: ", m_count)

w_percent = w_count / emp_count
m_percent = m_count / emp_count
print("Naiset prosentti: ", w_percent * 100, "% miehet prosentti: ", m_percent * 100, "%")

min_sal = df['salary'].min()
max_sal = df['salary'].max()
avg_sal = df['salary'].mean()
print("Minimipalkka: ", min_sal, " maksimipalkka: ", max_sal, " keskipalkka: ", avg_sal)

avg_sal_tuote = df[df['dname'] == 'Tuotekehitys']['salary'].mean()
print("Tuotekehityksen keskipalkka: ", avg_sal_tuote)

df_nans = df.isna().sum()
df = df.fillna(0)
missing_phone2 = (df['phone2'] == 0).sum()
print("Puuttuvat phone2:t: ", missing_phone2)

df['age'] = (datetime.now() - pd.to_datetime(df['bdate'])) // timedelta(days=365.2425)

ages = [15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]
labels = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]
df['age_group'] = pd.cut(df['age'], bins=ages, labels=labels, right=True)

df2 = df[['salary', 'age', 'gender']]
df2_corr = df2.corr()

import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 6))
sns.heatmap(df2_corr, annot=True, cmap='coolwarm', vmin=-1, vmax=1, center=0)
plt.show()
