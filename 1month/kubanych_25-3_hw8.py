print('[start] - начать\n'
      '[exit] - выход\n'
      'Загадайте число от 1 до 100')
list_attemps = []
while True:
    user_input = input('Введите команду: ').lower()
    if user_input == 'exit':
        break
    elif user_input == 'start':
        l1st = list(range(1, 101))
        attempts = 1
        answer = 50
        while True:
            guess = input(f'Число больше или меньше {answer}?: ').format(answer)
            if guess.title() == 'Меньше' or 'М':
                l1st[1] = answer
                answer = (l1st[1] + l1st[0]) // 2
                attempts += 1
                list_attemps.append(answer)
            elif guess.title() == 'Больше' or 'Б':
                l1st[0] = answer
                answer = (l1st[1] + l1st[0]) // 2
                attempts += 1
                list_attemps.append(answer)
            elif guess.title() == 'Равно' or 'Р':
                print('Congrats!')
                list_attemps.append(answer)
                with open('results.txt', 'w', encoding='UTF-8') as file:
                    file.write(
                        f'Количество попыток: {attempts}; \n'
                        f'Список попыток: {list_attemps}; \n'
                        f'Загаданное число: {answer}')
                break
            else:
                print('Команды - (Равно, Больше, Меньше)')
    else:
        print('Некорректный ввод')

