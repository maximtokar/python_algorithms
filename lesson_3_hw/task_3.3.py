"""
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
i_max = 0
i_min = array[0]
i_max_idx = 0
i_min_idx = 0

for i in range(len(array)):
    if array[i] > i_max:
        i_max = array[i]
        i_max_idx = i

for i in range(len(array)):
    if array[i] < i_min:
        i_min = array[i]
        i_min_idx = i

print(f'Old array:\t{array}')

array[i_max_idx], array[i_min_idx] = array[i_min_idx], array[i_max_idx]

print(f'New array:\t{array}')
