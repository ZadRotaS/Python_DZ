

def Read_doc():
    f = open('text.csv', 'r', encoding='utf-8')
    text = f.readlines()

    for i, tex in enumerate(text):
        tex = tex.replace(';', ' ')
        print(f'{i + 1}. {tex[:-1]}')
    f.close()
    return text


def Write_doc(text):
    f = open('text.csv', 'w', -1, 'utf-8')
    for i in range(len(text)):
        f.write(text[i])
    f.close


def int_input():
    while True:
        n = input("Введите целое число: ")

        if n.replace("-", "").replace(".", "").isdigit():
            n = int(n)
            break
        else:
            print("Error. Ввели не число")
    return n


def Operations():
    print('\n'.join(['', 'Операции:',
          '1 - Удалить из списка', '2 - Добавить в конец списка', '0 - exit']))
    n = int_input()
    return n


text = Read_doc()
n = Operations()
if n == 1:
    print('Ввыберите id для удаления')
    num = int_input() - 1
    if 0 < num < len(text):
        text.pop(num)
    Write_doc(text)

if n == 2:
    fam = input('Введите фамилию: ')+';'+input("Введите имя: ")+';' + \
        input("Введите номер: ")+';'+input("Введите коментарий: ")+";"+"\n"
    text.append(fam.replace(' ', ''))
    Write_doc(text)
