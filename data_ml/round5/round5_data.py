import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

# 1
df = pd.read_csv('salary.csv')
x = 'YearsExperience'
y = 'Salary'

plt.scatter(df['YearsExperience'], df['Salary'])
plt.xlabel(x)
plt.ylabel(y)
plt.show()

split_index = int(len(df) * 0.7)
training_data = df.iloc[:split_index]
test_data = df.iloc[split_index:]

x_train = training_data[[x]]
y_train = training_data[y]

x_test = test_data[[x]]
y_test = test_data[y]

#x_train, x_test, y_train, y_test = train_test_split(df[[x]], df[y], test_size=0.3, random_state=42)

model = LinearRegression()
model.fit(x_train, y_train)

print(f'Suoran yhtälö: y = {model.intercept_:.2f} + {model.coef_[0]:.2f} x')

y_pred = model.predict(x_test)

difference = y_pred - y_test
print('Keskimääräinen absoluuttinen ennustevirhe:', difference.values.mean())

plt.scatter(test_data[x], test_data[y])
plt.plot(x_test, y_pred)
plt.xlabel('Palkka')
plt.ylabel('Kokemus')
plt.title('Palkka vs kokemus (testidata)')
plt.show()

sns.regplot(x=x_test[x], y=y_test, ci=None)
plt.xlabel('Palkka')
plt.ylabel('Kokemus')
plt.title('Palkka vs kokemus (sns.regplot)')
plt.show()

MAE = mean_absolute_error(y_test, y_pred)
MSE = mean_squared_error(y_test, y_pred)
RMSE = np.sqrt(MSE)
R2 = r2_score(y_test, y_pred)

print(f'MAE: {MAE}')
print(f'MSE: {MSE}')
print(f'RMSE: {RMSE}')
print(f'R2: {R2}')

years = 7
prediction = model.predict(pd.DataFrame({x: [years]}))
print(f'Uuden työntekijän palkka {years}v kokemuksella on: {prediction[0]:.2f}')

df = pd.read_csv('housing.csv')
x = 'median_income'
y = 'median_house_value'

plt.scatter(df[x], df[y])
plt.xlabel(x)
plt.ylabel(y)
plt.show()

x_train, x_test, y_train, y_test = train_test_split(df[[x]], df[y], test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(x_train, y_train)

print(f'Suoran yhtälö: y = {model.intercept_:.2f} + {model.coef_[0]:.2f} x')

income = 7
prediction = model.predict(pd.DataFrame({x: [income]}))
print(f'Talon arvo {income}0 000 dollarin vuosipalkalla on: {prediction[0]:.2f} dollaria')

y_pred = model.predict(x_test)
difference = y_pred - y_test
plt.hist(difference)
plt.title('Ennustettujen ja todellisten talon arvojen erot')
plt.xlabel('Erotus')
plt.ylabel('Määrä')
plt.show()

MAE = mean_absolute_error(y_test, y_pred)
MSE = mean_squared_error(y_test, y_pred)
RMSE = np.sqrt(MSE)
R2 = r2_score(y_test, y_pred)

print(f'MAE: {MAE}')
print(f'MSE: {MSE}')
print(f'RMSE: {RMSE}')
print(f'R2: {R2}')

income = 3
prediction = model.predict(pd.DataFrame({x: [income]}))
print(f'Talon arvo {income}0 000 dollarin vuosipalkalla on: {prediction[0]:.2f} dollaria')
