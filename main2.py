from tkinter import Tk, Button

root = Tk()
button1 = Button(root, text="Кнопка 1")
button2 = Button(root, text="Кнопка 2")
button1.place(x=100, y=100)
button2.place(x=100, y=150)
root.mainloop()
