# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).


import random


# функция, создает список чисел в произвольном порядке, размер задает пользователь.
# В цикле проходим по элементам, которые находятся на четных индексах(нечетных позициях)
# и каждую итерацию суммируем в переменную summa значение находящееся по указанному индексу в списке.
def sum_odd_poss_elems(capacity: int):
    if capacity < 0:
        print('Incorrect input value')
        return

    ls = random.sample(range(-100, 100), capacity)
    print('List nums:', ls)
    summa = 0
    for i in range(0, len(ls), 2):
        summa += ls[i]
    return summa


print(f'Sum nums on odd possitions: {sum_odd_poss_elems(-5)}')
