'''
3. Написать функцию, аргументы имена сотрудников, возвращает словарь, ключи — первые буквы имён,
значения — списки, содержащие имена, начинающиеся с соответствующей буквы.

in
"Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"

out

{'А': ['Алина'], 'Б': ['Бибочка'], 'И': ['Иван', 'Илья'], 'М': ['Марина', 'Мария'], 'П': ['Петр', 'Петр']}
'''
# import console								# очистка консоли, только для Pythonista iOS, закомментировать в дргуих ОС


def employee_dict(name_emp, dict_in):
	if not name_emp.isalpha():						# провека на корректность ввода строки(без цифр)
		print('Incorrect employee name!')
		return dict_in

	first_letter = lambda s: s[:1].upper()					# лямбда, отделяет первую букву в строке и делает ее заглавной
	
	if not first_letter(name_emp) in dict_in:
		dict_in[first_letter(name_emp)] = [name_emp]				# если такого ключа нет в словаре, то создаем ключ с данным значением из входящего списка
	else:
		dict_in[first_letter(name_emp)].append(name_emp)			# иначе, добавляем значение из входящего списка, в список по данному ключу словаря
	
	sorted_tuple = sorted(dict_in.items(), key=lambda x: x[0])		# сортируем значения словаря по ключу, с помощью кортежа
	return dict(sorted_tuple)										# преобразуем кортеж обратно в словарь и возвращаем значения


def main():
	dict_emp = {}
	while True:
		name = input('enter employee name or empty string for exit: ')
		if not name:
			break

		# console.clear()										# очистка консоли, только для Pythonista iOS, закомментировать в дргуих ОС
		dict_emp = employee_dict(name, dict_emp)
		print(dict_emp)

main()
