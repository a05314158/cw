import tkinter as tk
from tkinter import ttk
from tkinter import colorchooser

BG_COLOR_TASK1 = "#e6f7ff"
BG_COLOR_TASK2 = "#f9f4e8"
BG_COLOR_TASK3 = "#e8f4e9"
BUTTON_COLOR_TASK1 = "#80bfff"
BUTTON_COLOR_TASK2 = "#e6c229"
BUTTON_COLOR_TASK3 = "#4caf50"
FONT = ("Arial", 14)

class TaskView:
    def __init__(self, root):
        self.root = root

        self.btn_task1 = tk.Button(self.root, text="Направления", font=FONT, bg=BUTTON_COLOR_TASK1, command=self.solve_task1)
        self.btn_task1.pack(pady=10)

        self.btn_task2 = tk.Button(self.root, text="Калькулятор", font=FONT, bg=BUTTON_COLOR_TASK2, command=self.solve_task2)
        self.btn_task2.pack(pady=10)

        self.btn_task3 = tk.Button(self.root, text="Движение круга", font=FONT, bg=BUTTON_COLOR_TASK3, command=self.solve_task3)
        self.btn_task3.pack(pady=10)

    def solve_task1(self):
        def show_message(direction):
            new_window = tk.Toplevel(self.root)
            new_window.configure(bg=BG_COLOR_TASK1)

            arrow_label = tk.Label(new_window, font=("Arial", 36), bg=BG_COLOR_TASK1)
            arrow_label.pack(padx=20, pady=20)

            if direction in direction_symbols:
                arrow_label.config(text=direction_symbols[direction])
            else:
                arrow_label.config(text="Некорректное направление")

        root = tk.Tk()
        root.title("Направления")
        root.configure(bg=BG_COLOR_TASK1)

        direction_symbols = {
            "вверх": "\u2191",
            "вниз": "\u2193",
            "влево": "\u2190",
            "вправо": "\u2192"
        }

        for direction in direction_symbols:
            button = tk.Button(root, text=direction, font=FONT, command=lambda d=direction: show_message(d),
                            bg=BUTTON_COLOR_TASK1)
            button.grid(row=len(direction_symbols) // 2, column=list(direction_symbols.keys()).index(direction))

    def solve_task2(self):
        def calculate():
            try:
                expression = entry.get()
                result = eval(expression)
                result_window = tk.Toplevel(root)
                result_window.title("Результат")
                result_window.configure(bg=BG_COLOR_TASK2)
                result_label = tk.Label(result_window, text=f"Результат: {result}", font=("Arial", 12), bg=BG_COLOR_TASK2)
                result_label.pack(padx=20, pady=20)
            except Exception as e:
                error_window = tk.Toplevel(root)
                error_window.title("Ошибка")
                error_window.configure(bg=BG_COLOR_TASK2)
                error_label = tk.Label(error_window, text="Ошибка при вычислении", font=("Arial", 12), bg=BG_COLOR_TASK2)
                error_label.pack(padx=20, pady=20)

        def clear_entry():
            entry.delete(0, tk.END)

        def remove_last_symbol():
            entry.delete(len(entry.get()) - 1)

        root = tk.Tk()
        root.title("Калькулятор")
        root.configure(bg=BG_COLOR_TASK2)

        entry = tk.Entry(root, width=30, font=("Arial", 14))
        entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('+', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('*', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('/', 4, 2),
            ('C', 4, 3),
            ('⌫ ', 4, 2)
        ]

        for (text, row, col) in buttons:
            button = ttk.Button(root, text=text, width=5, command=lambda t=text: entry.insert(tk.END, t))
            if text == 'C':
                button.configure(command=clear_entry)
            if text == '⌫ ':
                button.configure(command=remove_last_symbol)
            button.grid(row=row, column=col, padx=5, pady=5)

        equal_button = ttk.Button(root, text="=", width=5, command=calculate)
        equal_button.grid(row=4, column=3, padx=5, pady=5)

    def solve_task3(self):
        def move_circle(event):
            global target_x, target_y
            target_x, target_y = event.x, event.y
            animate()

        def choose_color():
            color = colorchooser.askcolor()[1]
            canvas.itemconfig(circle, fill=color)

        def animate():
            current_x, current_y = canvas.coords(circle)[0], canvas.coords(circle)[1]
            dx = (target_x - current_x) / 20
            dy = (target_y - current_y) / 20

            if abs(dx) < 1 and abs(dy) < 1:
                canvas.coords(circle, target_x - 10, target_y - 10, target_x + 10, target_y + 10)
            else:
                canvas.move(circle, dx, dy)
                canvas.after(30, animate)

        root = tk.Tk()
        root.title("Движение круга")
        root.configure(bg=BG_COLOR_TASK3)

        canvas = tk.Canvas(root, width=400, height=400, bg='white')
        canvas.pack()

        circle = canvas.create_oval(190, 190, 210, 210, fill='blue')

        canvas.bind("<Button-1>", move_circle)

        color_button = tk.Button(root, text="Выбрать цвет", command=choose_color, bg=BUTTON_COLOR_TASK3)
        color_button.pack(pady=10)

        root.mainloop()

