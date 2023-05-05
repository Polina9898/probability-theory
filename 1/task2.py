# На входной двери подъезда установлен кодовый замок, содержащий десять кнопок с цифрами от 0 до 9. 
# Код содержит три цифры, которые нужно нажать одновременно. Какова вероятность того, что человек,
# не знающий код, откроет дверь с первой попытки?

import math

#      10!
# _______________
#    (10 - 3)!

combs = math.factorial(10) / math.factorial(10 - 3)

print(1 / combs)