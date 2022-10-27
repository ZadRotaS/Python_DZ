import re
from user_interface import *


def Read_doc():
    f = open('baza.txt', 'r', encoding='utf-8')
    text = f.readlines()

    for i, tex in enumerate(text ,start=0):
        tex = tex.replace(';', ' ')
        print(f'id {i}. {tex[:-1]}')
    f.close()
    return text


def Write_doc(text):
    f = open('text.csv', 'w', -1, 'utf-8')
    for i in range(len(text)):
        f.write(text[i])
    f.close


def element(text, num,num2):
    text2 = []
    text3 = []
    for i in range(1, len(text)):
        text2.append(list(text[i][:-1].split(';')))
    for k in range(len(text2)):
        text3.append(text2[k][num -1])
    if num2 == 1:
        for n, tex in enumerate(text3, start=1):
            print(f"id {n} {tex}")
    return text3

n = Operations_One()
if n == 1:
    element(Read_doc(),Operations(),n)

if n == 2:
    text, key = element(Read_doc(),Operations(),n), input("Введите ключ для поиска: ")
    for i, num in enumerate(text, start= 1):
        if key == num:
            print(f'id {i} {num}')
        
# text = Read_doc()
# n = Operations()
