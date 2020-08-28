"""
В массиве найти максимальный отрицательный элемент.
Вывести на экран его значение и позицию в массиве.
Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
Это два абсолютно разных значения.
"""

import random

SIZE = 10
MIN_ITEM = -50
MAX_ITEM = 50
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print(f'Массив:\n{array}')

negatives = []

for i in array:
    if i < 0:
        negatives.append(i)

max_neg = negatives[0]

for i in negatives:
    if i > max_neg:
        max_neg = i

print(f'Наибольшее отрицательное число: {max_neg}')
