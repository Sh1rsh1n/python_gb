'''
1. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента. Use comprehension.
in
9
out
[15, 16, 2, 3, 1, 7, 5, 4, 10]
[16, 3, 7, 10]
'''
import random

# ВАРИАНТ 1 без функции
num = int(input('enter range of numbers: '))

list_in = [random.randint(-100, 100) for _ in range(num)]   # сгенерировали список случайных чисел
print(list_in)

''' 
Итерируемся по списке в диапазоне от элемента с индексом 1, до значения размера списка.
Сравниваем отдельно взятый элемент с предыдущим и если условия верно, 
записываем этот элемент в новый список.
'''
list_out = [list_in[i] for i in range(1, len(list_in)) if list_in[i] > list_in[i - 1]]
print(list_out)

print('=' * 40)
# ВАРИАНТ 2 с функцией
def compare_current_with_previous(capacity: int):
    ls = [random.randint(-100, 100) for _ in range(capacity)]
    print(ls)
    return [ls[i] for i in range(1, len(ls)) if ls[i] > ls[i - 1]]

print(compare_current_with_previous(10))