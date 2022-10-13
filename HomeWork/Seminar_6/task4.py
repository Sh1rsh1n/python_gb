'''
4. Функция принимает в качестве аргументов строки в формате «Имя Фамилия», 
возвращает словарь, ключи — первые буквы фамилий, 
значения — словари, реализованные по схеме предыдущего задания.
'''

import console

def add_employee_to_dict(data_emp, dict_in):
	emp = data_emp.split()
	for i in emp:
		if not i.isalpha():	# провека на корректность ввода строки(без цифр)
			print('Incorrect employee name!')
			return dict_in

	first_letter = lambda s: s[:1].upper()		# лямбда, отделяет первую букву в строке и делает ее заглавной
	
	if not first_letter(emp[1]) in dict_in:
		dict_in[first_letter(emp[1])] = {first_letter(emp[0]):[' '.join(emp)]}		# если такого ключа нет в словаре, то создаем ключ с данным значением из входящего списка
	elif not first_letter(emp[0]) in dict_in[first_letter(emp[1])]:
		dict_in[first_letter(emp[1])][first_letter(emp[0])] = {first_letter(emp[0]):[' '.join(emp)]}
	else:
		dict_in[first_letter(emp[1])][first_letter(emp[0])].append(' '.join(emp))	# иначе, добавляем значение из входящего списка, в список по данному ключу словаря
	
	sorted_tuple = sorted(dict_in.items(), key=lambda x: x[0])	# сортируем значения словаря по ключу, с помощью кортежа
	return dict(sorted_tuple)		# преобразуем кортеж обратно в словарь и возвращаем значения
	
	
def main():
	dict_emp = {}
	while True:
		data = input('enter employee name and surname or empty string for exit: ')
		if not data:
			break

		# console.clear()		# очистка консоли, только для Pythonista iOS, закомментировать в дргуих ОС
		dict_emp = add_employee_to_dict(data, dict_emp)
		print(dict_emp)

main()
