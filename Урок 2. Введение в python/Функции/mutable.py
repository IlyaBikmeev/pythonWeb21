'''
Неизменяемые типы данных:
Все примитивные типы данных: int, float, str, bool
А также кортежи : tuple
'''

a = 5
print('Id a = {}'.format(id(a)))
a = 6
b = a
print('Сейчас айди а = {}'.format(id(a)))
print('Но айдишник а = айдишнику b = {}'.format(id(b)))

#Массив - изменяемый тип данных. Посмотрим пример
arr = [1, 2, 3, 4, 5, 6, 7, 8]
print('Сейчас id массива равен: {}'.format(id(arr)))
arr[3] = 12345678
print('После изменения массива id не изменился: {}'.format(id(arr)))