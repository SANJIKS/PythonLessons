""" List, String"""

# list()
# list() (Списки) - коллекция элементов. Изменяемый, упорядоченный, индексируемый, итерируемый тип данных. Используется для хранения набора элементов

list_with_all_data_types = [1, 'string', True, False, None, [1, 2], {'a': 10}, {1, 2}, ('a', 1, 'b')]

list_of_numbers = [1, 2, 3, 4, 5, [6, 7]]
list_of_numbers[0]
list_of_numbers[3]
list_of_numbers[5]
list_of_numbers[5][1]

list_of_numbers[1:3]

# print(list_of_numbers[::-1])

""" Методы списков """

" 1) Добавление элементов в список "
a = [1, 2, 3]
# a.append(4)
# print(a)

a.insert(1, 1.5)
# print(a)

list1 = [1, 2, 3]
list2 = [4, 5, 6]

# list1.extend('World')
# print(list1)

# print(list1 + list2)
# list1[0] = 10
# print(list1)


" замена элементов "
# letters = ['a', 'b', 'c', 'g']
# letters[3] = 'd'
# print(letters)

" удаление элементов "
# letters = ['a', 'b', 'c', 'g']
# letters.pop(2)
# print(letters)

# letters = ['a', 'b', 'c', 'g']
# deleted_el = letters.pop(2)
# print(deleted_el)


# letters = ['a', 'a', 'b', 'c', 'g']
# letters.remove('a')
# print(letters)
# letters.remove('sdtfgyhj') # ValueError

# letters.clear()
# print(letters)

# del letters[1]
# print(letters) # ['a', 'b', 'c', 'g']


""" strings (строки) """

# str()

# string - неизменяемый, упорядоченный, индексируемый, итерируемый тип данных

string = 'hello'
string2 = "Hello"

doc_string = """ Строка документации - используется для описания кода в несколько строк """

docs_string2 = ''' СТрока документации'''

str1 = 'Hello'
str2 = 'World'
print(str1 + str2)
# Конкатенация - склеивание/сложение строк

frog = 'Quak'
# print(frog * 3)

# print(len(frog))


""" Функции и методы строк """

greeting = 'Hello everyone'

# print(dir(greeting))
# # dir(x) - возвращает список методово переданного объекта

# my_str = 'Hello#World'

# print(my_str.lower())
# print(my_str.upper())
# print(my_str.split('#')) # str.split() - возвращает список из строк по делителю, если не передать делитель, по пробелу


my_str2 = '     hello world     '

my_str2.title() # Hello World
my_str2.capitalize() # Hello world
my_str2.count('l') # 3
my_str2.replace('o', 'm') # hellm wmrld
# print(my_str2.strip()) # удаляет пробелы с двух сторон
my_str2.lstrip()
my_str2.rstrip()



string = 'Some string with 5 words'
string.isalpha() # False
string.isdigit() # False
string.isalnum() # False
string.startswith('s') # True
string.endswith('ds') # True

name = 'Baimuratik'
