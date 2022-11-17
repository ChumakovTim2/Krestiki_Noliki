#123456
map = [1,2,3,
       4,5,6,
       7,8,9]
# Победные линии
wins = [[0,1,2],
        [3,4,5],
        [6,7,8],
        [2,5,8],
        [0,4,8],
        [0,3,6],
        [1,4,7],
        [2,4,6]]
#Запустим карту 
def print_maps():
    print(maps[0], end = " ")
    print(maps[1], end = " ")
    print(maps[2])
    
    print(maps[3], end = " ")
    print(maps[4], end = " ")
    print(maps[5])
    
    print(maps[6], end = " ")
    print(maps[7], end = " ")
    print(maps[8])
    
def n(vopsos):
    otvet = None
    while otvet not in('да', 'нет'):
        otvet = input(question).lower()
    return otvet
    
def choice():
    hod_1 = nachalo ("Играть крестиками ?")
    if hod_1 == 'да':
        print ('Вы играете за крестики')
        man = X
        computer = O
    else:
        print('Вы играете за нолики')
        man = O 
        computer = X
    return man, computer
    
#Сделаем ход    
def step_maps(step,symbol)
    ind = maps.index(step)
    maps[ind] = symbol
# Получим текущий результат игры
def get_result():
    win = ""

    for i in win:
        if maps [i[0]] == 'X' and maps [i[1]] == 'X' and maps [i[2]] == 'X':
            win = 'X'
        if maps [i[0]] == 'O' and maps [i[1]] == 'O' and maps [i[2]] == 'O':
            win = 'O'

    return win 
    
#Ищем линии в которых либо есть, либо вообще нет 'X','O' для победы 
def check(sum_O,sum_X):
    step = ""
    for line in win :
        O = 0
        X = 0
        for a in range =(0,3):
            if maps [line[a]] == 'O':
                O = O + 1 
            if maps [line[a]] == 'X':
                X = X + 1 
                
        if O == sum_O and x == sum_X
            for a in range (0,3):
                if maps[line[a]] = 'O' and maps [line[a]] = 'X'
                step = maps[line[a]]
                
    return step
    
#Компьютер выбирает куда сходить 
def Intelect():
    
    step = ''
    step = check_line(2,0)
    
    if step == '':
    step == check_line(0,2)
    
    if step == '':
    step = check_line (1,0)