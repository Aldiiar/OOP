ar1 = int(input('температура в Чуе: '))
ar2 = int(input('температура в Оше: '))
ar3 = int(input('температура в Нарыне: '))
ar4 = int(input('температура в Жалал-Абаде: '))
ar5 = int(input('температура в Ысык-Куле: '))
ar6 = int(input('температура в Баткене: '))
ar7 = int(input('температура в Таласе: '))

sum_area = (ar1 + ar2 + ar3 + ar4 + ar5 + ar6 + ar7) / 7


print(f"Средний показатель температуры воздуха по КР на сегодня: {'%.1f' % sum_area}°C")

if sum_area >= 20:
    print('одевайтесь легко')
elif sum_area < 20:
    print('одевайтесь теплее')
else:
    print('error')

