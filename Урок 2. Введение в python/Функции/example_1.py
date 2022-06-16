def foo_1(x):
    x += 1

def foo_2(a):
    a[2] = 1234

number = 123
arr = [1,2,3,4]
foo_1(number)
foo_2(arr)

print('Переменная number не изменилась: number = {}'.format(number))
print('Переменная arr изменилась : arr = {}'.format(arr))

'''
Если тип данных изменяемый - он передается в функцию по ссылке.
Если неизменяемый - по значению.
'''