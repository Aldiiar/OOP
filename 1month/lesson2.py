# Логический тип данных, условные конструкции и операторы
#bool - boolean (логический тип данных)
#true, false
#and, or, not - логические операторы


# time = 'утро'
#
# if time == 'morning' or time == 'утро':
#     print('good morning')
# elif time == 'day' or time == 'день':
#     print('good afternoon')
# elif time == 'evening' or time == 'вечер':
#     print('good evening')
# else:
#     print('hello')


# print( 2 == 3-1)
# print(2 != 4)
# print(2 > 3)
# print(2 >= 2)
# print(2 >= 1)


# print(2 > 1 and 4 < 7)
# print(2 > 1 and 4 < 2)
# print(1 < 2 > 4)


# a = 5
# a = a + 5
# a += 5
#
# print(a)


# password = '123456'
#
# input_password = input('введите пароль: ')
#
# if input_password == password:
#     print('ok')
# else:
#     print('неверный пароль')


password = 'asalhgv8'

if len(password) >= 6 and not password.isdigit() and not password.isalpha():
    print('ok')
else:
    print(f'your password consist is {len(password)}\n'
          f'пароль должен состоять из чисел и букв, а также длиннее 5')



# word = 'corola'
#
# print('o' in word)
# print(word.count('o'))


# print(password.isdigit())
# print(password.isalpha())

# индексы
# word = 'python'
#
# print(word[1])
# print(word[1:4]) #срезы
# print(word[::3]) #срезы


# shoes_black = '34-44'
#
# first = int(shoes_black[:2])
# second = int(shoes_black[3:])
