import statistics

import math
import matplotlib.pyplot as plt

data = [101, 107, 103, 116, 110, 128, 100, 102, 109, 102, 100, 109, 110, 115, 120, 104, 93, 95, 101, 102, 138, 92]

mean = statistics.mean(data)  # media
median = statistics.median(data)  # mediana
variance = statistics.variance(data)  # varianza
standard_deviation = statistics.pstdev(data)  # desviación estándar

print("Data: " + data.__str__() +
      "\nMean: " + str(mean) +
      "\nMedian: " + str(median) +
      "\nVariance: " + str(variance) +
      "\nStandard deviation: " + str(standard_deviation))
'''
plt.plot(data)
plt.ylabel('pulsations')
plt.show()
'''

