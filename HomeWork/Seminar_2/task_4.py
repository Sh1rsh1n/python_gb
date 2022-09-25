# * 4. Напишите программу, которая принимает на вход 2 числа.
# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях(не индексах).
# Position one: 1
# Position two: 3
# Number of elements: 5
# -> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
# -> 15

# функция, заполняет список цифрами от -N до N,
# где N - число указанное при вводе
def fill_list():
    num = int(input('enter amount of elements [-N,N]: '))
    list = []
    for item in range(-num, num):
        list.append(item)
    return list

list_of_digits = fill_list()
print(list_of_digits)

# функция, принимает на вход список
# выполняет умножение двух чисел, на указанных позиция
def multiply_two_numbers(list):
    first_num = 0
    second_num = 0
    while first_num <= 0 or second_num <= 0:
        first_num = int(input('enter first possition: '))
        second_num = int(input('enter second possition: '))
        print('=' * 40)
    else:
        return list[first_num - 1] * list[second_num - 1]

print('multiple two numbers = ', multiply_two_numbers(list_of_digits))