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

departments = df['dname'].unique()

for dep in departments:
    emp_count = df[df['dep']]



