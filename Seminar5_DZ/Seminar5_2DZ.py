
def read_txt():
    with open("text_words.txt", "r") as txt:
        txt1 = txt.readlines()

    return txt1


def code_txt(txt):
    for k in range(len(txt)):
        text = list(txt[k])
        text2 = ""
        n = text[0]
        count = 0
        for i in range(len(text)):
            if n == text[i] :
                count += 1
            else:
                text2 = text2 + str(count) + n
                count = 1
                n = text[i]
        with open("text_code_words.txt", "a", encoding="utf-8") as txt_code:
            txt_code.write(f"{text2}\n")
    return text2


txt = read_txt()
code_txt(txt)