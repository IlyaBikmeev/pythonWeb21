'''
Работа с файлами
Текстовые файлы
'''
import random

f = open('test.txt', 'w')
s = set()

for i in range(1000000):
    number = random.randint(1, 10000)
    f.write(f'{number}\n')
    s.add(number)

print(len(s))
f.close()

with open('text.txt', 'r') as f:

    s = f.read()
    for word in s.split():
        print(word)

#Как нужно открывать файлы:
'''
with open('file.txt', 'w') as f:
    #работа с файлом
'''

'''
Задание: напишите функцию, которая принимает имя текстового файла и возвращает словарь:
частоты встреч каждого слова в тексте. 
(Считаем, что у нас нет знаков препинания и в тексте только слова)

Результат работы функции записать в новый файл
'''


