#7
# lst = [1, 2, 3, 4, 5, 6, 7]
# avg = sum(lst) / len(lst)

# for num in lst:
#     if num > avg:
#         print(num)

#8
# strings = ["apple", "banana", "pear", "watermelon"]
# longest = ''
# for string in strings:
#     if len(string) > len(longest):
#         longest = string

# print(longest)

#9
# lst = [3, 1, 4, 1, 5, 9, 2]

# max_index = 0
# for i in range(1, len(lst)):
#     if lst[i] > lst[max_index]:
#         max_index = i

# print(max_index)

#10
# s = 'hello'
# reversed_char = ''
# for char in s:
#     reversed_char = char + reversed_char

# print(reversed_char)

#11
# lst1 = [1, 2, 3, 4]
# lst2 = [3, 4, 5, 6]
# result = []

# for num in lst1:
#     if num in lst2:
#         result.append(num)

# print(result)

#12
# lst = [1, 2, 2, 3, 4, 4, 5]
# unique = []

# for elem in lst:
#     if elem not in unique:
#         unique.append(elem)

# print(unique)

#13
# d = {"a": 1, "b": 2, "c": 3}
# total = 0

# for value in d.values():
#     total += value

# print(total)

#14
# lst = [1, 2, 3, 4, 5]
# result = []

# for i in lst:
#     result.append(i ** 2)

# print(result)

#15
# lst = ['a', 'b', 'c']
# result = ','.join(lst)
# print(result)

#16
# lst = [1, 2, 3, 1, 1, 4, 5]
# target = 1
# count = 0

# for num in lst:
#     if num == target:
#         count +=1

# print(count)

#17
# d1 = {"a": 1, "b": 2, "c": 3}
# d2 = {"b": 4, "c": 5, "d": 6}
# common_keys = []

# for key in d1:
#     if key in d2:
#         common_keys.append(key)

# print(common_keys)

#19
# lst = [1, 2, 3, 4, 5, 6]
# target = 3
# result = []

# for num in lst:
#     if num >= target:
#         result.append(num)

# print(result)

#20
""" Найдите три ключа с самыми высокими значениями в словаре my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}. """

# my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}

# results = sorted(my_dict, key=my_dict.get)[-3:]
# print(results)