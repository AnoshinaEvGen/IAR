from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import requests

def update_b_label(event):
    # Получаем полное название базовой криптовалюты из словаря
    code = b_combobox.get()
    name = cryptos[code]
    b_label.config(text=name)

def update_t_label(event):
    # Получаем полное название целевой валюты из словаря
    code = t_combobox.get()
    name = currencies[code]
    t_label.config(text=name)

def exchange():
    crypto_code = b_combobox.get()
    currency_code = t_combobox.get()

    if crypto_code and currency_code:
        try:
            response = requests.get(
                f'https://api.coingecko.com/api/v3/simple/price?ids={crypto_code}&vs_currencies={currency_code}'
            )
            response.raise_for_status()
            data = response.json()

            if currency_code.lower() in data.get(crypto_code, {}):
                rate = data[crypto_code][currency_code.lower()]
                crypto_name = cryptos[crypto_code]
                currency_name = currencies[currency_code]
                mb.showinfo("Курс обмена", f"1 {crypto_name} = {rate} {currency_name}")
            else:
                mb.showerror("Ошибка", "Данные не найдены")
        except Exception as e:
            mb.showerror("Ошибка", f"Ошибка API: {e}")
    else:
        mb.showwarning("Внимание", "Выберите криптовалюту и валюту")

# Словари кодов и названий
cryptos = {
    "bitcoin": "Bitcoin (BTC)",
    "ethereum": "Ethereum (ETH)",
    "ripple": "Ripple (XRP)",
    "cardano": "Cardano (ADA)",
    "solana": "Solana (SOL)",
    "dogecoin": "Dogecoin (DOGE)"
}

currencies = {
    "USD": "Доллар США",
    "EUR": "Евро",
    "RUB": "Российский рубль",
    "JPY": "Японская йена",
    "CNY": "Китайский юань"
}

# Создание графического интерфейса
window = Tk()
window.title("Курс криптовалют")
window.geometry("360x300")

Label(text="Криптовалюта:").pack(padx=10, pady=5)
b_combobox = ttk.Combobox(values=list(cryptos.keys()))
b_combobox.pack(padx=10, pady=5)
b_combobox.bind("<<ComboboxSelected>>", update_b_label)

b_label = ttk.Label()
b_label.pack(padx=10, pady=10)

Label(text="Валюта:").pack(padx=10, pady=5)
t_combobox = ttk.Combobox(values=list(currencies.keys()))
t_combobox.pack(padx=10, pady=5)
t_combobox.bind("<<ComboboxSelected>>", update_t_label)

t_label = ttk.Label()
t_label.pack(padx=10, pady=10)

Button(text="Получить курс", command=exchange).pack(padx=10, pady=10)

window.mainloop()
