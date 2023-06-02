# Известно, что генеральная совокупность распределена нормально со средним квадратическим отклонением, равным 16.
# Найти доверительный интервал для оценки математического ожидания a с надежностью 0.95, 
# если выборочная средняя M = 80, а объем выборки n = 256.

import numpy as np
from scipy import stats
import math

sigma = 16
n = 256
m = 80
p = 0.95
alpha = 0.05
z = stats.t(n - 1).ppf(1 - alpha / 2)
print(f"interval [ {m-z*(sigma/math.sqrt(n))} ; {m+z*(sigma/math.sqrt(n))} ]")

