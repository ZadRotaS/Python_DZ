import os


array = ["1 2 3", "4 5 6", "7 8 9"]


def print_geme(array):
    os.system('CLS')
    print(*array, sep="\n")


def Player1(array):
    print_geme(array)
    n = int(input("Ход первого игрока: "))
    if 0 < n < 4:
        if n == 1:
            array[0] = array[0].replace("1", "X")
        if n == 2:
            array[0] = array[0].replace("2", "X")
        if n == 3:
            array[0] = array[0].replace("3", "X")
    if 2 < n < 7:
        if n == 4:
            array[1] = array[1].replace("4", "X")
        if n == 5:
            array[1] = array[1].replace("5", "X")
        if n == 6:
            array[1] = array[1].replace("6", "X")
    if 6 < n < 10:
        if n == 7:
            array[2] = array[2].replace("7", "X")
        if n == 8:
            array[2] = array[2].replace("8", "X")
        if n == 9:
            array[2] = array[2].replace("9", "X")
    return array


def Player2(array):
    print_geme(array)
    n = int(input("Ход второго игрока: "))
    if 0 < n < 4:
        if n == 1:
            array[0] = array[0].replace("1", "O")
        if n == 2:
            array[0] = array[0].replace("2", "O")
        if n == 3:
            array[0] = array[0].replace("3", "O")
    if 2 < n < 7:
        if n == 4:
            array[1] = array[1].replace("4", "O")
        if n == 5:
            array[1] = array[1].replace("5", "O")
        if n == 6:
            array[1] = array[1].replace("6", "O")
    if 6 < n < 10:
        if n == 7:
            array[2] = array[2].replace("7", "O")
        if n == 8:
            array[2] = array[2].replace("8", "O")
        if n == 9:
            array[2] = array[2].replace("9", "O")
    return array


def game(array):
    n = ''
    if array[0] == "X X X" or array[1] == "X X X" or array[2] == "X X X":
        n = "player1 Win"
    if array[0] == "O O O" or array[1] == "O O O" or array[2] == "O O O":
        n = "player2 Win"
    
    
    if array[0][0] == "O" and array[1][0] == "O" and array[2][0] == "O":
        n = "player2 Win"
    if array[0][2] == "O" and array[1][2] == "O" and array[2][2] == "O":
        n = "player2 Win"
    if array[0][4] == "O" and array[1][4] == "O" and array[2][4] == "O":
        n = "player2 Win"
    if array[0][0] == "O" and array[1][2] == "O" and array[2][4] == "O":
        n = "player2 Win"
    if array[0][4] == "O" and array[1][2] == "O" and array[2][0] == "O":
        n = "player2 Win"
    

    if array[0][0] == "X" and array[1][0] == "X" and array[2][0] == "X":
        n = "player1 Win"
    if array[0][2] == "X" and array[1][2] == "X" and array[2][2] == "X":
        n = "player1 Win"
    if array[0][4] == "X" and array[1][4] == "X" and array[2][4] == "X":
        n = "player1 Win"
    if array[0][0] == "X" and array[1][2] == "X" and array[2][4] == "X":
        n = "player1 Win"
    if array[0][4] == "X" and array[1][2] == "X" and array[2][0] == "X":
        n = "player1 Win"
    
    return n

x = 0
for i in range(10):
    
    if i == 9:
        print_geme(array)
        print("Не чья")
    else:
        if game(array) == "player1 Win" or game(array) == "player2 Win":
            print_geme(array)
            print(game(array))
            break
        elif x == 0:
            Player1(array)
            x +=1
        elif x == 1:
            Player2(array)
            x -=1
       