# 3. Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.

num = int(input('enter number: '))
list = []

# вычисляем результат по данной формуле и складываем полученные значения в список
# округляем результат до 2х цифр после запятой
for n in range(1, num + 1):
    result = round((1 + 1 / n) ** n, 2)
    list.append(result)

print('list values:', list)

sum = 0

# проходим по списку и прибавляем значения, которые находятся в списке к переменно sum
for i in list:
    sum += i
    sum = round(sum, 2)

print('sum of all values from list:', sum)
