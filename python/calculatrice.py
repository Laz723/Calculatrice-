"""
Calculatrice — tout-en-un.
Regroupe la logique de calcul (ex-fonctions.py) et l'interface
graphique Tkinter (ex-interface.py) dans un seul fichier.
"""

import tkinter as tk
from tkinter import messagebox


# ============================================================
#  Logique de calcul
# ============================================================
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Erreur! Division par zéro."
    return x / y


# ============================================================
#  Interface graphique
# ============================================================
class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculatrice")
        self.root.geometry("450x400")
        self.root.configure(bg='#f0f0f0')

        self.display = tk.Entry(root, width=25, justify='right', font=('Arial', 16))
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('+', 4, 1), ('=', 4, 2), ('C', 4, 3)
        ]

        for (text, row, col) in buttons:
            button = tk.Button(root, text=text, width=5, height=2, font=('Arial', 16),
                               command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, padx=5, pady=5)

    def on_button_click(self, char):
        if char == 'C':
            self.display.delete(0, tk.END)
        elif char == '=':
            try:
                result = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(0, str(result))
            except Exception:
                messagebox.showerror("Erreur", "Expression invalide")
        else:
            self.display.insert(tk.END, char)


if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
