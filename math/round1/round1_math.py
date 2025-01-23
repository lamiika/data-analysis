import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 4a

x1 = np.array([[3.1], [3.9], [5.2], [6.9]])
x2 = np.array([[9], [7.5], [6], [5]])
y = np.array([[10.2], [11.5], [13.9], [15]])

plt.scatter(x1, y)
plt.show()
plt.scatter(x2, y)
plt.show()

# 4b

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
n=len(x1)
ax.scatter(x1, x2, y)
ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_zlabel('y')

plt.show()

# 4c

X = np.hstack([x1, x2, np.ones((n, 1))])

a = np.linalg.inv(X.transpose()@X)@X.transpose()@y

# 4d

a1 = a[0]
a2 = a[1]
a3 = a[2]

print(f"a1 = {a1} a2 = {a2} a3 = {a3}")
# a1 = [0.23597122] a2 = [-1.02618705] a3 = [18.57827338]
# Saadut luvut ovat koneoppimismallin kertoimet

y_ennustettu = a1*x1 + a2*x2 + a3
print(y)
# [[10.2] [11.5] [13.9] [15. ]]
print(y_ennustettu)
# [[10.07410072] [11.80215827] [13.64820144] [15.07553957]]

# np.linalg.inv(X.transpose()@X)@X.transpose()@y
# Otetaan inversio (X:n transpoosi matriisitulo X):stä
# Otetaan tämän tulosmatriisin matriisitulo X:transpoosista
# Otetaan tämän tulosmatriisin matriisitulo y:n kanssa
# a = (X^T X)^(-1) X^T y

# 5a
y_avg = y.mean()
print(y_avg)
# 12.65

# 5b
y_distance = np.subtract(y, y_avg)
print(y_distance)
#[[-2.45] [-1.15] [ 1.25] [ 2.35]]

# 5c
y_distance_squared = np.square(y_distance)
print(y_distance_squared)
#[[6.0025] [1.3225] [1.5625] [5.5225]]

# 5d
SSTot = sum(y_distance_squared)
print(SSTot)
# [14.41]

# 5e
check_SSTot = sum(np.square(y - y.mean()))
print(check_SSTot)
# [14.41]

# 6a
residuals = np.subtract(y, y_ennustettu)
print(residuals)
# [[ 0.12589928] [-0.30215827] [ 0.25179856] [-0.07553957]]

# 6b
SSRes = sum(np.square(residuals))
print(SSRes)
# [0.17625899]

# 6c
check_SSRes = sum(np.square(y - y_ennustettu))
print(check_SSRes)
# [0.17625899]

# 7a
x1 = [3.1, 3.9, 5.2, 6.9]
x2 = [9, 7.5, 6, 5]
y = [10.2, 11.5, 13.9, 15]
p2 = np.polyfit(x1, y, 2, full=True)
print(p2[0])

# 7b
# y = (-0.25667057) * x^2 + 3.87115982 * x + 0.54796716

# 7c
p = np.poly1d(p2[0])
line = np.linspace(min(x1), max(x1), 100)
plt.scatter(x1, y)
plt.plot(line, p(line), color='green')
plt.xlabel('x1')
plt.ylabel('y')
plt.show()

# 7d
sns.residplot(x=x1, y=y, scatter_kws={'alpha': 0.5}, line_kws={'color': 'green'})
plt.show()

# 8a
residuals = np.subtract(y, y)
