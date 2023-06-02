# Рост дочерей 175, 167, 154, 174, 178, 148, 160, 167, 169, 170

# Рост матерей  178, 165, 165, 173, 168, 155, 160, 164, 178, 175

# Используя эти данные построить 95% доверительный интервал для разности среднего роста родителей и детей.


import numpy as np
from scipy import stats
import math

a = np.array([175, 167, 154, 174, 178, 148, 160, 167, 169, 170])
b = np.array([178, 165, 165, 173, 168, 155, 160, 164, 178, 175])

mean_a = np.mean(a)
mean_b = np.mean(b)

delta = mean_a - mean_b

D_a = np.var(a, ddof=1)
D_b = np.var(b, ddof=1)
D = (D_a + D_b) / 2

SE = np.sqrt(D / len(a) + D / len(b))
t = stats.t.ppf(0.95, 18)
print(f"interval [ {delta - t * SE} ; {delta + t * SE} ]")


