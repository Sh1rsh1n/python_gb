# 2. Создать список, длины n, значения формируются по формуле 3k + 1,
#    где k принимает значения от 1 до n включительно.


n = int(input('enter N: '))

list = []

for i in range(1, n + 1):
    list.append(3 * i + 1)

print(list)