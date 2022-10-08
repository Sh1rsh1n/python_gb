from random import choice


def fill_list(num):
    arr = [i for i in range(num + 1)]
    arr.remove(choice(arr))
    return arr

def check_number(array):
    for i in range(1, len(array)):
        if array[i] - 1 != array[i - 1]:
            return array[i] - 1
    return -1
list_1 = fill_list(5)
print(list_1)
print(check_number(list_1))