# работа с файлами txt
# w - write(писать)
# a - add
# r - read
# x - safety method

# new = open('file.txt', 'w', encoding='UTF-8')
# new.write('Испания выиграет ЧМ')
# new.close()

# with open('new.txt', 'w', encoding='UTF-8') as file:
#     file.write('GeekTech')

with open('new.txt', 'a') as file:
    file.write('\nAldik super')

# with open('nex.txt', 'x') as file:
#     file.write('dscvfvdvdscx')


with open('new.txt', 'r', encoding='UTF-8') as file:
    # print(file.read())
    # print(file.readline())
    # print(file.readlines()[-2])
