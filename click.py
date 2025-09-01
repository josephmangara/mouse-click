import tkinter as tk
from pynput import mouse
import threading
import time

root = tk.Tk()
root.attributes("-topmost", True)   
root.overrideredirect(True)        
root.attributes("-fullscreen", True)  
root.configure(bg="white")          

canvas = tk.Canvas(root, bg="white", highlightthickness=0)
canvas.pack(fill="both", expand=True)

def show_circle(x, y):
    r = 20  
    circle = canvas.create_oval(x-r, y-r, x+r, y+r, outline="red", width=3)

    def remove_circle():
        time.sleep(1)  
        canvas.delete(circle)

    threading.Thread(target=remove_circle, daemon=True).start()

def on_click(x, y, button, pressed):
    if pressed:
        root.after(0, show_circle, x, y)

listener = mouse.Listener(on_click=on_click)
listener.start()

root.mainloop()
