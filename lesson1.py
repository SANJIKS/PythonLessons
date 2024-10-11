""" Типы Данных """

# Mutable (Изменяемые типы данных)
# 1. List - []
# 2. Dict - {}
# 3. Set - {}

# Immutable (Неизменяемые типы данных)
# 1. str - '', "" 
# 2. int - 100
# 2.1 float - 100.00
# 2.2 complex - ab123
# 3. tuple - ()
# 4. bool - True, False
# 5. None - None

# List

my_list = []

# Список из целых чисел
numbers = [1, 2, 3, 4, 5]

# Список из строк
words = ['apple', 'banana', 'cherry']

mixed = [1, 'apple', 3.14, True]

# print(mixed)
# my_list.append(1)
# print(my_list)
# my_list.remove(1)
# print(my_list)

# mixed[0] = 2
# print(mixed)

# print(mixed[2])

# print(len(mixed[1]))


# Tuple - кортеж
numbers = (1, 2, 3, 4, 5)

words = ('apple', 'banana', 'cherry')

mixed = (1, 'apple', 3.14, True, 'apple')

single_element_tuple = (1,)  # Обязательно ставим запятую

first = numbers[0]

# new_tuple = numbers + words
# print(new_tuple)
# repeated_tuple = numbers * 2
# print(repeated_tuple)

# print(mixed.count('apple'))
# print(mixed.index('apple'))


# Set - Множество
# my_set = set()

# numbers = {1, 2, 3, 1, 2}
# # print(numbers)

# my_set.add('orange')
# my_set.add('banana')

# print(my_set)

# my_set.remove('banana')
# my_set.discard('apple')

# print(my_set)

# set1 = {1, 2, 3}
# set2 = {3, 4, 5}

# union_set = set1 | set2 # .union()
# print(union_set)

# intersection_set = set1 & set2 # .intersection()
# print(intersection_set)

# difference_set = set1 - set2 # .difference()
# print(difference_set)
# differnce_set2 = set2 - set1
# print(differnce_set2)

# print(set1.symmetric_difference(set2))

# Dict - Словарь
# Ключами могут только неизменяемые типы данных

my_dict = {}

person = {
    0: 'Alice',
    1: 25,
    'city': 'Bishkek',
    'works': False

}

mixed_dict = {
    'number': 10,
    'list': [1, 2, 3],
    'nested_dict': {'key': 'value'}
}

# print(person.get('car', 'Машины нет'))

# person['age'] = 26
# print(person['age'])

# person['car'] = 'Kia'
# print(person)

# del person['city']
# print(person)

# works = person.pop('works')

# print(person)
# print(works)

# for key in person:
#     print(key)

# for value in person.values():
#     print(value)

# for key, value in person.items():
#     print(f'{key}: {value}')

# print(person.keys())


# str - Строки

s1 = 'Hello'

s2 = "World"

s3 = """ This is 
a multiline
string """
# ctrl + shift + a
 

greeting = 'Hello World'
# print(greeting)
# print('Hello' * 3)

# print(greeting[0])
# print(greeting[-1])
# print(len(greeting))

# substring = greeting[::-2]
# print(substring)

text = 'Python and Backend'

# print(text.lower())
# print(text.upper())
# print(text.strip(''))
# print(text.replace('h', 'g'))
# print(text.split('and'))

# my_list = ['Apple', 'Banana', 'Orange']

# print(', '.join(my_list))

# name = input('Введите имя: ')

# print(f'Hello {name}')



# int - Число (integer)

a = 5
b = -10

x = 10
y = 3

print(x + y)  # 13
print(x - y)  # 7
print(x * y)  # 30
print(x / y)  # 3.3333333333333335 (деление с плавающей точкой)
print(x // y) # 3 (целочисленное деление)
print(x % y)  # 1 (остаток от деления)
print(x ** y) # 1000 (10 в степени 3)

# Числа с плавающей точкой (float):

a = 3.14
b = -0.001
c = 2.0

# Комплексные числа (complex)
z = 2 + 3j

int()
float()
str()
list()
set()
dict()
bool()
None

# Булевый тип (bool)

x = True
y = False
z = None # null


if y:
    print(True)
if not y:
    print(False)

if 5 > 10:
    print('5 больше 10')
elif 5 == 10:
    print('5 это  10')
else:
    print('5 меньше 10')


# 1 = True, 0 = False
print(2 * False)

name = None
name = input('Введите имя')