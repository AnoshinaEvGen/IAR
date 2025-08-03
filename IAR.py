from tkinter import *
from tkinter import messagebox as mb
import requests
import json




response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,'
                      'litecoin,tether&vs_currencies=usd,rub,eur,cny')
response.raise_for_status()
data = response.json()


# Создание графического интерфейса
window = Tk()
window.title("Курс криптовалют")
window.geometry("360x300")

label_1 = Label(text="Криптовалюта:").pack(padx=10, pady=5)
label_2 = Label(text="Валюта:").pack(padx=10, pady=5)

Button(text="Получить курс", command=exchange).pack(padx=10, pady=10)

window.mainloop()

