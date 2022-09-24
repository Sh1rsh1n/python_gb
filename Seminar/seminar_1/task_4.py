# 4. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.


print('=' * 20, 'Start program', '=' * 20)

num = float(input('enter number: '))
num = num * 10 % 10
if num != 0:
    print(int(num))
else:
    print('no')
