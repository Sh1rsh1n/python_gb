# 5. ** Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.


def fib_negative(num: int):
    x = y = 1
    num_list = [0]
    for i in range(num):
        num_list.append(x)
        num_list.insert(0, x * (-1) ** i)
        x, y = y, x + y
    return num_list

print(fib_negative(8))

