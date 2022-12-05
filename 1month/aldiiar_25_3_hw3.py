vowel = "yuoaiаиеоуыэюяeёЁУЕЫАОЭЯИЮYEUIOA"
consonant = "qwrtpsdfghjklzxcvbnmйцукнгшщзхфвпрлджчсмтбQWRTPSDFGHJKLZXCVBNMЙЦКНГШЩЗХЪФВПРЛДЖЧСМТЬБ"

while True:
    word = input('введите слово на английском или русском языке '
                 '\n(для остановки напишите exit или выход): ')
    letter = len(word)
    word.upper(), word.lower()

    if word == 'exit' or word == 'выход':
        break


    v = 0
    c = 0
    for i in word:
        if i in vowel:
            v += 1
        elif i in consonant:
            c += 1

    vo = v / letter * 100
    co = c / letter * 100

    print(f'слово: {word.lower()}'
          f'\nколичество букв: {letter}'
          f'\nгласных букв: {v}'
          f'\nсогласных букв: {c}', end=''
          f'\nгласные/согласные: {round(vo, 2)}%/{round(co, 2)}%')
