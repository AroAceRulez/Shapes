from tkinter import *
from tkinter import ttk

root= Tk()
root.title("ShapeMaker")
root.geometry("1000x600")
root.configure(bg="pink1")

canvas = Canvas(root, width=990, height=490, highlightthickness=5, highlightbackground="MistyRose2", bg="white")
canvas.pack()

label= Label(root, text="Choose Color", bg="pink1")
label.place(relx=0.6, rely=0.9, anchor=CENTER)

colors=["red", "blue", "green", "yellow", "orange", "black"]

colorsdd= ttk.Combobox(root, state="readonly", values=colors, width=10)
colorsdd.place(relx=0.8, rely=0.9, anchor=CENTER)

root.mainloop()