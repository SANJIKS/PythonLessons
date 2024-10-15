""" List, Loops: for, while """

# list()
# list() (Списки) - коллекция элементов. Изменяемый, упорядоченный, индексируемый, итерируемый тип данных. Используется для хранения набора элементов

# Элементами списка могут быть любые типы данных

list_with_all_data_types = [1, 'string', True, False, None, [1, 2], {'a': 10}, {1, 2}, ('a', 1, 'b')]

list_of_numbers = [1, 2, 3, 4, 5, [6, 7]]
list_of_numbers[0] # 1
list_of_numbers[1] # 2
# print(list_of_numbers[5][1])

# print(list_of_numbers[::-1])

a = [1, 2, 3]
# print('До ', a)
# a.append(4)
# print('После ', a)

# a.insert(1, 0.5)
# print(a)
# a.insert(index, element)

# a.insert(len(a), '4')
# print(a)

# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# list1.extend(list2)
# print(list1)

# new_list = list1 + list2
# print(new_list)

""" замена элементов """
letters = ['a', 'b', 'c', 'd']
# letters[3] = 'g'
# print(letters)


""" удаления элементов """
letters = ['a', 'b', 'c', 'd']
letters.pop(2)
# print(letters)

letters = ['a', 'b', 'c', 'd']
deleted_el = letters.pop(2)
# print(deleted_el)
letters.pop() # 'd'
# print(letters)

letters = ['a', 'a', 'b', 'c', 'd']
# letters.remove('a')
# print(letters)
# letters.remove('g') # ValueError


# letters.clear()
# print(letters)

# del letters[1]
# print(letters)

""" сортировка и копирование списка """

nums = [1, 2, 3, 4]
nums_copy = nums.copy()
nums_copy2 = nums[:]

# nums = [1, 2, 3, 4]
# nums2 = nums
# nums2.append(5)
# print(nums2)
# print(nums)
# print(nums is nums2)

nums_list = [8, 6, 10, 5]
nums_list.sort()
nums_list.sort()
# print(nums_list)

names = ['Kolya', 'Baimurat', 'Ivan', 'Alexandr']
# names.sort(key=len)
# print(names)
# new_names = sorted(names)
# print(new_names)

nums_list.reverse()
# print(nums_list)

""" Циклы """

# Цикл - многократное выполнение определенного участка кода

# Итерируемый объект - объект, к которому можно применить цикл

# nums_list = [1, 2, 3, 4, 5]
# print(nums_list[0])
# print(nums_list[1])
# print(nums_list[2])
# print(nums_list[3])
# print(nums_list[4])

# 1) for
# nums_list = [1, 2, 3, 4, 5]
# for num in nums_list:
#     print(num)

# for - цикл, который перебирает каждый элемент в итерируемом объекте и работает до тех пор, пока эти элементы не закончатся
# for элемент in итерируемый_об:
#   тело цикла


# string = 'Hello world'
# for letter in string:
#     print(letter)


# nums = range(10)
# for num in nums:
#     print(num)

# new_nums = []
# for num in range(1, 21):
#     if num % 2 == 0:
#         new_nums.append(num)

# print(new_nums)

list_of_lists = [[1, 2, 3], ['Katya', 'Masha', 'Sanya'], [4, 5, 6]]

# for list_ in list_of_lists:
#     for element in list_:
#         print(element)

# for element in list_of_lists[-1]:
#     print(element)



# while условие
# while - цикл, который работает до тех пор, пока условие возвращает True

# import time

# counter = 0
# while counter < 5:
#     print(counter)
#     print('hello world')
#     counter += 1
#     time.sleep(1)

# while True:
#     print('hello world')

# CTRL + C - остановка бесконечного цикла/процесса

# msg = input('Введите сообщение или stop: ')
# while msg != 'stop':
#     print(f'Ваше сообщение\n{msg}')
#     msg = input('Введите сообщение или stop: ')

# while True:
#     msg = input('Сообщение или stop: ')
#     if msg == 'stop':
#         print('цикл остановлен')
#         break
#     print(msg)


# break - оператор для остановки цикла
# continue - начинает цикл заново, пропуская остальное тело цикла

# a = 'Privetik'
# b = ''
# for letter in a:
#     if letter == 'i':
#         continue
#     b += letter

# print(b)

""" else в циклах """
nums = range(1, 101, 2)
# print(list(numsX))
result = 0
for num in nums:
    if num == 50:
        break
    result += num
else:
    print(result)