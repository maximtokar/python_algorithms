"""
В диапазоне натуральных чисел от 2 до 99 определить,
сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
"""

numbers = [2, 3, 4, 5, 6, 7, 8, 9]
sum_line = []

for number in numbers:
    num = 0
    for i in range(2, 99+1):
        if i % number == 0:
            num += 1
    sum_line.append(num)

for i in range(0, len(numbers)):
    print(f'{numbers[i]:>5}', end='')
    print(f'{sum_line[i]:>5}')
