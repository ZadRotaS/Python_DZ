
text = ["Задача 1: Проверяет, является ли этот день выходным.",
        "Задача 2: Поверка истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.",
        "Задача 3: Выдаёт номер четверти плоскости (X и Y).",
        "Задача 4: Показывает диапазон возможных координат точек в этой четверти.",
        "Задача 5: Принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве."]
print('\n'.join(text))
x = int(input("Ввыбирите задачу: "))
if 0 < x < 6:

    if x == 1:
        data = int(input("Введите число недели: "))
        if data < 7:
            if data <=5:
                print("Нет это рабочий день")
            else:
                print("Да это выходной")
        else:
            ptint("это число больше дней чем в неделе")

    if x == 2:
        for x in range(2):
            for y in range(2):
                for z in range(2):
                    if (x == z or x <= y and z):
                        print(x,y,z)

    if x == 3:
        X = int(input("Введите Х: "))
        Y = int(input("Введите Y: "))
        if X !=0 and Y !=0:
            if X > 0 and Y > 0:
                print("Х =",X,"Y =",Y,"-> 1")
            if X < 0 and Y > 0:
                print("Х =",X,"Y =",Y,"-> 2")
            if X < 0 and Y < 0:
                print("Х =",X,"Y =",Y,"-> 3")
            if X > 0 and Y < 0:
                print("Х =",X,"Y =",Y,"-> 4")
        else:
            print("ERROR, 0 entered!")
    
    if x == 4:
        quarter = int(input("Введите номер четверти: "))
        if 0 < quarter < 5:
            if quarter == 1:
                print("Х > 0 Y > 0")
            if quarter == 2:
                print("Х < 0 Y > 0")
            if quarter == 3:
                print("Х < 0 Y < 0")
            if quarter == 4:
                print("Х > 0 Y < 0")
        else:
            print("The quarter is entered incorrectly!")

    if x == 5:
        Ax = int(input("Введите первую координату A: "))
        Ay = int(input("Введите вторую координату A: "))
        Bx = int(input("Введите первую координату В: "))
        By = int(input("Введите вторую координату B: "))
        print((((Bx -Ax) ** 2) + ((By - Ay) ** 2)) ** 0.5)
        
else:
    print("Вы выбрали задачу которой нету в списке, перезапустите ")
