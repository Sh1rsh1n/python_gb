'''5. ** Реализовать функцию, возвращающую n шуток, сформированных из трех случайных слов, взятых из трёх списков (по одному из каждого)
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью", "когда-то", "где-то"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
in 
10 True
out

['дом ночью мягкий', 'огонь завтра зеленый', 'лес вчера яркий', 'автомобиль сегодня веселый', 'город позавчера утопичный']
'''

from random import choice

dict_words = {'nouns': ["автомобиль", "лес", "огонь", "город", "дом"], 'adverbs': ["сегодня", "вчера", "завтра", "позавчера", "ночью", "когда-то", "где-то"], 'adjectives': ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]}

def joke_creater(dict_in):
	return [choice(dict_in[key]) for key in dict_in]

def create_joke_list(amount):
	ls = []
	for i in range(amount):
		ls.append(' '.join(joke_creater(dict_words)))
	return ls
		


ls = create_joke_list(10)

print(ls)