# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.


# метод вычисляет расстояние между двумя точками по теореме Пифагора
# просим пользователя ввести координаты точек, получаем и возвращаем результат вычислений
def get_dist():
    point_one_x = int(input('enter coordinate X1: '))
    point_one_y = int(input('enter coordinate Y1: '))
    point_two_x = int(input('enter coordinate X2: '))
    point_two_y = int(input('enter coordinate Y2: '))
    return (((point_one_x - point_two_x) ** 2) + ((point_one_y - point_two_y) ** 2)) ** 0.5


print('distance beetwin two points: ',
      "%.2f" % get_dist())  # выводим резльтат вычислений, округяем до 2х цифр после запятой
