import tkinter as tk
from pynput import mouse
import threading
import time


# Tkinter window setup 
root = tk.Tk()
root.attributes("-topmost", True)
root.overrideredirect(True)
root.attributes("-transparentcolor", "black")
root.geometry(f"{root.winfo_screenmmwidth()}x{root.winfo_screenmmheight()}+0+0")
root.configure(bg="black")

canvas = tk.Canvas(root, bg="black", highlightthickness=0)
canvas.pack(fill="both", expand=True)

def show_circle(x,y):
    r = 20
    circle = canvas.create_oval(x-r, y-r, x+r, y+r, outline="blue", width=3)

    def remove_circle():
        time.sleep(1)
        canvas.delete(circle)
    
    threading.Thread(target=remove_circle, daemon=True).start()

