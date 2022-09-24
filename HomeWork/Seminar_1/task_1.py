# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# метод, вычисляет цифру дня недели
def day_of_week():
    number = int(input('введите число: '))

    # проверка ввода числа меьнше либо равного 0
    while(number <= 0):
        print('некорректное значение, повторите ввод числа')
        number = int(input('введите число: '))
    else:
        if 0 < number < 8:
            return number
        elif number % 7 == 0:
            return 7
        else:
            return number % 7


# метод, выводит в консоль результат проверки, является ли день выходным.
def check_weekend(num):
    if 5 < num < 8:
        print("это выходной")
    else:
        print("это рабочий день")


dayNumber = day_of_week()

check_weekend(dayNumber)


