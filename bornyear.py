pushkinBornYear = 1799
try:
    if int(input('В каком году родился А.С. Пушкин? Ваш ответ в виде числа: ')) != pushkinBornYear:
        print('Неверно')
    else:
        print('Верно')
except ValueError:
    print('Введено не число!')