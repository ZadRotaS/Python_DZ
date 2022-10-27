from logg import Log

def Worling_with():
    print('\n'.join(['', '', 'Working with',
          '1 - ratiomal', '2 - complex', '0 - exit']))
    return int(input())


def Operations():
    print('\n'.join(['', '', 'Operations:',
          '1 - sum', '2 - sub', '3 - mul', '4 - div', '5 - pow', '6 - sqrt', '0 - previous menu']))
    return (int(input()[0]))


def Operations_calculations(n):

    if n == 3:
        print('\n'.join(["", "1 - '*'", "2 - '**'", "0 - previous menu"]))
        return (int(input()) * 10)

    if n == 4:
        print('\n'.join(["", "1 - '/'", "2 - '//'",
              "3 - '%'", "0 - previous menu"]))
        return ((int(input()) *10)+1)
    


def numbers():

    while True:
        nombers_One = input("Введите 1 число: ")
        Log(nombers_One)
        if nombers_One.replace("-", "").replace(".","").isdigit():
            nombers_One = float(nombers_One)
            break
        else:
            print("Error. Ввели не число")
    
    while True:
        nombers_Two = input("Введите 2 число: ")
        Log(nombers_Two)
        if nombers_Two.replace("-", "").replace(".","").isdigit():
            nombers_Two = float(nombers_Two)
            break
        else:
            print("Error. Ввели не число")
    
    return nombers_One, nombers_Two


def numbers_complex():
    while True:
        nombers_One = input("Введите 1 число: ")
        Log(nombers_One)
        if nombers_One.replace("-", "").replace(".","").isdigit():
            nombers_One = float(nombers_One)
            break
        else:
            print("Error. Ввели не число")
    
    while True:
        nombers_Two = input("Введите 2 число: ")
        Log(nombers_Two)
        if nombers_Two.replace("-", "").replace(".","").isdigit():
            nombers_Two = float(nombers_Two)
            break
        else:
            print("Error. Ввели не число")
    
    while True:
        nombers_Three = input("Введите 3 число: ")
        Log(nombers_Three)
        if nombers_Three.replace("-", "").replace(".","").isdigit():
            nombers_Three = float(nombers_Three)
            break
        else:
            print("Error. Ввели не число")
    
    while True:
        nombers_Four = input("Введите 4 число: ")
        Log(nombers_Four)
        if nombers_Four.replace("-", "").replace(".","").isdigit():
            nombers_Four = float(nombers_Four)
            break
        else:
            print("Error. Ввели не число")
    
    return nombers_One, nombers_Two, nombers_Three, nombers_Four



