# функции , аргумент: *args, **kwargs.
# DRY - don't repeat yourself
# def - definition

# def plus(*args):
#     return sum(args)
#
# print(plus(2, 5, 7, 90, 142, 334))

def days(**kwargs):
    return kwargs

print(days(monday=1, tuesday=2))


# def get_square(width, length):
#     return width * length
#
# square_2 = get_square(width=int(input('ширина: ')), length=int(input('длина: ')))
# square_hall = get_square(8, 15)
#
# print(square_2)


def len1(sequence):
    counter = 0
    for _ in sequence:
        counter += 1
    return counter

print(len1('bishkek'))



# def greet(name, surname): #name - обязательный, позиционный параметр
#     print(f'name: {name.title()}, surname: {surname.title()}')
#
# greet('azamat', 'alimov')
# greet('alina', 'kamilova')




# width = 5
# length = 7
# square_2 = width * length
# print(square_2)
#
# width = 8
# length = 15
# square_hall = width * length
# print(square_hall)

