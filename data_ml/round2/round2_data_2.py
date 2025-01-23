import pandas as pd
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

# Tehtävä 3

df_data = pd.read_csv('Titanic_data.csv')
df_names = pd.read_csv('Titanic_names.csv')

print("data info: ", df_data.info())
print("names info: ",df_names.info())
print("data describe: ", df_data.describe())
print("names describe: ", df_names.describe())

df_data.hist(bins=4)

df = pd.merge(df_data, df_names, how='inner', on='id')

person_count = df['Name'].count()
print("\nHenkilöiden määrä: ", person_count)

m_count = df[df['GenderCode'] == 0].count().iloc[0]
w_count = df[df['GenderCode'] == 1].count().iloc[0]
print("Miesten määrä: ", m_count, "\nNaisten määrä: ", w_count)

avg_age = df['Age'].mean()
print("Keski-ikä: ", avg_age)

zero_count = df[df['Age'] == 0].count().iloc[0]
print("Nollan ikäisiä: ", zero_count)

# Tehtävä 4
print("\nTehtävä 4\n")

avg_age = df['Age'][df['Age'] != 0].mean()
df['Age'] = df['Age'].replace(0, avg_age)

print("Keski-ikä: ", avg_age)

print(df['PClass'].unique())

print(df['Name'][df['PClass'] == '*'])

survivor_count = df[df['Survived'] == 1].count().iloc[0]
dead_count = df[df['Survived'] == 0].count().iloc[0]

print("Selviytyneiden määrä: ", survivor_count)
print("Ei-selviytyneiden määrä: ", dead_count)

survivor_percentage = survivor_count / person_count * 100
dead_percentage = dead_count / person_count * 100

print("Selviytyneiden prosentti: ", survivor_percentage, "%")
print("Ei-selviytyneiden prosentti: ", dead_percentage, "%")

m_survivor_count = df[(df['Survived'] == 1) & (df['GenderCode'] == 0)].count().iloc[0]
m_dead_count = df[(df['Survived'] == 0) & (df['GenderCode'] == 0)].count().iloc[0]
w_survivor_count = df[(df['Survived'] == 1) & (df['GenderCode'] == 1)].count().iloc[0]
w_dead_count = df[(df['Survived'] == 0) & (df['GenderCode'] == 1)].count().iloc[0]

print("Selviytyneiden miesten määrä: ", m_survivor_count)
print("Ei-selviytyneiden miesten määrä: ", m_dead_count)
print("Selviytyneiden naisten määrä: ", w_survivor_count)
print("Ei-selviytyneiden naisten määrä: ", w_dead_count)