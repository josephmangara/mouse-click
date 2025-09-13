from pynput.mouse import Button, Controller
from tkinter import *
from tkinter import ttk

mouse = Controller()
root = Tk()
root.title("circle")

canvas = Canvas(root, width=100, height=100, bg="white")
canvas.pack()

center_x = 50
center_y = 50
radius = 25

x0 = center_x - radius
y0 = center_y - radius
x1 = center_x + radius
y1 = center_y + radius

canvas.create_oval(x0, y0, x1, y1, fill="red", outline="darkred", width=2)


root.mainloop()
