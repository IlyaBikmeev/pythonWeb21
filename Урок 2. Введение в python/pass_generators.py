#Функция добавляет в алфавит все символы с символами от start до end (в кодировке)
def addSymbols(str, start, end):
    #Превращаем символы в их порядковые номера
    start = ord(start)
    end = ord(end)

    while start <= end:
        str += chr(start)    #chr - принимает порядковый номер, возвращает символ с этим номером
        start += 1

    return str

#Функция генерации всех паролей из алфавита alph длины n и записи в файл f
def generate(alph, n, f, currentPassword):
    if len(currentPassword) == n:
        f.write(currentPassword + '\n')
        return

    for c in alph:
        generate(alph, n, f, currentPassword + c)


alphabet = addSymbols('', 'a', 'z')
alphabet = addSymbols(alphabet, 'A', 'Z')
alphabet = addSymbols(alphabet, '0', '9')

f = open('passwords.txt', 'w')
generate(alphabet, 5, f, '')

f.close()