"""
1). Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых трех уроков.
Примечание. Идеальным решением будет:
● выбрать хорошую задачу, которую имеет смысл оценивать,
● написать 3 варианта кода (один у вас уже есть),
● проанализировать 3 варианта и выбрать оптимальный,
● результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили замеры),
● написать общий вывод: какой из трёх вариантов лучше и почему.
"""

"""
7. Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство:
1+2+...+n = n(n+1)/2, где n — любое натуральное число.
"""

import timeit
import cProfile


# способ 1 - рекурсия
def sum_rec(n):
    if n == 1:
        return n
    else:
        result = n + sum_rec(n - 1)
        return result


# способ 2 - цикл for
def sum_for_loop(n):
    result = 0
    for i in range(n + 1):
        result += i
    return result


# способ 3 - цикл while
def sum_while_loop(n):
    i = 0
    result = 0
    while i <= n:
        result += i
        i += 1
    return result


# замеры:
print(timeit.timeit('sum_rec(10)', number=1000, globals=globals()))     # 0.002150836999999999
print(timeit.timeit('sum_rec(50)', number=1000, globals=globals()))     # 0.017512200999999998
print(timeit.timeit('sum_rec(100)', number=1000, globals=globals()))    # 0.03712977299999999
print(timeit.timeit('sum_rec(200)', number=1000, globals=globals()))    # 0.054110147

cProfile.run('sum_rec(10)')     # ncalls = 10/1
cProfile.run('sum_rec(50)')     # ncalls = 50/1
cProfile.run('sum_rec(100)')    # ncalls = 100/1

print(timeit.timeit('sum_for_loop(10)', number=1000, globals=globals()))     # 0.0009919929999999966
print(timeit.timeit('sum_for_loop(50)', number=1000, globals=globals()))     # 0.0031044290000000058
print(timeit.timeit('sum_for_loop(100)', number=1000, globals=globals()))    # 0.005771288999999999
print(timeit.timeit('sum_for_loop(200)', number=1000, globals=globals()))    # 0.011608925999999992

cProfile.run('sum_for_loop(10)')
cProfile.run('sum_for_loop(50)')
cProfile.run('sum_for_loop(100)')

print(timeit.timeit('sum_while_loop(10)', number=1000, globals=globals()))     # 0.0010356399999999766
print(timeit.timeit('sum_while_loop(50)', number=1000, globals=globals()))     # 0.00480998299999999
print(timeit.timeit('sum_while_loop(100)', number=1000, globals=globals()))    # 0.010269112000000025
print(timeit.timeit('sum_while_loop(200)', number=1000, globals=globals()))    # 0.020988279999999998

cProfile.run('sum_while_loop(10)')
cProfile.run('sum_while_loop(50)')
cProfile.run('sum_while_loop(100)')

"""
Вывод: замеры производились для значений 10, 50, 100 и 200. 3 варианта функции: рукурсия, цикл for и цикл while.
При использовании рекурсии количество вызовов соответствует входному значению (n). 
При использовании циклов количество вызовов не зависит от входных данных (=1).

Для всех трех вариантов наблюдается линейная зависимость (O(n)) при отличающихся коэффициентах.
Наиболее низний коэффициент - у функции sum_for_loop. Данный вариант - наиболее предпочтителен.
"""
