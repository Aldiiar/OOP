min_n = 0
max_n = 100
attempt = 0
attempts1 = []
print('Загадайте целое число от 0 до 100')


while True:

      formula = (max_n + min_n) // 2

      answer = input(f'Отвечайте только - да, больше, меньше'
                     f'\nЭто число - {formula}?: ')
      attempt += 1
      attempts1.append(formula)

      if answer == 'да':
            print('Программа угадала ваше число')
            with open('otvety.txt', 'w', encoding='UTF-8') as file:
                  file.write(f'Загаданное число: {formula}'
                             f'\nКоличество попыток: {attempt}'
                             f'\nВаши попытки: {attempts1}')
            break

      elif answer == 'больше':
            min_n = formula + 1

      elif answer == 'меньше':
            max_n = formula - 1

      else:
            print('Неправильный ввод!')

