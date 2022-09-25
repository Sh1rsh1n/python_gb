# 5. ** Реализуйте алгоритм перемешивания списка. Без функции shuffle из модуля random.
# 10
# -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# -> [0, 7, 6, 3, 4, 2, 9, 5, 1, 8]
import random

# функция, заполняет список цифрами до значения переданного в аргументе
def fill_list(num):
    list = []
    for item in range(num):
        list.append(item)
    return list

# функция, перемешивает все числа в данном списоке
def shuffle_list(list):
    for i in list:
        random_poss = random.randint(0, len(list) - 1)  # рандомная позиция от 0 до последнего индекса списка
        temp = list[i]                                  # переменной temp присвоили значение переменной по индексу i
        list[i] = list[random_poss]                     # переменной с индексом i присвоили значение по индексу random_poss
        list[random_poss] = temp                        # переменной с индексом random_poss присвоили значение переменной temp
    return list


sorted_list = fill_list(10)

print('sorted list: ', sorted_list)

shuffle_after_list = shuffle_list(sorted_list)

print('shuffle list: ', shuffle_after_list)