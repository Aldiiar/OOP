mentors = ["Аблай", "Вова", "Марлен"]

while True:

      print(f'список менторов: {mentors}'
            f'\n1 - для добавления ментора'
            f'\n2 - для изменения имени ментора'
            f'\n3 - для удаления ментора'
            f'\n0 - для выхода из программы')

      adding = str.title(input('Введите имя ментора: '))
      mentors.append(adding)


      if len(mentors) < 6:
        print(mentors)
      else:
        print('Превышен лимит имён')




