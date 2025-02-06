import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import chi2_contingency, pearsonr, spearmanr
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

# 1
df = pd.read_excel('tt.xlsx')
print(df.describe())
df.hist()
plt.show()
df.info()
largest = df.nlargest(5, 'palkka').loc[:, ['palkka']]
smallest = df.nsmallest(5, 'palkka').loc[:, ['palkka']]
print(largest)
print(smallest)

# tee frekvenssitaulukko 
# (koulutustausta, lukumäärä ja %-osuus)
value_map = {1.0: '1 Peruskoulu', 2.0: '2 2. aste', 3.0: '3 Korkeakoulu', 4.0: '4 Ylempi korkeakoulu'}
df['koulutus'] = df['koulutus'].map(value_map)

crosstable = pd.crosstab(df['koulutus'], 'Lukumäärä')

total_amount = crosstable.sum().sum()
percentages = crosstable.div(total_amount).mul(100)

colors = ['blue', 'yellow', 'green', 'red']

# Plot the crosstable with different colors for each bar
crosstable.plot(kind='barh', color=colors)
plt.show()
crosstable['%'] = percentages.iloc[:, 0]

print(crosstable)

plt.show()

# 2
df_male = df[df['sukup'] == 1]
df_female = df[df['sukup'] == 2]
male = pd.crosstab(df_male['koulutus'], 'Mies')
female = pd.crosstab(df_female['koulutus'], 'Nainen')

combined = pd.concat([female, male], axis=1).fillna(0)
print(combined)

# 3
chi2, p, dof, expected = chi2_contingency(combined)
if p < 0.05:
    print('3) p-arvo merkitsevä:', p)
else:
    print('3) p-arvo ei-merkitsevä:', p)
print(chi2, p, dof, expected)

combined.plot(kind='barh')
plt.show()

# 4
df = pd.read_excel('tt.xlsx')
df_corr = df.loc[:, ['sukup', 'ikä', 'perhe', 'koulutus', 'palkka']]

print(df_corr.corr())
sns.heatmap(df_corr.corr(), annot=True, cmap='coolwarm', vmin=-1, vmax=1, center=0)
plt.show()

pay_corr = pearsonr(df_corr['palkka'], df_corr['ikä'])
print('4) palkan ja iän korrelaatio:', pay_corr[0])
if pay_corr[1] < 0.05:
    print('4) p-arvo merkitsevä:', pay_corr[1], '< 0.05')
else:
    print('4) p-arvo ei-merkitsevä:', pay_corr[1], '>= 0.05')

pay_corr_spear = spearmanr(df_corr['palkka'], df_corr['ikä'])
print('4) palkan ja iän korrelaatio spearmanr', pay_corr_spear[0])
if pay_corr[1] < 0.05:
    print('4) p-arvo merkitsevä:', pay_corr_spear[1], '< 0.05')
else:
    print('4) p-arvo ei-merkitsevä:', pay_corr_spear[1], '>= 0.05')

sns.regplot(x=df_corr['ikä'], y=df_corr['palkka'], ci=None)
plt.show()



