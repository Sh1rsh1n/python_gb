# 5. Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.


print('=' * 20, 'Start program', '=' * 20)

num = int(input("enter number: "))

if (num % 5 == 0 and num % 10 == 0 or num % 15) and num % 30 != 0:
    print('yes')
else:
    print('no')