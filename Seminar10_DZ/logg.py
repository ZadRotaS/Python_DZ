import datetime



def Logg(m, text):
    
    with open("logg.txt", "a", encoding='utf-8') as Log:
        today = datetime.datetime.today().strftime("%d-%m-%Y %H:%M")
        Log.write(f'{today} Пользователь: "{m.chat.first_name} {m.chat.last_name}" чат: "{m.chat.id}" ввод: "{text}" \n')