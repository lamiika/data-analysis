import numpy as np

# 2 a
x=[2,3,6]
y=[1,4,5]

p = np.polyfit(x, y, 1, full=True)

SSRes = p[1]
print("2a SSRes: ", SSRes)

# 2 b
y_col = np.array(y)
y_mean = np.mean(y_col)
y_res = y_col - y_mean
SSTot = sum(y_res**2)

R2 = 1-(SSRes/SSTot)
print("2b Selitysaste: ", R2)

# 2 c

x_col = np.array(x)
SSReg = sum((p[0][0]*x_col+p[0][1]-y_mean)**2)

print("2c Regressioneliösumma: ", SSReg)

# 2 d

R2 = SSReg/SSTot
print("2d Selitysaste: ", R2)

# 3 a
y = np.array([10.2, 11.5, 13.9, 15])
x1 = np.array([3.1, 3.9, 5.2, 6.9])
x2 = np.array([9, 7.5, 6, 5])
x1 = np.array([[3.1], [3.9], [5.2], [6.9]])
x2 = np.array([[9], [7.5], [6], [5]])
y = np.array([[10.2], [11.5], [13.9], [15]])
n = len(x1)

X = np.hstack([x1, x2, np.ones((n, 1))])
a = np.linalg.inv(X.transpose()@X)@X.transpose()@y

a1 = a[0]
a2 = a[1]
a3 = a[2]

y_ennustettu = a1*x1 + a2*x2 + a3

residuals = y - y_ennustettu
print("3a Residuaalit: ", residuals.tolist())

# 3 b
y_avg = y.mean()
SSRes = sum(residuals**2)
SSTot = sum((y-y_avg)**2)

R2 = 1 - SSRes/SSTot
print("3b Selitysaste: ", R2)

# 4 a
SSReg = sum((y_ennustettu-y_avg)**2)
print("4a SSReg: ", SSReg)

# 4 b
R2 = SSReg / SSTot
print("4b Selitysaste: ", R2)
# 3 b ja 4 b selitysaste on sama 0.98776829

# 5 a




