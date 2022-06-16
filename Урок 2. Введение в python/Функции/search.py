'''
Дан отсортированный массив а и число х. Определить, есть ли число х в массиве
'''

#Примитивный поиск
#Худший случай - O(n)
def naiveSearch(a, x):
    for element in a:
        if element == x:
            return True
    return False

#Бинарный поиск
#Худший случай - O(log n)
def binarySearch(a, x):
    left = 0
    right = len(a) - 1

    while left < right:
        mid = (left + right) // 2
        if a[mid] == x:
            return True
        elif a[mid] > x:
            right = mid - 1
        else:
            left = mid + 1

    return a[left] == x

a = [0, 1, 3, 7, 8, 9, 20, 35]
print(binarySearch(a, 8))