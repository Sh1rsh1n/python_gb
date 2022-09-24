# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.

print('=' * 20, 'Start program', '=' * 20)

max_value = 0
for item in range(5):
    num = int(input('enter number: '))
    if max_value < num:
        max_value = num

print(max_value)