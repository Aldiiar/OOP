# словари и множества
# dict - словарь {key: value}
# set - множества

# new = dict(([1, 'one'], [2, 'two']))
# new = dict(enumerate('oop'))
other_student = dict(name = 'azat', age = 23, country = 'kgz')
# print(new)


student = {
    'name': 'Marlen',
    'age': 18,
    'weight': 70.6,
    'born_place': ('bishkek', 'kgz'),
    'hobby': ['chess', 'it', 'boxing']
}




# print(student.items())


# for i in student.items():
#     print(i)

# for k, v in student.items():
#     print(k, '==7>', v)

# for i in student:
#     print(f"{i}: {student[i]}")



# print(student.keys())
# print(student.values())
# print(student.items())


# '''delete'''
# deleted = student.pop('born_place')
# del student['hobby'][1]



# '''add'''
# student['favorite_food'] = ['rice', 'fish']
#
# '''edit'''
# student['weight'] += 3
# student.update(other_student)
# print(student)


#print(student.get('ag', 'нет такого ключа'))
# print(student['hobby'][2])
# print(student['age'])

