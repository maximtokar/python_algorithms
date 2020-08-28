"""
Пользователь вводит данные о количестве предприятий,
их наименования и прибыль за 4 квартал (т.е. 4 числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.
"""

from collections import namedtuple

Firms = namedtuple('Firms', 'name, q1, q2, q3, q4, sum')

number = int(input('Number of firms: '))

firm_list = []
for i in range(number):
    name = input('Enter the name: ')
    profit = []
    for el in range(4):
        a = int(input(f'Profit for {el + 1} quarter: '))
        profit.append(a)
    firm_list.append(Firms(name, *profit, sum(profit)))

total_profit = 0
for i in range(number):
    total_profit += firm_list[i].sum

average = total_profit / number

print(f'Average profit: {average}')

for i in range(number):
    if firm_list[i].sum > average:
        print(f'Profit of {firm_list[i].name} is above the average')
    else:
        print(f'Profit of {firm_list[i].name} is about or below the average')
