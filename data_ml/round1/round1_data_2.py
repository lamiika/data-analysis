import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("diabetes.csv")

count = df.count()
mean = df.mean()
min_val = df.min()
max_val = df.max()
std = df.std()

print(f"\ncount:\n\n{count}")
print(f"\nmean:\n\n{mean}")
print(f"\nmin_val:\n\n{min_val}")
print(f"\nmax_val:\n\n{max_val}")
print(f"\nstd:\n\n{std}")

df['Pregnancies'].hist(bins=10)
plt.title('Pregnancies')
plt.show()

df['Glucose'].hist(bins=10)
plt.title('Glucose')
plt.show()

df['BloodPressure'].hist(bins=10)
plt.title('BloodPressure')
plt.show()

df['SkinThickness'].hist(bins=10)
plt.title('SkinThickness')
plt.show()

df['Insulin'].hist(bins=10)
plt.title('Insulin')
plt.show()

df['BMI'].hist(bins=10)
plt.title('BMI')
plt.show()

df['DiabetesPedigreeFunction'].hist(bins=10)
plt.title('DiabetesPedigreeFunction')
plt.show()

df['Age'].hist(bins=10)
plt.title('Age')
plt.show()

df['Outcome'].hist(bins=10)
plt.title('Outcome')
plt.show()

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("diabetes.csv")

correlation_matrix = df.corr()

plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='inferno', vmin=-0.2, vmax=1)
plt.show()
