# Заявляется, что партия изготавливается со средним арифметическим 2,5 см. 
# Проверить данную гипотезу, если известно, что размеры изделий подчинены нормальному закону распределения. 
# Объем выборки 10, уровень статистической значимости 5%

# 2.51, 2.35, 2.74, 2.56, 2.40, 2.36, 2.65, 2.7, 2.67, 2.34


# Сигма не дана, значит используем критерий Стьюдента. 
# Нужно найтирасчетное значение критерия и сравнить с табличным
# Для alpha = 0.05 и объемом выборки из 10, т е 9 степеней свободы, 
# табличное значение критерия Стьюдента 1,833

import numpy as np
from scipy import stats


n = 10
alpha = 0.05
a = 2.5
x = np.array([2.51, 2.35, 2.74, 2.56, 2.40, 2.36, 2.65, 2.7, 2.67, 2.3])
mean_x = x.mean()
std_x = np.std(x, ddof=1)
t = (mean_x - a) / (std_x / np.sqrt(n))
print(stats.ttest_1samp(x, a))

# pvalue=0.6525010152046617, что больше alpha = 0.05, поэтому мы принимаем нулевую гипотезу, статистически значимые различий нет
