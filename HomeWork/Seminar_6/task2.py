'''
2. Для чисел в пределах от 20 до N найти числа, кратные 20 или 21. Use comprehension.
in
100

out
[20, 21, 40, 42, 60, 63, 80, 84, 100]
'''
import random


# Функция, проверяет кратность данного числа, числам 20 и 21
check_div_nums = lambda num: not num % 20 or not num % 21

# Функция, принимает список чисел, проверяет их кратность 20 и 21, и возвращет новый список
def list_num_from_20_to_N(list_in):
	return [i for i in list_in if check_div_nums(i)]

range_max_value = int(input('enter max range of numbers: '))
list_in = [i for i in range(20, range_max_value + 1)]

list_out = list_num_from_20_to_N(list_in)
print(f'output list: \n{list_out}')
