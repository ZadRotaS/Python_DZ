from ast import Num
import numbers
from random import randint, random
from re import X


text = ["Задача 1: Список из произвольных чисел, сумма элементов нечетных позициях.",
        "Задача 2: Списко из произвольных чисел, произвидение пар чисел.",
        "Задача 3: Преоброзование десятичного в двоичное число.",
        "Задача 4: Разница между максимальным и минимальным значением дробной части элементов.",
        "Задача 5: Список чисел Фибоначчи и Негафибоначи."]
print('\n'.join(text))
x = int(input("Ввыбирите задачу: "))
if 0 < x < 6:

    if x == 1:
        N = int(input("Введите число: "))
        array = []
        for i in range(N):
            array.append(randint(0, 9))
        print(array)
        sum = 0
        for i in range(0, N, 2):
            sum += array[i]
        print(sum)

    if x == 2:
        N = int(input("Введите число: "))
        array = []
        for i in range(N):
            array.append(randint(0, 9))
        print(array)
        sum = []
        j = len(array) - 1
        for i in range(0, round((N + 0.1)/2)):
            if (i == j):
                sum.append(array[i])
            else:
                sum.append(array[i] * array[(j)])
                j -= 1
        print(sum)

    if x == 3:
        N = int(input("Введите число: "))
        N1 = ''
        while N > 0:
            N1 = str(N % 2) + N1
            N = N // 2
        print(N1)

    if x == 4:
        N = int(input("Введите число: "))
        array = []
        
        for i in range(N):
            array.append(randint(100, 999))
            array[i] = array[i] / 100
        min = max = array[0] % 1

        for i in range(0,N):
            if (min > (array[i] % 1)):
                min = array[i] % 1
            if (max < (array[i] % 1)):
                max = array[i] % 1
        print(array)
        print("min", f"{min:0.2f}","max", f"{max:0.2f}","Difference",f"{max - min:0.2f}")
    if x == 5:
        fib1 = 1
        fib2 = 1
        fib = [0,1,1]
        notfib = []
        n = int(input("Введите число: "))
        for i in range(3, n+1):
            fib.append(fib1 + fib2)
            fib1 = fib2
            fib2 = fib[i]

        for i in range(-n, 0):
            if (i % 2 != 0):
                notfib.append(fib[-i])
            else:
                notfib.append(fib[-i] * -1)
        print(notfib,fib)

else:
    print("Вы выбрали задачу которой нету в списке, перезапустите ")
