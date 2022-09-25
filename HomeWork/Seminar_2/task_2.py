# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# 1 - 1 * 1, 2 - 1 * 2, 3 - 1 * 2 * 3, 4 - 1 * 2 * 3 * 4 и т.д.
# - 4 -> [1, 2, 6, 24]
# - 6 -> [1, 2, 6, 24, 120, 720]

# решение как в примере
value = int(input('enter number: '))

list = []
result = 1
for i in range(1, value + 1):
    result *= i
    list.append(result)

print(value, ' -> ', list)


# решение через рекурсию
# (только вывод не соображу, как сделать, также как в примере)
def factorial(num):
    result = 1
    if num == 0 or num == 1:
        print(f'[{result}', end='] ')
        return result
    else:
        result = num * factorial(num - 1)
        print(f'[{result}', end='] ')
        return result


factorial(value)
