pushkinBornYear = '1799'
pushkinBornDay = '06'
pushkinBornMonth = '06'
our_month = ''
our_day = ''
our_year = ''

while our_year != pushkinBornYear:
    our_year = input('В каком году родился А.С. Пушкин? Ваш ответ: ')
    if our_year != pushkinBornYear:
        print('Неверный год')
    else:
        while not((our_month == pushkinBornMonth)&(our_day == pushkinBornDay)):
            try:
                our_day, our_month = map(str, input('В какой день родился А.С. Пушкин? Ваш ответ в формате "дд мм": ').split())
                if (our_day == pushkinBornDay) & (our_month == pushkinBornMonth):
                    print('Верно')
                else:
                    print('Неверно')
            except ValueError:
                print('Неверный ввод')