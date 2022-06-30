#Лямбда выражения
#Синтаксис: lambda аргументы : что вернуть

def foo(x):
    return 2 * x

f = lambda x : 2 * x

isEven = lambda x : True if x % 2 == 0 else False
isOdd = lambda x : not isEven(x)

print(isEven(246))
print( (lambda x : x ** 2)(10))


change = lambda a : list(map((lambda x : 2 * x), a)) #Так делать не надо

a = [1, 2, 3]
a = change(a)
print(a)