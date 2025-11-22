import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("калькулятор")
window.geometry("500x350")

# _____создание кнопки______
frame = ttk.Frame(borderwidth=1, relief=tk.SOLID, padding=[8, 10])
name_label = ttk.Label(frame, text="Введите первое число")
name_label.pack(anchor=tk.NW)

name_entry = ttk.Entry(frame)
name_entry.pack(anchor=tk.NW)

frame.pack(anchor=tk.NW, fill=tk.X, padx=5, pady=5)
# _____________________________________________________________________
frame = ttk.Frame(borderwidth=1, relief=tk.SOLID, padding=[8, 10])
name_label = ttk.Label(frame, text="Введите действие")
name_label.pack(anchor=tk.NW)

name_entry2 = ttk.Entry(frame)
name_entry2.pack(anchor=tk.NW)

frame.pack(anchor=tk.NW, fill=tk.X, padx=5, pady=5)
# _____________________________________________________________________
frame = ttk.Frame(borderwidth=1, relief=tk.SOLID, padding=[8, 10])
name_label = ttk.Label(frame, text="Введите второе число")
name_label.pack(anchor=tk.NW)

name_entry3 = ttk.Entry(frame)
name_entry3.pack(anchor=tk.NW)

frame.pack(anchor=tk.NW, fill=tk.X, padx=5, pady=5)
# _____________________________________________________________________

frame = ttk.Frame(borderwidth=1, relief=tk.SOLID, padding=[8, 10])
name_label = ttk.Label(frame, text="Результат")
name_label.pack(anchor=tk.NW)

# Создаем поле для результата
result_entry = ttk.Entry(frame)
result_entry.pack(anchor=tk.NW)

frame.pack(anchor=tk.NW, fill=tk.X, padx=5, pady=5)


def calculate():
    try:
        num1 = float(name_entry.get())  # Используем float вместо int для работы с десятичными числами
        operation = name_entry2.get()
        num2 = float(name_entry3.get())

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                result = "на ноль делить нельзя"
            else:
                result = num1 / num2
        else:
            result = "неверная операция"

        # Выводим результат в поле результата
        result_entry.delete(0, tk.END)  # Очищаем поле
        result_entry.insert(0, str(result))  # Вставляем результат

    except ValueError:
        result_entry.delete(0, tk.END)
        result_entry.insert(0, "Ошибка: введите числа")
    except Exception as e:
        result_entry.delete(0, tk.END)
        result_entry.insert(0, f"Ошибка: {str(e)}")


button = tk.Button(window, text='Посчитать', command=calculate)
button.pack()

window.mainloop()