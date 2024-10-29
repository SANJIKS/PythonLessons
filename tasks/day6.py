nums = [1, 2, 3, 4, 5]
squaries = {num: num * num for num in nums if num % 2 == 0}

result = {}
for num in nums:
    if num % 2 == 0:
        result.update({num: num * num})


# print(squaries)

strings = ('banana', 'apple', 'pine', 'monitor')
result = [string for string in strings if len(string) > 5]

# print(type(squaries))
# print(type(result)) 

# strings = ("apple", "banana", "cherry")
# result = ','.join(strings)
# print(result)


# target = input('Введите число: ')

# result = 0
# for num in range(1, int(target)+1):
#     result += num

# print(result)