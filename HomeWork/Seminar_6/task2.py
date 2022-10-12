'''
2. Для чисел в пределах от 20 до N найти числа, кратные 20 или 21. Use comprehension.
'''
import random


# ВАРИАНТ 1
# Функция, проверяет кратность данного числа, числам 20 и 21
def check_div_nums(num):
	return not num % 20 or not num % 21

# Функция, заполняет список числами от 20 до указанного значения'''
def fill_list(range_max_value):
	return [i for i in range(20, range_max_value)]

list_in = fill_list(100)
print(f'source list: \n{list_in} ')

list_out = [i for i in list_in if check_div_nums(i)]
print(f'output list: \n{list_out}')


print('=' * 50)

# ВАРИАНТ 2 (с генерацией списка случайных чисел)
range_max_value = int(input('enter max range: '))

div_nums = lambda num: not num % 20 or not num % 21

list_in = [random.randint(1, 100) for _ in range(range_max_value)]
print(f'output list: \n{list_in}')

list_out = [i for i in list_in if div_nums(i)]
print(f'output list: \n{list_out}')