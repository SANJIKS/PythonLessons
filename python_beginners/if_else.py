""" Условные выражения (if-elif-else) """

# bool() - неизменяемый тип данных, которым имеет всего 2 значения: True, False

# 10 > 2 # True
# < - меньше
# > - больше
# <= - меньше или равно
                        # --> bool()
# >= - больше или равно
# != - неравенство
# == - равенство

# print(25 == 23) # False
# print(25.0 == 25) # True
# print('яблоко' > 2) # Type Error

# print(bool(0)) # False
# print(bool(1)) # True

# print(bool(2)) # True
# print(bool(-2)) # True

# print(bool('it')) # True
# print(bool('')) # False

# bool([]) # False
# bool({}) # False
# bool(set()) # False
# bool(None) # False


""" if else """
# num = 15
# if num > 20:
#     print('num больше 20')
# else:
#     print('num НЕ больше 20')

# temperature = 40

# if temperature < 20:
#     print('холодно')
# else:
#     if temperature < 30:
#         print('тепло')
#     else:
#         if temperature > 35:
#             print('жарко')

""" elif """
# temperature = 40
# if temperature < 20:
#     print('холодно')
# elif temperature < 30:
#     print('тепло')
# elif temperature > 35:
#     print('жарко')
# else:
#     print('НЕВЕРНАЯ ТЕМПЕРАТУРА')

# num2 = 15
# if num2 < 20:
#     print('num2 < 20')
# elif num2 > 10:
#     print('num > 10')

# num2 = 15
# if num2 < 20:
#     print('num2 < 20')
# if num2 > 10:
#     print('num2 > 10')


# mark = input('Введите оценку от 1 до 5')

# if mark.isdigit():
#     mark = int(mark)
#     msg = ''
#     if mark == 5:
#         msg = 'Ты молодец!'
#     elif mark == 4:
#         msg = 'Хорошо!'
#     elif mark <= 3:
#         msg = 'Подтяни предмет!'
    
#     print(msg)
# else:
#     print('Вы ввели не число!')


""" and, or, not """
# age = 18
# if age >= 18 and age < 28:
#     print('Входите')
# else:
#     print('Входа нет')

False # False
True # True
False and False # False
True and True # True
False and True # False
True and False # False

False or False # False
True or True # True
False or True # True
True or False # True

not True # False
not False # True

(False or True) and (False and False) # False


""" is, ==, in """
# a = [1,2,3]
# b = [1,2,3]
# print(a is b)
# print(id(a))
# print(id(b))
# print(a == b)

# string = 'hello world'
# print('world' in string)


""" тернарный оператор """
# msg = input('Введите сообщение ')
# if len(msg) > 10:
#     print('Сообщение длиннее 10')
# else:
#     print('Сообщение короче 10')

# msg = input('Введите сообщение ')

# res = 'Сообщение длиннее 10' if len(msg) > 10 else 'Сообщение короче 10'
# print(res)

# if условие:
#     действие 1
# else:
#     действие 2

# действие 1 if условие else действие 2
