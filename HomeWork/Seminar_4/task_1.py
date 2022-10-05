# 1. Вычислить число c заданной точностью d
# in
# Enter a real number: 9
# Enter the required accuracy '0.0001': 0.000001
#
# out
# 9.000000
import re
from decimal import Decimal

# Функция, проверяет ввод значения
# Если значение - это какие-либо число,
# то функция вернет True.
def check_digit_value(val):
    val = re.split(r'[.]', val)
    if ''.join(val).isdigit():
        return True
    return False

# Функция, принимает два значения, выполняет проверку ввода значения,
# с помощью функций класса Decimal, преобразуем число до указанной точности
def num_accuracy(num, d):
    if not check_digit_value(num) or not check_digit_value(d):
        print('incorrect value')
        return -1
    num = Decimal(num)
    num = num.quantize(Decimal(str(d)))
    return num


num = input('Enter a real number: ')
d = input('Enter accuracy: ')

result = num_accuracy(num, d)

print("result:", result)
