from ast import Num
import numbers
from random import randint, random
from re import X


text = ["Задача 1: Сумма чисел числа N.",
        "Задача 2: Факториал числа N.",
        "Задача 3: Cписок из N чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.",
        "Задача 4: Cписок из N элементов, заполненных числами из промежутка [-N, N] и произведение элементов на указанных позициях.",
        "Задача 5: Алгоритм перемешивания списка из модуля random."]
print('\n'.join(text))
x = int(input("Ввыбирите задачу: "))
if 0 < x < 6:

    if x == 1:
        Numbers = input("Введите число: ")
        N = int((float(Numbers) * 10 ** len(Numbers)))
        sum = 0
        while N != 0:
            sum += N % 10
            N = N // 10    
        print(Numbers, "->", sum)
    
    if x == 2:
        N = int(input("Введите число: "))
        fac = 1
        print(N, "->", fac ,end=" ")
        for i in range(2, N+1):
            fac *= i
            print(fac, end=" ")

    if x == 3:
        N = int(input("Введите число: "))
        array = []
        sum = 0
        for i in range(1,N+1):
            array.append(round((((1 + 1/i)**i))))
            sum +=array[i - 1]
        print("для n =", N ,array, "->", sum)

    if x == 4:
        N = int(input("Введите число: "))
        number1 = int(input("Введите позицию 1: "))
        number2 = int(input("Введите позицию 2: "))
        array = []
        if (N > 0):
            for i in range(-N,N+1):
                array.append(i)
        else:
            N *=-1
            for i in range(-N, N+1):
                array.append(i)
        print("->",array)
        print("->",array[number1 - 1] * array[number2 - 1])

    if x == 5:
        N = int(input("Введите количество элементов списка: "))
        array = list(range(N))
        X = 0
        X1 = 0
        print("->", array)
        for i in range(len(array)):
            X1 = randint(0,N-1)
            X = array[i]
            array[i] = array[X1]
            array[X1] = X
        print("->", array)
else:
    print("Вы выбрали задачу которой нету в списке, перезапустите ")