from random import choice


def polynomial(num):
    if num < 1:
        return 0

    poly = ''
    num_list = range(0,10)

    with open("poly.txt", 'a', encoding='utf-8') as my_file:
        for i in range(num, 0, -1):
            value = choice(num_list)
            if value:
                poly += f"{value}*x^{i} {choice('-+')} "

        my_file.write(f"{poly}{choice(num_list)} = 0\n")


for _ in range(3):
    polynomial(int(input('enter a number from 0 to 5: ')))