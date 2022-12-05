# лямбда, исключения
# lambda arguments: expressition

a = lambda a, b: a + b
print(a(2, 10))


# def up_letter(word: str):
#     return word.title()
#
# def show_words(sequence, func):
#     for word in sequence:
#         print(func(word))
#
# show_words(['python', 'geektech', 'school'], up_letter)
# show_words(['python', 'geektech', 'school'], lambda word: word.upper())


# numbers = list(range(1, 10+1))
# print(numbers)

# filtered_numbers = list(filter(lambda x: x<6, numbers))
# filtered_numbers = [i for i in numbers if i > 5]
# print(filtered_numbers)


# mapped_list = list(map(lambda x: x*2, numbers))
# print(mapped_list)
try:
    print(10/2)
except:
    print('на ноль не делим')