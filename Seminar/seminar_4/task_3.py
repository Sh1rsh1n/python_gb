# 3. Задайте два числа. Напишите программу, которая найдёт
#    НОК (наименьшее общее кратное) этих двух чисел.
from math import gcd


def NOK(x, y):
    return (x * y) // gcd(x, y)

print(NOK(14,18))