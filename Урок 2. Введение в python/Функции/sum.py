'''
Определение функции:
def nameOfFunction(arg1, arg2, arg3):
    #some code
    pass
'''


def sumOfTwoNumbers(a, b):
    return a + b

#Тесты
#Передать мы можем переменные любых типов
res_1 = sumOfTwoNumbers(5, 7)
res_2 = sumOfTwoNumbers(3.14, 2.718281828459045)
res_3 = sumOfTwoNumbers([1, 2, 3], [4, 5, 6])
res_4 = sumOfTwoNumbers('Hello', ' World!')

for i, R in enumerate([res_1, res_2, res_3, res_4]):
    print('Res {} equals {}'.format(i + 1, R))

