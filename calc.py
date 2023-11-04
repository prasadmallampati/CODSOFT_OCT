import tkinter as tk
from tkinter import ttk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")

        # Variables
        self.num1_var = tk.StringVar()
        self.num2_var = tk.StringVar()
        self.result_var = tk.StringVar()

        # Create GUI elements
        self.create_entries()
        self.create_buttons()

    def create_entries(self):
        entry_frame = ttk.Frame(self.root)
        entry_frame.grid(row=0, column=0, columnspan=2, sticky="nsew")

        ttk.Label(entry_frame, text="Number 1:").grid(row=0, column=0, padx=5, pady=5)
        num1_entry = ttk.Entry(entry_frame, textvariable=self.num1_var)
        num1_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(entry_frame, text="Number 2:").grid(row=1, column=0, padx=5, pady=5)
        num2_entry = ttk.Entry(entry_frame, textvariable=self.num2_var)
        num2_entry.grid(row=1, column=1, padx=5, pady=5)

    def create_buttons(self):
        button_frame = ttk.Frame(self.root)
        button_frame.grid(row=1, column=0, columnspan=2, sticky="nsew")

        buttons = [
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('/', 2, 3),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('*', 3, 3),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3),
            ('0', 5, 0), ('.', 5, 1), ('=', 5, 2), ('+', 5, 3),
            ('C', 6, 0)
        ]

        for (text, row, col) in buttons:
            button = ttk.Button(button_frame, text=text, command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, sticky="nsew")

    def on_button_click(self, text):
        if text == '=':
            self.calculate()
        elif text == 'C':
            self.num1_var.set("")
            self.num2_var.set("")
            self.result_var.set("")
        else:
            current_entry = self.num1_var if not self.num1_var.get() else self.num2_var
            current_entry.set(current_entry.get() + text)

    def calculate(self):
        try:
            num1 = float(self.num1_var.get())
            num2 = float(self.num2_var.get())
            result = num1 + num2  # Default operation is addition

            self.result_var.set(result)

        except ValueError:
            self.result_var.set("Error: Invalid input")

        # Display the result in a pop-up window
        result_window = tk.Toplevel(self.root)
        result_window.title("Result")
        ttk.Label(result_window, text=f"Result: {result}").pack(padx=10, pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
