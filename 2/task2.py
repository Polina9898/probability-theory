# Вероятность того, что лампочка перегорит в течение первого дня эксплуатации, равна 0.0004. 
# В жилом комплексе после ремонта в один день включили 5000 новых лампочек. 
# Какова вероятность, что ни одна из них не перегорит в первый день? 
# Какова вероятность, что перегорят ровно две?

from math import factorial, pow, e as E

l = 5000.0 * 0.0004

def compute_prob(l, m):
    return pow(l, m) / factorial(m) * pow(E, -l)

print(compute_prob(l, 0))
print(compute_prob(l, 2))