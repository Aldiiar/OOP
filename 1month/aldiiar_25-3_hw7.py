'''1'''
ten = list(range(1, 11))
evens = list(filter(lambda x: x % 2 == 0, ten))

print(list(map(lambda x: x ** 2, evens)))

'''2'''
def element(list_example=ten):
    print('Для выхода из программы напишите - exit')

    while True:
        try:
            index_user = input('Введите индекс: ')
            if index_user == 'exit':
                return 'Программа завершенна'
            else:
                print(list_example[int(index_user)])
        except ValueError:
            print(f'Неверный ввод! Пожалуйста введите индекс с 0 до {len(list_example) - 1}.')
        except IndexError:
            print(f'Неверный индекс! Пожалуйста введите индекс с 0 до {len(list_example) - 1}')


print(element())
