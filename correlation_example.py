from scipy import stats
import numpy as np
import matplotlib.pyplot as plt


a = np.array([0, 0, 0, 1, 1, 1, 1])
b = np.arange(7)
pearsonr = stats.pearsonr(a, b)  # [coeficiente de correlación Pearson, valor de dos colas]

print('Data: ')
print('a: ' + a.tostring().decode())
print('b: ' + b.tostring().decode())
print('pearson r = ' + str(pearsonr))

plt.plot(a, b)
plt.show()
