"""
Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как коллекция, элементы которой — цифры числа.
Например, пользователь ввёл A2 и C4F.
Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""

from collections import deque

a_1 = list(deque(input('Enter the number #1 (0 - F): ').upper()))
a_2 = list(deque(input('Enter the number #2 (0 - F): ').upper()))

hex_to_dec = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'A': 10,
    'B': 11,
    'C': 12,
    'D': 13,
    'E': 14,
    'F': 15
}


def convert_to_dec(x):
    result = 0
    power = len(x) - 1
    for i in x:
        result += hex_to_dec[i] * (16 ** power)
        power -= 1
    return result


def convert_to_hex(x):
    hex_result = []
    while x != 0:
        dec_result = x % 16
        for k, v in hex_to_dec.items():
            if v == dec_result:
                hex_result.insert(0, k)
        x = x // 16
    return hex_result


sum_dec = convert_to_dec(a_1) + convert_to_dec(a_2)
mul_dec = convert_to_dec(a_1) * convert_to_dec(a_2)
print(f'Sum: {convert_to_hex(sum_dec)}')
print(f'Multiplied: {convert_to_hex(mul_dec)}')
