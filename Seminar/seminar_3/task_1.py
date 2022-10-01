import random


def magic(count, find_num2):
    if count < 0:
        return "Все плохо"
    ls = random.sample(range(count * 2), count)
    print(ls)

    if find_num2 in ls:
        return "Yes"
    return "No"


num1 = int(input("Введите число: "))
num2 = int(input("Введите число: "))
print(magic(num1, num2))