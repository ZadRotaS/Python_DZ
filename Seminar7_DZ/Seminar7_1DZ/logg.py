import datetime
def Log(text):
    today = datetime.datetime.today()
    today = today.strftime("%d-%m-%Y %H.%M.%S")
    # print( today.strftime("%d-%m-%Y %H.%M.%S") ) 
    with open("logg.txt", "a") as txt:
        txt.write(f'User Input "{text}" datatime "{today}" \n')
    