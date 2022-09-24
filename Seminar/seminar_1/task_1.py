# Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.

print('=' * 20, 'Start program', '=' * 20)

first = int(input('enter number: '))
second = int(input('enter number: '))


if first == second ** 2 or second == first ** 2:
    print('yes')
else:
    print('no')
