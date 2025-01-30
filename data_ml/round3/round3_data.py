import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

# 1

df = pd.read_csv('emp-dep.csv', dtype={'phone1':str, 'phone2':str})

plt.scatter(x=df['age'], y=df['salary'])
plt.title('Ikä ja palkka')
plt.xlabel('Ikä')
plt.ylabel('Palkka')
plt.show()

department_counts = df.groupby('dname').size()
    
department_counts.plot.barh()
plt.show()

# 2
age_counts = df.groupby('age_group').size()
age_counts.plot.bar()
plt.show()

# 3
gender_counts = df.groupby('gender').size()
gender_counts.plot.pie(labels=['miehet', 'naiset'], autopct='%1.1f%%')
plt.show()

age_genders = df.loc[:, ['gender', 'age_group', 'count']]
age_genders = age_genders.groupby(['age_group', 'gender']).sum()
sns.barplot(data=age_genders, x='age_group', y='count', hue='gender')
plt.show()
