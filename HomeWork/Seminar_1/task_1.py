# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

import random

print("*" * 20, "Day of week", "*" * 20)

def day_of_week(num): # метод, вычисляет цифру дня недели
    if num < 8:
        return num
    elif num % 7 == 0:
        return 7
    else:
        return num % 7

def check_weekend(num): # метод, выводит в консоль результат проверки, является ли день выходным.
    if 5 < num < 8:
        print("this day is weekend")
    else:
        print("this day is workday")


number = random.randint(1, 10)  # просто рандомное число от 1 до 10
print(number)                   # выводим рандомное число

check_weekend(day_of_week(number))