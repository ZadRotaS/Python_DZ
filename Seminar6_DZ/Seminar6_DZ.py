from random import randint


text = ["Задача 1.",
        "Задача 2.",
        "Задача 3.",
        "Задача 4 не понимаю что от меня нужно.",
        "Задача 5 не понимаю что от меня нужно."]
print('\n'.join(text))
x = int(input("Ввыбирите задачу: "))
if 0 < x < 6:

    if x == 1:
        array = [randint(1, 20) for i in range(int(input("Введите число: ")))]
        print(array)
        array2 = []
        for i in range(1, len(array)):
            if array[i-1] < array[i]:
                array2.append(array[i])
        print(array2)

    if x == 2:
        array = [i for i in range(
            1, int(input("Введите число: "))) if i % 20 == 0 or i % 21 == 0]
        print(array)

    if x == 3:
        array = ["Иван", "Мария", "Петр", "Илья",
                 "Марина", "Петр", "Алина", "Бибочка"]
        array2 = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О',
                  'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']
        print(array)
        def sort(array, array2):
            array3 = []
            n = ''
            
            for i in range(len(array2)):
                n = array2[i]
                array3.append(n + ':')
                for k in range(len(array)):
                    if n == array[k][0]:
                        array3.append(array[k])
                if len(array3) > 1:
                    print(*array3, end=" ")
                array3 = []

        sort(array, array2)

    if x == 4:
        x = 0

    if x == 5:
        x = 0

else:
    print("Вы выбрали задачу которой нету в списке, перезапустите ")
