#Проверка корректности введенного года
def isYearCorrect(year):
    if isinstance(year, int) and year >= 0:
        return True
    return False

#Проверка года на високосность
def isLean(year):
    if not isYearCorrect(year):
        print('Неправильно введен год!')
        return -1

    if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
        return True
    return False

#Печать високосных лет в диапазоне
def printLeansRange(year_1, year_2):
    if not isYearCorrect(year_1) or not isYearCorrect(year_2):
        print('Неправильно введен год!')
        return -1

    for y in range(year_1, year_2 + 1):
        if isLean(y):
            print(y, end=' ')

#Следующий високосный год
def nextLeanYear(year):
    if not isYearCorrect(year):
        print('Неправильно введен год!')
        return -1

    year += 1
    while not isLean(year):
        year += 1
    return year

#1 Тестируем первую функцию
print('Тест 1')
for year in ['stroka', -1, 0, 234567, 2012, 2022]:
    if isYearCorrect(year):
        print('Год {} - корректен'.format(year))
    else:
        print('Год {} - некорректен'.format(year))
print('\nТест 2')
#2 Тестируем вторую функцию
for year in range(2000, 2201):
    if isLean(year):
        print('Год {} - високосный'.format(year))
    else:
        print('Год {} - не високосный'.format(year))

#3 Тестируем третью функцию
print('\nТест 3')
printLeansRange(2000, 2200)

#4 Тестируем четвертую функцию
print('\n\nТест 4')
for year in [2000, 2007, 2008, 2016, 2018]:
    print(nextLeanYear(year))