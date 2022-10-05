# 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности в том же порядке.
# in
# 7
# out
# [4, 5, 3, 3, 4, 1, 2]
# [5, 1, 2]
import random

# функция, заполняет и возвращает список случайных значений
def fill_list(capacity):
    ls = []
    if not str(capacity).isdigit():
        print('incorrect value')
        return ls

    for i in range(capacity):
        ls.append(random.randint(0, capacity))
    return ls

start_list = fill_list(10)

print('random values list =>', start_list)

# Функция, принимает на вход список, проходим по всем элементам списка,
# все значения, которые являются уникальными в данном списке, добавляем в новый список.
def list_without_duplicates(num_list: list):
    ls = []
    for i in num_list:
        if num_list.count(i) == 1:  # проверяем, что значение встречается, только 1 раз
            ls.append(i)
    return ls

print('without duplicates list =>', list_without_duplicates(start_list))