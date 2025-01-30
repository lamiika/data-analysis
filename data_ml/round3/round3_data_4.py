import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

# 4

df = pd.read_excel('unemployment.xlsx')

df_tot = df.loc[:, ['Period', 'Unemployed']]

df_tot = df_tot.groupby('Period').sum()

sns.lineplot(df_tot)
plt.ticklabel_format(style='plain', axis='y')
plt.title('Total unemployment')
plt.legend()
plt.show()


df_gender_tot = df.loc[:, ['Gender', 'Period', 'Unemployed']]

df_gender_tot = df_gender_tot.groupby(['Period', 'Gender']).sum()

sns.lineplot(data=df_gender_tot, x='Period', y='Unemployed', hue='Gender')
plt.ticklabel_format(style='plain', axis='y')
plt.title('Unemployment by Gender')
plt.legend()
plt.show()

df_age_tot = df.loc[:, ['Age', 'Period', 'Unemployed']]

df_age_tot = df_age_tot.groupby(['Period', 'Age']).sum()

sns.lineplot(data=df_age_tot, x='Period', y='Unemployed', hue='Age')
plt.ticklabel_format(style='plain', axis='y')
plt.title('Unemployment by Age')
plt.legend()
plt.show()

#sns.lineplot(x='Period', y='Unemployed', data=df[df['Gender'] == 'Men'], label='Men', errorbar=None)
#sns.lineplot(x='Period', y='Unemployed', data=df[df['Gender'] == 'Women'], label='Women', errorbar=None)
#plt.title('Unemployment by Gender')
#plt.legend()
#plt.show()

#age_groups = df['Age'].unique()

#for age in age_groups:
#    sns.lineplot(x='Period', y='Unemployed', data=df[df['Age'] == age], label=age, errorbar=None)
    
#plt.title('Unemployment by Age')
#plt.legend()
#plt.show()

