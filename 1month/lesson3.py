# циклы - for, while
# for
# while
# i, item, iterable

# eng = "qwertyuiop[]asdfghjkl;'zxcvbnm,."
# rus = "йцукенгшщзхъфывапролджэячсмитьбю "
#
# while True:
#     user_input = input('\nвведите слово: ')
#     for i in user_input:
#         if i in eng:
#             print(rus[eng.index(i)], end='')
#         else:
#             print(eng[rus.index(i)], end='')


# print(rus[eng.index('r')])












# print('word'.index('w'))


c = 0

while c != 5:
    c += 1
    if c == 3:
        print('мы устали')
        break
    print(c)


# from time import sleep
#
# c = 0
#
# while True:
#     sleep(1)
#     print('hello', c)
#     c += 1






# c = 0
#
# while c != 100:
#     print('hello', c)
#     c += 1



# cash = 100
# percents = 0.1
# years = 5
#
# counter = 1
#
# for year in range(1, years + 1):
#     cash = round(cash * percents + cash, 1)
#     print(f'year: {counter} - {cash}')
#     counter += 1


# for i in range(1, 4):
#     for k in range(1, 4):
#         print(i, k)

# word = 'аксессуар'
#
# for letter in word:
#     if letter == 'с':
#         print('мы пропускаем "c"')
#         continue
#     print(letter)


    # if letter == 'е':
    #     print('цикл завершён!')
    #     break
    # print(letter)
    # print(letter.upper(), end=' ')