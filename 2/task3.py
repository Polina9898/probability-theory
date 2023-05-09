# Монету подбросили 144 раза. Какова вероятность, что орел выпадет ровно 70 раз?

from math import factorial

def bernulli(n, k, p, q):
    return factorial(n) / (factorial(k) * factorial(n - k)) * (p ** k) * (q ** (n - k))

p = 0.5
n = 144
k = 70
q = 1 - p

print(bernulli(n, k, p, q))
