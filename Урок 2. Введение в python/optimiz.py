'''
Дан массив A и дано число x. Найти два таких индекса i, j в массиве, что A[i] + A[j] = x
Если таких индексов нет, напечатайте -1

A = [1, 2, 3, 4]
x = 5

ответ --   0, 3
'''

#Примитивное решение (naive solution)

def naiveSolution(a, x):
    n = len(a)

    for i in range(n - 1):
        for j in range(i + 1, n):
            if a[i] + a[j] == x:
                return (i, j)
    return -1


#Оптимизированное решение

#Проверка есть ли такая пара
def optimizedSolution1(a, x):
    s = set()

    for number in a:
        if x - number in s:
            return True
        s.add(number)

    return False


#Теперь с индексами
def optimizedSolution2(a, x):
    s = {}   #Храним в словаре пары элемент-индекс

    for i, number in enumerate(a):
        if x - number in s:
            return (i, s[x - number])

        s[number] = i

    return -1


# n = int(input())
#
# topics = {}  # номер темы - заголовок
# graph = {x : [] for x in range(1, n + 1)}  # номер сообщения - список ответов
# k = 1  # текущий номер темы
#
# for i in range(n):
#     num = int(input())
#     if num == 0:
#         header = input()
#         body = input()
#         topics[k] = header
#         k += 1
#     else:
#         body = input()
#         graph[num].append(k)
#         k += 1
#
#
#

#tree - словарь, root - номер вершины текущей
def calcNodes(tree, root):
    if len(tree[root]) == 0:
        return 0

    s = 0

    for topic in tree[root]:
        s += 1 + calcNodes(tree, topic)

    return s


n = int(input())

topics = {}  #название темы по номеру
tree = {x : [] for x in range(1, n + 1)}     #Номер сообщения - список ответов

for i in range(1, n + 1):
    num = int(input())    #либо 0, либо номер сообщения, на которое отвечаем

    if num == 0:   #новая тема. Нужно ее создать
        header = input()   #заголовок темы
        body = input()     #текст сообщения
        topics[i] = header

    else:   #ответ на какое-то сообщение
        body = input()
        tree[num].append(i)  #добавляем в список ответов

numbersOfMessages = -1   #максимальное количество сообщений
ans = -1                 #номер темы, которой соответствует это количество

for key, value in topics.items():
    nodes = calcNodes(tree, key)

    if nodes > numbersOfMessages:
        numbersOfMessages = nodes
        ans = key

print(topics[ans])