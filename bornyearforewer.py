pushkinBornYear = 1799
our_year = 0
while our_year != pushkinBornYear:
    try:
        our_year = int(input('В каком году родился А.С. Пушкин? Ваш ответ в виде числа: '))
        if our_year != pushkinBornYear:
            print('Неверно')
        else:
            print('Верно')
    except ValueError:
        print('Введено не число!')