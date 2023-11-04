import tkinter as tk
from tkinter import ttk, messagebox
import secrets
import string
import sqlite3

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        # Variables
        self.length_var = tk.StringVar()
        self.complexity_var = tk.StringVar(value="Low")
        self.generated_password_var = tk.StringVar()

        # Create GUI elements
        ttk.Label(root, text="Password Length:").grid(row=0, column=0, padx=10, pady=10)
        self.length_entry = ttk.Entry(root, textvariable=self.length_var)
        self.length_entry.grid(row=0, column=1, padx=10, pady=10)

        ttk.Label(root, text="Complexity:").grid(row=1, column=0, padx=10, pady=10)
        self.complexity_combobox = ttk.Combobox(root, values=["Low", "Medium", "High"], textvariable=self.complexity_var)
        self.complexity_combobox.grid(row=1, column=1, padx=10, pady=10)

        generate_button = ttk.Button(root, text="Generate Password", command=self.generate_password)
        generate_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        ttk.Label(root, text="Generated Password:").grid(row=3, column=0, padx=10, pady=10)
        self.generated_password_label = ttk.Label(root, textvariable=self.generated_password_var)
        self.generated_password_label.grid(row=3, column=1, padx=10, pady=10)

        # Database setup
        self.conn = sqlite3.connect("passwords.db")
        self.cursor = self.conn.cursor()
        self.create_table()

    def generate_password(self):
        try: #exception handling
            password_length = int(self.length_var.get())
            complexity = self.complexity_var.get().lower()

            if password_length <= 0:
                messagebox.showwarning("Warning", "Please enter a valid password length.")
                return

            charset = self.get_charset(complexity)
            generated_password = ''.join(secrets.choice(charset) for _ in range(password_length))
            self.generated_password_var.set(generated_password)

            # Save password to the database
            self.save_password(generated_password)

        except ValueError:
            messagebox.showwarning("Warning", "Please enter a valid number for the password length.")

    def get_charset(self, complexity):
        if complexity == "low":
            return string.ascii_letters + string.digits
        elif complexity == "medium":
            return string.ascii_letters + string.digits + string.punctuation
        else:
            return string.ascii_letters + string.digits + string.punctuation + string.ascii_letters.upper()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS passwords
                            (id INTEGER PRIMARY KEY AUTOINCREMENT, password TEXT)''')
        self.conn.commit()

    def save_password(self, password):
        self.cursor.execute("INSERT INTO passwords (password) VALUES (?)", (password,))
        self.conn.commit()

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
