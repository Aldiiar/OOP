#списки, кортежи
#list - (список)
#tuple - (кортеж)



# objects = (3,)
#
# print(objects)
# print(type(objects))



#new = list(range(1, 4))
# print(new)

# objects = [5, 5, 8, True, False, 4.7, 8, 8, 8, 20.5]
# new = objects.copy()
#
# # new[-1] = 5
# print(objects == new)
# print(objects is new)
#
#
# print(objects)
# print(new)



# max_ap = 1
# for i in objects:
#     if objects.count(i)


# objects.sort()
# print(min(objects))
# print(max(objects))

"""изменения"""
# objects[0], objects[3] = objects[3], objects[0]
# objects[objects.index(False)] = 'Bishkek'
# objects[0] = objects[0].title()
# objects[2] += 15
# del objects[-1][1]


"""удаление"""

# del objects[4:7]

# objects = [i for i in objects if type(i) != str]

# objects.pop(0)
# deleted = objects.pop(0)
# print(deleted)

# objects.remove(True)
# objects.remove(4.7)

"""добавление"""
# objects.append('bishkek')
# objects.insert(3, 100)
# objects.append(new)
# objects.extend(new)
# objects += new
