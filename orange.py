import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("калькулятор")
window.geometry("500x350")

window.configure(bg='lightblue')   # фоновый цвет




def calculate():
    try:
        num1 = float(name_entry.get())
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


# _____первое число______
frame1 = ttk.Frame(borderwidth=1, relief=tk.SOLID, padding=[8, 10])
name_label1 = ttk.Label(frame1, text="Введите первое число")
name_label1.pack(anchor=tk.NW)

name_entry = ttk.Entry(frame1)
name_entry.pack(anchor=tk.NW)

frame1.pack(anchor=tk.NW, fill=tk.X, padx=5, pady=5)
# _____________________________________________________________________
# _____действие______
frame2 = ttk.Frame(borderwidth=1, relief=tk.SOLID, padding=[8, 10])
name_label2 = ttk.Label(frame2, text="Введите действие")
name_label2.pack(anchor=tk.NW)

name_entry2 = ttk.Entry(frame2)
name_entry2.pack(anchor=tk.NW)

frame2.pack(anchor=tk.NW, fill=tk.X, padx=5, pady=5)
# _____________________________________________________________________
# _____второе число______
frame3 = ttk.Frame(borderwidth=1, relief=tk.SOLID, padding=[8, 10])
name_label3 = ttk.Label(frame3, text="Введите второе число")
name_label3.pack(anchor=tk.NW)

name_entry3 = ttk.Entry(frame3)
name_entry3.pack(anchor=tk.NW)

frame3.pack(anchor=tk.NW, fill=tk.X, padx=5, pady=5)
# _____________________________________________________________________

# _____кнопка посчитать______
button = tk.Button(window, text='Посчитать', command=calculate)
button.pack(pady=10)  # добавляем отступ сверху и снизу
# _____________________________________________________________________

# _____результат (в самом низу)______
frame4 = ttk.Frame(borderwidth=1, relief=tk.SOLID, padding=[8, 10])
name_label4 = ttk.Label(frame4, text="Результат")
name_label4.pack(anchor=tk.NW)

# Создаем поле для результата
result_entry = ttk.Entry(frame4)
result_entry.pack(anchor=tk.NW)

frame4.pack(anchor=tk.NW, fill=tk.X, padx=5, pady=5)
# _____________________________________________________________________

window.mainloop()