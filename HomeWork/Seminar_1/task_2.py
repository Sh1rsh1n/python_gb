# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
import random

print("*" * 20, "Check predicate", "*" * 20)

def check_predicate():      # метод проверяет истенность утверждения
    x = []
    for i in range(3):
        rnd = random.randint(-1000, 1000)   # рандомное число от -1000 до 1000
        if rnd >= 0:        # если число больше либо равно 0, добавляем в массив значение True
            x.append(True)
        else:               # если число меньше 0, добавляем в массив значение False
            x.append(False)
    print(x)                # проверка, что массив заполнен верно

    left = not (x[0] or x[1] or x[2])   # сравниваем все значения левой части
    right = not x[0] and not x[1] and not x[2]  # сравниваем все значения правой части
    return left == right        # сравниваем левую часть с правой и выводим результат


if check_predicate() == True:
    print("Утверждение истинно")
else:
    print("Утверждение ложно")