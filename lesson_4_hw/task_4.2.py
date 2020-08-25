"""
2). Написать два алгоритма нахождения i-го по счёту простого числа.
Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
Проанализировать скорость и сложность алгоритмов.

Первый — с помощью алгоритма «Решето Эратосфена».
Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков.
Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.

Второй — без использования «Решета Эратосфена».
"""

import timeit
import cProfile


def prime_test(function):
    prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
                     101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197,
                     199]
    for el, item in enumerate(prime_numbers):
        if function(el + 1) == item:
            print(el, 'True')
        else:
            print(el, 'Fail')


def prime(n):
    i = 1
    prime_i = 2

    while n > i:
        prime_i += 1
        for el in range(2, prime_i):
            if prime_i % el == 0:
                break
        else:
            i += 1
    return prime_i


def sieve(n):
    num = n * 1000
    array = [i for i in range(num)]
    array[1] = 0
    for i in range(2, num):
        if array[i] != 0:
            j = i + i
            while j < num:
                array[j] = 0
                j += i
    result = [i for i in array if i != 0]
    return result[n-1]


# prime_test(prime)
# prime_test(sieve)

print(timeit.timeit('prime(10)', number=100, globals=globals()))     # 0.002969467999999996
print(timeit.timeit('prime(100)', number=100, globals=globals()))     # 0.24026788200000002
print(timeit.timeit('prime(1000)', number=100, globals=globals()))    # 39.446295354

cProfile.run('prime(10)')     # percall = 0
cProfile.run('prime(100)')    # percall = 0.004
cProfile.run('prime(1000)')   # percall = 0.410

print(timeit.timeit('sieve(10)', number=100, globals=globals()))        # 0.521265039
print(timeit.timeit('sieve(100)', number=100, globals=globals()))       # 5.591758294
print(timeit.timeit('sieve(1000)', number=100, globals=globals()))      # 76.587482532

cProfile.run('sieve(10)')     # percall = 0.005
cProfile.run('sieve(100)')    # percall = 0.074
cProfile.run('sieve(1000)')   # percall = 0.842

"""
Вывод: в обоих случаях - квадратичная сложность алгоритма.
Количество выховов не зависит от входящих данных. Существенно возрастает время на одно выполнение функции.
Способ решения без решета - более оптимален.
"""