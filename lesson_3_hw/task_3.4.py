"""
Определить, какое число в массиве встречается чаще всего.
"""

import random

SIZE = 100
MIN_ITEM = 1
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print(f'Массив:\n{array}')
print(f'Уникальные значения:\n{set(array)}')

x_count_max = 0

for i in set(array):
    x_count = 0
    for item in array:
        if i == item:
            x_count += 1
    if x_count > x_count_max:
        x_count_max = x_count
        x_max = i

print(f'Наиболее часто встречается число {x_max} - {x_count_max} раз')
