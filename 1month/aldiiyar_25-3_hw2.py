day = int(input('Введите день рождения: '))
month = int(input('Введите месяц рождения: '))


if (day > 20 and day < 32 and month == 3) or (month == 4 and day > 0 and day < 21):
    print('овен')
elif (day > 20 and day < 31 and month == 4) or (month == 5 and day > 0 and day < 22):
    print('телец')
elif (day > 21 and day < 32 and month == 5) or (month == 6 and day > 0 and day < 22):
   print('близнецы')
elif (day > 21 and day < 31 and month == 6) or (month == 7 and day > 0 and day < 23):
    print('рак')
elif (day > 22 and day < 32 and month == 7) or (month == 8 and day > 0 and day < 22):
    print('лев')
elif (day > 21 and day < 32 and month == 8) or (month == 9 and day > 0 and day < 24):
    print('дева')
elif (day > 23 and day < 31 and month == 9) or (month == 10 and day > 0 and day < 24):
    print('весы')
elif (day > 23 and day < 32 and month == 10) or (month == 11 and day > 0 and day < 23):
    print('скорпион')
elif (day > 22 and day < 31 and month == 11) or (month == 12 and day > 0 and day < 23):
    print('стрелец')
elif (day > 22 and day < 32 and month == 12) or (month == 1 and day > 0 and day < 21):
    print('козерог')
elif (day > 20 and day < 32 and month == 1) or (month == 2 and day > 0 and day < 20):
    print('водолей')
elif (day > 19 and day < 29 and month == 2) or (month == 3 and day > 0 and day < 21):
    print('рыбы')
else:
  print('указана некоректная дата рождения')