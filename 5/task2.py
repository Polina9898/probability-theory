# Проведите тест гипотезы. Утверждается, что шарики для подшипников, изготовленные автоматическим станком, 
# имеют средний диаметр 17 мм.

# Используя односторонний критерий с α=0,05, проверить эту гипотезу, 
# если в выборке из n=100 шариков средний диаметр оказался равным 17.5 мм, а дисперсия известна и равна 4 кв. мм.

# H0 : mu = mu0
# H1 : mu > mu0

import math


alfa = 0.05
sigma = 4
n = 100

se = sigma / math.sqrt(n)
z = (17.5 - 17) / se
zt = 1.6 # 100 - 0.05 = 0.95 

print(f"расчетное значение {z} попадает в область принятия гипотезы H0, средний диаметр 17 мм при α=0,05")