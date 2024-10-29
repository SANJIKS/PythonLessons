""" Множества (set) """

# set()

# set - изменяемая, неупорядоченная, итерируемая последовательность, которая содержит только уникальные/неповторяющиеся и неизменяемыые элементы

# коллекции - типы данных, которые могут содержать в себе последовательность элементов (list, tuple, dict, set)

# литералы - {}

# my_set1 = {1, 'string', 2, 3}
# print(my_set1)

# my_set2 = {'h', 'k', 'a', 'b'}
# print(my_set2)
# list_of_names = ['Alena', 'Aliya', 'Alena', 'Misha', 'Kayrat', 'Kayrat']
# print(list(set(list_of_names)))


# empty_set = {} # это не set, а dict
# print(type(empty_set))

# real_empty_set = set() # вот - это set
# print(type(real_empty_set))


""" Методы set """

class_a = {'Aktan', 'Aygul', 'Mayrash', 'Artyom'}
class_b = {'Malik', 'Aygul', 'Eldos', 'Aktan'}

# inter = class_a.intersection(class_b)
# print(class_a & class_b)
# print(inter)

# diff = class_a.difference(class_b)
# diff2 = class_b.difference(class_a)
# print(class_a - class_b)
# print(diff)
# print(diff2)


# print(class_a.union(class_b))
# print(class_a | class_b)


fruits = {'apple', 'banana', 'kiwi', 'tangerin'}
vegetables = {'carrot', 'potato', 'tomato', 'apple'}

# fruits.intersection_update(vegetables)
# print(fruits)

# vegetables.difference_update(fruits)
# print(vegetables)

# fruits.update(vegetables)
# print(fruits)

# a = {1, 2, ('a', 'b')} # TypeError
# print(a)

# my_unique_set = {True, False, 1, 0, 'string', (1, 2)}
# print(my_unique_set)

""" Словари - Dict """

# dict
# словарь - изменяемый, итерируемый тип данных. Вместо индекса имеет ключи. Состоит из пар - ключ: значение

# Ключи могут быть только неизменяемыми типами данных и должны быть уникальными

# Значениями могут быть любые типы данных

# литералы - {}

passport = {'name': 'Meerim', 'last_name': 'Kayratova', 'age': 25, 'gender': 'F'}

# print(passport['name'])
# print(passport['last_name'])
# print(passport['age'])
# print(passport['gender'])
# passport['licence'] # KeyError

# passport['licence'] = 'Can drive B'
# passport['licence'] # 'Can drive B'

# print(passport)

""" Создание словаря """
# my_dict = {1: 10}

# my_dict2 = dict(name='Vasya', age=23)
# print(my_dict2)

# my_dict3 = dict(
#     [
#     ('name', 'Vasya'), ('age', 23)
#     ]
#     )
# print(my_dict3)

# my_dict4 = dict.fromkeys(['a', 'b', 'c', 'd', 'key'], 10)
# print(my_dict4)

human = {
    'name': 'Bakai',
    'age': 25,
    'friends': ['Sasha', 'Artur'],
    'name': 'Bakyt'
}
# print(human)

# dict_5 = {
#     'name': 'Ak-Maral',
#     [1, 2]: 'ERROR' # TypeError
# }

""" Получение значений из словаря """
car = {
    "marka": "Toyota",
    "model": "Camry",
    "color": "black",
    "volume": 3.2,
    "year": 2012
}

# print(car['marka'])
# print(car['kuzov'])

# print(car.get('marka'))
# print(car.get('kuzov')) # None
# print(car.get('kuzov', 'Такого ключа нет!')) # 'Такого ключа нет!'

# print(car.setdefault('year'))
# print(car.setdefault('kuzov', 'Sedan'))
# print(car)

""" Добавление данных в словарь """
house = {
    "color": "white",
    "category": "elite",
    "rooms": 4,
    "warmness": True
}

house['area'] = '30x40'
# print(house)

house.update({'floor': 3, 'door': 'wooden'})
# print(house)

house['color'] = 'yellow'
# print(house)

house.update({'rooms': 6})
# print(house)

""" Удаление данных из словаря """
house = {
    "color": "white",
    "category": "elite",
    "rooms": 4,
    "warmness": True
}

deleted_key = house.pop('category')
print(house)
print(deleted_key)

deleted_pair = house.popitem()
print(house)
print(deleted_pair)

del house['rooms']
print(house)

house.clear()
print(house)