# 4.* Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# in
# 5
# out
# [5.16, 8.62, 6.57, 7.92, 9.22]
# Min: 0.16, Max: 0.92. Difference: 0.76
import random

# Функция, генерирует произвольные вещественные числа,
# после округления до 2х чисел после запятой, добавляет число в новый список
def fill_list(capacity: int):
    if capacity <= 0:
        print('Incorrect input value. Method "fill_list"')
        return
    ls = []
    for i in range(capacity):
        num = random.randint(0, 10) + random.random()
        ls.append(round(num, 2))
    print('start list:', ls)
    return ls

# Функция, принимает на вход список, в цикле проходим по всем значениям
# отделяем дробную часть и записываем это значение в новый список
def split_fraction(num_list: list):
    if num_list is None:
        print('Invalid input type. Method "split_fraction"')
        return
    ls = []
    for i in num_list:
        ls.append(round(i % 1, 3))
    print(f'list after split: {ls}')
    return ls

# Функция, принимает список, находит минимальное, максимальное значения и их разницу
def min_max_diff(num_list: list):
    if num_list is None:
        print('Invalid input type. Method "min_max_diff"')
        return
    max = num_list[0]
    min = num_list[1]
    for i in num_list:
        if i > max:
            max = i
        if i < min:
            min = i
    print(f'Min: {min}, Max: {max}, Difference: {round(max - min, 2)}')

start_list = fill_list(5)

list_after_split = split_fraction(start_list)

min_max_diff(list_after_split)
