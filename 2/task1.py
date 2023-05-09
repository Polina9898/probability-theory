# Вероятность того, что стрелок попадет в мишень, выстрелив один раз, равна 0.8. 
# Стрелок выстрелил 100 раз. Найдите вероятность того, что стрелок попадет в цель ровно 85 раз.

from math import factorial

k = 85
n = 100
p = 0.8
q = 1 - p

def bernulli(n, k, p, q):
    return factorial(n) / (factorial(k) * factorial(n - k)) * (p ** k) * (q ** (n - k))

print(bernulli(n, k, p, q))