# словари, множества
# dict - dictionary (словарь)
# set - множество
# {key: value}

"""ДОП. ЗАДАНИЕ
создать возможность поиска блюда по нескольким ингридиентам
"""

menu = {
    'ramen': {'noodles', 'egg', 'pepper'},
    'beshbarmak': {'noodles', 'onion', 'meat'}
}

while True:
    user_input = input('введите продукт: ')
    for name, ingrs in menu.items():
        if user_input in ingrs:
            print(name)



    # user_input = input('введите название: ')
    # if user_input in menu.keys():
    #     print(menu[user_input])





# ramen.remove('egg')
# ramen.add('water')
# print(ramen)


#
# print(ramen.difference(beshbarmak))
# print(ramen - beshbarmak)
#
# print(ramen.union(beshbarmak))
# print(ramen | beshbarmak)
#
# print(ramen.intersection(beshbarmak))
# print(ramen & beshbarmak)
#
# print(ramen.symmetric_difference(beshbarmak))
# print(ramen ^ beshbarmak)

# numbers = [1, 2, 3, 2, 3, 4, 'a', 'a']
# numbers1 = {'a', 1, 4, 3, 2, 3, 2, 'a', 'a'}
#
# print(numbers)
# print(numbers1)
# print(type(numbers1))


# new = dict(([1, 'one'], [2, 'two']))
# new = dict(enumerate('oop'))
# other_student = dict(name='azat', age=23, country='kgz')
# print(new)
# print(new)

# student = {
#     'name': 'Marlen',
#     'age': 20,
#     'weight': 70.6,
#     'born_place': ('bishkek', 'kgz'),
#     'hobby': ['chess', 'it', 'boxing']
# }

# numbers = {n: n**2 for n in range(1, 4)}
# print(numbers)

# for i in student.items():
#     print(i)

# for key, value in student.items():
#     print(key, ' ==> ', value)

# for i in student:
#     print(f"{i}: {student[i]}")

# print(student.keys())
# print(student.values())
# print(student.items())

# """delete"""
# deleted = student.pop('born_place')
# del student['hobby'][1]

# print(deleted)

# """add"""
# student['favorite_food'] = ['rice', 'fish']
# student.update(other_student)
# print(student)

"""edit"""
# student['weight'] += 3
# student['hobby'] = tuple(student['hobby'])
# student['hobby'][1] = student['hobby'][1],
# print(student)

# print(tuple(student['hobby']))

# print(student.get('age', 'нет такого ключа!'))
# print(student['ag'])

# print(student['hobby'][1])
# print(type(student))
