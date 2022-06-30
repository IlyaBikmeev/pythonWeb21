'''
Дается число n
Дается список из n слов, каждое с новой строки.
Посчитайте какое слово сколько раз встречается
'''
'''
n = int(input())
frequency = {} #Словарь для частоты слов. Ключ - слово, значение - частота.

for i in range(n):
    word = input()
    if word not in frequency:
        frequency.update({word : 1}) #Добавляем новое слово в словарь с частотой 1
    else:
        frequency.update({word : frequency[word] + 1}) #Увеличиваем частоту данного слова на 1

for key, value in frequency.items():
    print('Слово {} встречается {} раз'.format(key, value))
'''

text = input()
frequency = {}

for word in text.split():
    if word in frequency:
        frequency.update({word : frequency[word] + 1})
    else:
        frequency.update({word : 1})

for key, value in frequency.items():
    print('Слово {} встречается {} раз'.format(key, value))