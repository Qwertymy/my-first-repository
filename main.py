import tkinter as tk

def greet():
    name = entry.get()
    greeting_label.config(text=f"Привет, {name}, а я программа!")

root = tk.Tk()
root.title("Приветствие")

instruction_label = tk.Label(root, text="Как вас зовут?")
instruction_label.pack()

entry = tk.Entry(root)
entry.pack()

greet_button = tk.Button(root, text="А вас как?", command=greet)
greet_button.pack()

greeting_label = tk.Label(root, text="")
greeting_label.pack()

root.mainloop()