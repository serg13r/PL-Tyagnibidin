import tkinter as tk
from tkinter import messagebox
import requests
import json

def fetch_and_save():
    username = entry.get().strip()
    if not username:
        messagebox.showwarning("Ошибка", "Введите имя пользователя или организации GitHub!")
        return

    url = f"https://api.github.com/users/{username}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        user_data = response.json()

        # Извлекаем только нужные поля
        filtered_data = {
            'company': user_data.get('company'),
            'created_at': user_data.get('created_at'),
            'email': user_data.get('email'),
            'id': user_data.get('id'),
            'name': user_data.get('name'),
            'url': user_data.get('url')
        }

        filename = f"{username}_info.json"
        with open(filename, "w") as f: # Сохраняем в файл
            json.dump(filtered_data, f, indent=4)
            # indent чтобы каждый вложенный уровень структуры был сдвинут на 4 пробела, как в примере
        messagebox.showinfo("Успех", f"Данные сохранены в файл {filename}")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Неожиданная ошибка: {e}")


root = tk.Tk()
root.title("Получить данные пользователя GitHub")
root.geometry("400x150")

tk.Label(root, text="Имя пользователя/организации GitHub:").pack(pady=10)
entry = tk.Entry(root, width=40)
entry.pack(pady=5)
entry.focus()

tk.Button(root, text="Получить данные", command=fetch_and_save).pack(pady=10)

root.mainloop()

# Вводим имя организации, вариант 2 - apache

# Вывод:
# {
#     "company": null,
#     "created_at": "2009-01-17T20:14:40Z",
#     "email": null,
#     "id": 47359,
#     "name": "The Apache Software Foundation",
#     "url": "https://api.github.com/users/apache"
# }
