import numpy as np
import matplotlib.pyplot as plt

# 4a

x1=np.array([[3.1], [3.9], [5.2], [6.9]])
x2=np.array([[9], [7.5], [6], [5]])
y=([[10.2], [11.5], [13.9], [15]])

plt.plot(x1, y)
plt.plot(x2, y)

n=len(x1)

X = np.hstack([x1, x2, np.ones((n, 1))])


# pyplt.plot()