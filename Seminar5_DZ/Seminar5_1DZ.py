from random import sample

n = int(input("Введите число: "))
text = ""
if n > 0:
    for i in range(n):
        text += str("".join(sample("абв", k=3)) + " ")
    print(text)
    print(text.replace("абв ", ""))
else:
    print("The data is incorrect")

