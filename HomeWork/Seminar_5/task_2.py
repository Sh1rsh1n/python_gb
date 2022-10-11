'''
2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
Входные и выходные данные хранятся в отдельных текстовых файлах.
'''

'''функция сжатия данных'''
def compress_file(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            text = file.read()
    except FileNotFoundError:
        print('Invalid file path...')

    encode = ''
    i = 0
    while i < len(text):
        count = 1
        while i + 1 < len(text) and text[i] == text[i + 1]:     # цикл выполняется пока есть текст и данный символ равен следующему символу
            count += 1
            i += 1
        encode += str(count) + text[i]      # запись/сжатие данных
        i += 1

    with open('compressied_file.txt', 'w', encoding='utf-8') as file:
        file.write(encode)



'''функция распаковки данных'''
def decompress_file(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            text = file.read()
    except FileNotFoundError:
        print('Invalid file path...')

    decode = ''
    count = ''
    for index in text:
        if index.isdigit():
            count += index
        else:
            decode += index * int(count)
            count = ''

    print(f'out:\n{decode}')


compress_file('source_text.txt')
decompress_file("compressied_file.txt")



