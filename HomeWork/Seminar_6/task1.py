'''
1. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента. Use comprehension.
in
9
out
[15, 16, 2, 3, 1, 7, 5, 4, 10]
[16, 3, 7, 10]
'''

def compare_current_with_previous_nums(capacity: int):
    ls = [random.randint(-100, 100) for _ in range(capacity)]   # генерируем список случайных чисел
    print(ls)
    return [ls[i] for i in range(1, len(ls)) if ls[i] > ls[i - 1]]  # сравниваем данное значение с предыдущем, и если условие выполняется добавляем его в новый список

num = int(input('enter max range of numbers: '))
print(compare_current_with_previous_nums(num))
