'''
3. * Создайте программу для игры в "Крестики-нолики". Поле 3x3. Игрок - игрок, без бота.
'''

import random

field = list(range(1, 10))

# отображение игрового поля
def show_board(field):
	print('*' * 13)
	for i in range(3):
		print('*', field[0 + i * 3], '*', field[1 + i * 3], '*', field[2 + i * 3], '*')
		print('*' * 13)

# ввод значения пользователем
def player_input(player_action):
	value = False
	while not value:
		answer = input('When set ' + player_action + '? ')
		try:
			answer = int(answer)
		except:
			print('incorrect input, enter a number')
			continue
		if answer >= 1 and answer <= 9:
			if (str(field[answer - 1]) not in '\U0000274C'):
				field[answer - 1] = player_action
				value = True
			elif (str(field[answer - 1]) not in '\U00002B55'):
				field[answer - 1] = player_action
				value = True
			else:
				print('this position is busy')
		else:
			print('incorrect input, enter numbers from 1 to 9.')

# проверка результата игры
def check_win(field):
	win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
	for index in win_coord:
		if field[index[0]] == field[index[1]] == field[index[2]]:
			return field[index[0]]
	return False

# выбор, кто первый будет начинать игру
def player_starter():
	return random.choice(['\U0000274C', '\U00002B55'])


def main(field):
	count = 0
	player = player_starter()
	win = False
	while not win:
		show_board(field)
		if player == '\U0000274C':
			player_input(player)
			player = '\U00002B55'
		else:
			player_input(player)
			player = '\U0000274C'
		count += 1
		if count > 4:
			c_w = check_win(field)
			if c_w:
				print(c_w, 'WIN!!!')
				win = True
				break
		if count == 9:
			print('Drawn!')
			break
	show_board(field)



main(field)
