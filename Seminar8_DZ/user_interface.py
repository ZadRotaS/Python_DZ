

def int_input():
    while True:
        n = input("Введите целое число: ")

        if n.replace("-", "").isdigit():
            n = int(n)
            break
        else:
            print("Error. Ввели не число")
    return n

def Operations_One():
    print('\n'.join(['',  'Что нужно:',
          '1 - вывод списка', '2 - поиск по ключу']))
    while True:
        n = int_input()
        if 0<n<3:
            break
        else:
            print('Error такого нет в списке')

    return n
def Operations():
    print('\n'.join(['',  'Критерий отбора:',
          '1 - Фамилия', '2 - Имя', '3 - Отчество', '4 - id_Сотрудника', '5 - Должность']))
    while True:
        n = int_input()
        if 0<n<6:
            break
        else:
            print('Error такого нет в списке')

    return n
