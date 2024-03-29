name = input('Your name: ')
a = 0



maps = [1, 2, 3,
        4, 5, 6,
        7, 8, 9]

# Победные линии
win = [[0, 1, 2],
       [3, 4, 5],
       [6, 7, 8],
       [0, 3, 6],
       [1, 4, 7],
       [2, 5, 8],
       [0, 4, 8],
       [2, 4, 6]]


def instruct():
    """Выводит на экран инструкцию для игрока."""
print ('Добро пожаловать на ринг грандиознейших интеллектуальных состязаний всех времён.Твой мозг и мой процессор сойдутся в схватке за доской игры Крестики-нолики.Чтобы сделать ход, введи число от 1 до 9. Приготовься с к бою, жалкий человечишка. Вот-вот начнётся решающее сражение.')

# Запустим карту
def print_maps():
    print(maps[0], end=' ')
    print(maps[1], end=' ')
    print(maps[2])

    print(maps[3], end=' ')
    print(maps[4], end=' ')
    print(maps[5])

    print(maps[6], end=' ')
    print(maps[7], end=' ')
    print(maps[8])



# Сделаем ход
def step_maps(step, symbol):
    ind = maps.index(step)
    maps[ind] = symbol


# Получим текущий результат игры
def get_result():
    victories = ''

    for i in win:
        if maps[i[0]] == 'X' and maps[i[1]] == 'X' and maps[i[2]] == 'X':
            victories = 'X'
        if maps[i[0]] == 'O' and maps[i[1]] == 'O' and maps[i[2]] == 'O':
            victories = 'O'

    return victories


# Ищем линии в которых либо есть, либо вообще нет 'X','O' для победы
def check_line(sum_O, sum_X):
    step = ""
    for line in win:
        o = 0
        x = 0
        for a in range(0, 3):
            if maps[line[a]] == 'O':
                o = o + 1
            if maps[line[a]] == 'X':
                x = x + 1

        if o == sum_O and x == sum_X:
            for a in range(0, 3):
                if maps[line[a]] != 'O' and maps[line[a]] != 'X':
                    step = maps[line[a]]

    return step


# Компьютер выбирает куда сходить
def computer():
    step = ''

    step = check_line(2, 0)

    if step == '':
        step = check_line(0, 2)

    if step == '':
        step = check_line(1, 0)

    if step == '':
        if maps[4] != 'X' and maps[4] != 'O':
            step = 5
    if step == '':
        if maps[0] != 'X' and maps[0] != 'O':
            step = 1

    return step


game_over = False
man = True

while game_over == False:

    print_maps()

    if man == True:
        symbol = 'X'
        step = int(input('Ход человека:'))
    else:
        print('Ход компьютера:')
        symbol = 'O'
        step = computer()

    # Если компьтер нашел клетку в которую сходит , продолжим игру. Если нет то ничья.
    if step != '':
        step_maps(step, symbol)
        victories = get_result()  # Поймем кто победил.
        if victories != '':
            game_over = True
        else:
            game_over = False
    else:
        print('ничья')
        game_over = True
        victories = 'дружба'

    man = not (man)

# Объявим победителя. Покажем карту.
print_maps()
if victories == 'дружба':
    print ('Победила дружба')
else:
    print('Победил', victories)


word = name
with open("scores.txt", "r") as b:
    line = ''
    while word not in line:
        line = b.readline()
        if word in line:
            print(b.tell())

        with open('scores.txt', 'a') as f:
            if (victories == 'X'):
                a = a + 1
            else:
                a = a + 0
            f.write(str(a))
            f.close()

