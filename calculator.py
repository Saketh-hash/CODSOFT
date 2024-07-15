import tkinter as tk
from tkinter import messagebox
def add():
    try:
        result = float(entry1.get())+float(entry2.get())
        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers")
def sub():
    try:
        result = float(entry1.get()) - float(entry2.get())
        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers")
def mul():
    try:
        result = float(entry1.get()) * float(entry2.get())
        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers")
def div():
    try:
        if float(entry2.get()) == 0:
            messagebox.showerror("Division by zero", "Cannot divide by zero")
        else:
            result = float(entry1.get()) / float(entry2.get())
            result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers")
def reset():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    result_label.config(text="Result: ")
root = tk.Tk()
root.title("Simple Calculator")
tk.Label(root, text = "Enter first Number: ").grid(row = 0, column = 0)
entry1 = tk.Entry(root)
entry1.grid(row = 0, column = 1)
tk.Label(root, text = "Enter second Number: ").grid(row = 1, column = 0)
entry2 = tk.Entry(root)
entry2.grid(row = 1, column = 1)
tk.Label(root, text = "Choose operation: ").grid(row = 2, column = 0)
btn_add = tk.Button(root, text = "Add", command = add)
btn_add.grid(row = 2, column = 1)
btn_sub = tk.Button(root, text = "Subtract", command = sub)
btn_sub.grid(row = 3, column = 1)
btn_mul = tk.Button(root, text = "Multiply", command = mul)
btn_mul.grid(row = 4, column = 1)
btn_div = tk.Button(root, text = "Divide", command = div)
btn_div.grid(row = 5, column = 1)
btn_reset = tk.Button(root, text = "Reset", command = reset)
btn_reset.grid(row = 6, column = 1)
result_label = tk.Label(root, text = "Result: ")
result_label.grid(row = 7, columnspan = 2)
root.mainloop()