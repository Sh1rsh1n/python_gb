import re


def file_to_list_words(path):
    '''Функция, обрабатывает текст входящего файла и удаляет все строки, в которых есть значение "абв" '''
    try:
        with open(path, encoding='utf-8') as file:
            text = file.read()
            print(text)
            '''
            В лямбда выражении используем метод split модуля re для преобразования текста в массив строк,
            далее проходим по всем элементам массива отфильтруем те элементы, в которых нет символов "абв" 
            и преобразуем в новый лист.
            '''
            text_mod = list(filter(lambda index: 'абв' not in index.lower(), re.split(r'[.,\s]*\s', text)))
            text_mod = ' '.join(text_mod).lower()
            print(text_mod)
    except FileNotFoundError:
        '''В случае, если указан неверный путь, выводим сообщение об этом.'''
        print('Invalid file path...')


file_to_list_words('text.txt')      # вывод результата как в примере, без слов в которых есть "абв"
# file_to_list_words('dasdc.txt')   # ошибка
