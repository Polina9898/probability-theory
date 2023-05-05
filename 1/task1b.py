# Из колоды в 52 карты извлекаются случайным образом 4 карты.
# б) Найти вероятность, что среди 4-х карт окажется хотя бы один туз.

import math

total_cards = 52
aces_count = 4

select_count = 4
select_ace_count = 1

def comb(of, by):
    return math.factorial(of) / (math.factorial(by) * math.factorial(of - by))

ace_comb = comb(aces_count, select_ace_count)
other_comb = comb(total_cards - aces_count, select_count - select_ace_count)

select_ace_comb = ace_comb * other_comb

all_select_comb = comb(total_cards, select_count)

print(select_ace_comb / all_select_comb)