# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).


def show_coord(num):
    if 1 > num > 4:
        print('incorrect value')
    else:
        if num == 1:
            print('All points 1st quater:')
            for i in range(1, 11):
                for j in range(1, 11):
                    print(f'x = {i}, y = {j}')
        elif num == 2:
            print('All points 2nd quater:')
            for i in range(-1, -11, -1):
                for j in range(1, 11):
                    print(f'x = {i}, y = {j}')
        elif num == 3:
            print('All points 3rd quater:')
            for i in range(-1, -11, -1):
                for j in range(-1, -11, -1):
                    print(f'x = {i}, y = {j}')
        elif num == 4:
            print('All points 4th quater:')
            for i in range(1, 11):
                for j in range(-1, -11, -1):
                    print(f'x = {i}, y = {j}')


print('=' * 20, 'Start program', '=' * 20)

print(
    """enter number from 1 to 4:
    1. 1st quater points:
    2. 2nd quater points:
    3. 3rd quater points:
    4. 4th quater points:
    """
)
digit = int(input('>> '))

show_coord(digit)
