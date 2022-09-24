# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# метод выполняет проверку утверждения для всех значений предиката
# если одно из утверждений будет ложным, то метод вернет False
# если утверждение истинно для всех значений, то метод вернет True
def check_precicate(num):
    while num < 1:
        print('некорректное значение')
        num = int(input('введите число еще раз: '))
    else:
        for x in range(num):
            for y in range(num):
                for z in range(num):
                    left_side = not (x or y or z)
                    right_side = not x and not y and not z
                    if left_side != right_side:
                        return False
    return True


number = int(input('введите число: '))

if check_precicate(number):
    print('утверждения истинно для всех значений предиката')
else:
    print('утверждения ложно для одного из значений предиката')
