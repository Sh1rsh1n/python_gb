# 1. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.


number = int(input('enter number: '))

num = 1
for item in range(number):
    num *= -3
    print(num)