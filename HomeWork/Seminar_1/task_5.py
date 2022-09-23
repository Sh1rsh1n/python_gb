# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.

import math
import random

print('=' * 20, 'GET DISTANCE', '=' * 20)

# метод принимает на вход два кортежа, которые содержать рандомные координаты двух точек
# и вычисляет расстояние между двумя точками по теореме Пифагора
def get_dist(point1, point2):
    print(f'Point one: {point1} \nPoint two: {point2}')
    return math.sqrt(((point1[0] - point2[0]) ** 2) + ((point1[1] - point2[1]) ** 2))

point_one = ((random.randint(-10, 10)), (random.randint(-10, 10)))
point_two = ((random.randint(-10, 10)), (random.randint(-10, 10)))

print('distance beetwin two points: ', "%.2f" % get_dist(point_one, point_two))