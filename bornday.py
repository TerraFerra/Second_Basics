pushkinBornYear = 1799
pushkinBornDay = '06'
pushkinBornMonth = '06'
try:
    if int(input('В каком году родился А.С. Пушкин? Ваш ответ в виде числа: ')) != pushkinBornYear:
        print('Неверный год')
    else:
        our_day, our_month = map(str, input('В какой день родился А.С. Пушкин? Ваш ответ в формате "дд мм": ').split())
        if (our_day == pushkinBornDay) & (our_month == pushkinBornMonth):
            print('Верно')
        else:
            print('Неверно')
except ValueError:
    print('Неправильный ввод!')
