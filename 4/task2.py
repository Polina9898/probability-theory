#  О случайной непрерывной равномерно распределенной величине B известно, что ее дисперсия равна 0.2.

# Можно ли найти правую границу величины B и ее среднее значение зная, что левая граница равна 0.5?

# Если да, найдите ее.

import math

d = 0.2
a = 0.5
b = math.sqrt(2.4) - 0.5
m = (a + b)/2
print(b, m)
