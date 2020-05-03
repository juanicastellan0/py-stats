import math
import itertools

data = [101, 107, 103, 116, 110, 128, 100, 102, 109, 102, 100, 109, 110, 115, 120, 104, 93, 95, 101, 102, 138, 92]

factorial = math.factorial(len(data))
# permutations = list(itertools.permutations(data)) !!! this crash pc

# print(permutations)
print('Factorial of ' + str(len(data)) + ': ' + str(factorial))
# print('Quantity of permutations in range 1 - 4: ' + str(len(permutations)))
