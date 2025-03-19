import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from scipy import stats
from scipy.stats import mannwhitneyu
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from sklearn.compose import ColumnTransformer
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

filename = 'Epileptic_Seizure_Recognition.csv'
colname = 'Unnamed'
blue = '#1f77b4'
orange = '#ff7f0e'

total_rows = sum(1 for line in open(filename))
rows_to_read = total_rows // 20

df = pd.read_csv(filename)
df_original = df

df.info()
nans = df.isna().sum()

first_row = df.iloc[0]

# Preprocessing

df[['second', 'patient']] = df[colname].str.split('.V', expand=True)
df['second'] = df['second'].str.replace('X', '', regex=False).astype(int)
df['second'] = df['second'].apply(lambda x: f'{x:02d}')
columns = df.columns.tolist()
new_order = columns[-3:] + columns[1:-3]
df = df[new_order]
df = df.sort_values(by=['patient', 'second'])

y_patient = df.loc[:, ['patient', 'y']]
y_patient = y_patient.groupby('patient').mean().reset_index()

df_drops = df.iloc[:, 2:]

result = (
  df_drops.groupby('patient')
  .apply(lambda group: group.drop(columns='patient').to_numpy().flatten())
  .apply(pd.Series)
)

df_merged = result.reset_index()
df_merged = df_merged.merge(y_patient, on='patient', how='left')

cols = df_merged.columns.tolist()
cols.remove('patient')
cols.remove('y')
cols = ['patient', 'y'] + cols
df_merged = df_merged[cols]

df_abs = df_merged.copy()
df_abs.iloc[:, 2:] = df_abs.iloc[:, 2:].applymap(abs)

# Preprocessing complete

df_seizure = df_merged[df_merged['y'] == 1]
df_non_seizure = df_merged[df_merged['y'] != 1]

df_abs_seizure = df_abs[df_abs['y'] == 1]
df_abs_non_seizure = df_abs[df_abs['y'] != 1]

plt.figure(figsize=(12, 8))
plt.plot(df_abs_seizure.iloc[:, 2:].mean(), color=blue, label='Average Seizure Readings (n=100)')
plt.plot(df_abs_non_seizure.iloc[:, 2:].mean(), color=orange, label='Average Non-Seizure Readings (n=400)')

# Format x-axis values
tick_positions = range(0, len(df_seizure.iloc[:, 2:].columns), 178)
tick_labels = [f'{i//178}s' for i in tick_positions]
plt.xticks(tick_positions, tick_labels)
# Format y-axis values
formatter = FuncFormatter(lambda x, _: f'{x:.0f}µV')
plt.gca().yaxis.set_major_formatter(formatter)

plt.ylim(bottom=0)
plt.title('Epileptic Seizure Average Absolute Value EEG Data Comparison')
plt.xlabel('Time (seconds)')
plt.ylabel('Readings (µV)')
plt.legend()
plt.show()

plt.figure(figsize=(12, 8))

for _, row in df_seizure.iterrows():
  plt.plot(row.iloc[2:], color=blue, alpha=0.1)

for _, row in df_non_seizure.iterrows():
  plt.plot(row.iloc[2:], color=orange, alpha=0.1)

plt.xticks(tick_positions, tick_labels)
plt.gca().yaxis.set_major_formatter(formatter)

plt.title('Average EEG Readings for Each Patient')
plt.xlabel('Time (seconds)')
plt.ylabel('Readings (µV)')
plt.tight_layout()
plt.show()

numeric_cols = [col for col in df_abs.columns if col not in ['patient', 'y']]
X = df_abs[numeric_cols]
y = df_abs['y'].apply(lambda value: 1 if value == 1 else 0)

ct = ColumnTransformer(transformers=[], remainder='passthrough')
X = ct.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
difference = y_pred - y_test

R2 = r2_score(y_test, y_pred)
MAE = mean_absolute_error(y_test, y_pred)
MSE = mean_squared_error(y_test, y_pred)
RMSE = np.sqrt(MSE)

print('Linear regression values')
print(f'R2: {R2}')
print(f'MAE: {MAE}')
print(f'RMSE: {RMSE}')
print('')

t_test_results = {}

for column in df_merged.columns[2:]:
  seizure_data = df_abs_seizure[column]
  non_seizure_data = df_abs_non_seizure[column]
    
  t_statistic, p_value = stats.ttest_ind(seizure_data, non_seizure_data)
    
  t_test_results[column] = {
    't_statistic': t_statistic,
    'p_value': p_value
  }

avg_t_statistic = np.mean([result['t_statistic'] for result in t_test_results.values()])
avg_p_value = np.mean([result['p_value'] for result in t_test_results.values()])

print(f'Average T-statistic comparing seizure to non-seizure: {avg_t_statistic:.4f}')
print(f'Average P-value comparing seizure to non-seizure: {avg_p_value:.4f}')

sig = 0.001
significant_features = sum(1 for result in t_test_results.values() if result['p_value'] < sig)
print(f'Number of seizure data with significant difference to non-seizure data: {significant_features} out of {len(t_test_results)}')

percentage = significant_features / len(t_test_results) * 100
print(f'Percentage of seizure data with significant difference to non-seizure data: {percentage:.3g}%')
print('')

seizure_values = df_abs_seizure.iloc[:, 2:].to_numpy().flatten()
non_seizure_values = df_abs_non_seizure.iloc[:, 2:].to_numpy().flatten()

statistic, p_value = mannwhitneyu(seizure_values, non_seizure_values, alternative='two-sided')

print(f'Mann-Whitney U Statistic: {statistic}')
print(f'P-value: {p_value}')

sig = 0.001
if p_value < sig:
    print('Reject the null hypothesis: There is a significant difference between the two groups.')
else:
    print('Fail to reject the null hypothesis: No significant difference between the two groups.')