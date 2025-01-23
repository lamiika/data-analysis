# Tehtävä 1
import pandas as pd
from datetime import datetime, timedelta

a = [1,2,3,4,5]

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
df_nans = df.isna().sum()
df = df.fillna(0)

avg_sal = df['salary'].mean()
avg_sal_tuote = df[df['dname'] == 'Tuotekehitys']['salary'].mean()

w_count = df[df['gender'] == 1].count()
m_count = df[df['gender'] == 0].count()

w_percent = w_count / emp_count
m_percent = m_count / emp_count

df['age'] = (datetime.now() - pd.to_datetime(df['bdate'])) // timedelta(days=365.2425)

















