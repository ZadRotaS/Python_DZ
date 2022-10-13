from ast import Num
import numbers
from random import randint, random
from re import X


text = ["Задача 1.",
        "Задача 2.",
        "Задача 3.",
        "Задача 4 не понимаю что от меня нужно.",
        "Задача 5 не понимаю что от меня нужно."]
print('\n'.join(text))
x = int(input("Ввыбирите задачу: "))
if 0 < x < 6:

    if x == 1:
        print(f'{float(input("Введите число: ")):.{(len(input("Введите точность: ")) - 2)}f}')

    if x == 2:
        def simple(n):
            num = 2
            simple = []
            while num * num <= n:
                while n % num == 0:
                    simple.append(num)
                    n = n / num
                num = num + 1
            if n > 1:
                simple.append(n)
            return simple

        print(simple(int(input("Введите число: "))))

    if x == 3:
        array = [randint(0,9) for i in range(int(input("Введите число: ")))]
        print(array)
        def del_double(my_list):
            i = 0
            while (i < (len(my_list))):
                key = my_list[i]
                if my_list.count(key)>1:
                    i -=1
                    while my_list.count(key) != 0:
                        my_list.pop(my_list.index(key))
                i +=1
            return my_list
        print(del_double(array))

    if x == 4:
        x = 0

    if x == 5:
        x = 0

else:
    print("Вы выбрали задачу которой нету в списке, перезапустите ")
