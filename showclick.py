import queue
from tkinter import Tk, Toplevel, Canvas
from pynput import mouse

# circle parameters
DIAMETER = 50
DURATION = 500  
OUTLINE_WIDTH = 4

click_queue = queue.Queue()


def on_click(x, y, button, pressed):
    if button == mouse.Button.left and pressed:
        click_queue.put((int(x), int(y)))


def start_listener():
    listener = mouse.Listener(on_click=on_click)
    listener.start()
    return listener


class ClickOverlay:
    def __init__(self, root):
        self.root = root
        self.root.withdraw()
        self.poll_queue()  # start polling queue

    def poll_queue(self):
        try:
            while True:
                x, y = click_queue.get_nowait()
                self.show_circle(x, y)
        except queue.Empty:
            pass
        self.root.after(25, self.poll_queue)

    def show_circle(self, x, y):
        d = DIAMETER
        r = d // 2

        win = Toplevel(self.root)
        win.overrideredirect(True)
        win.attributes("-topmost", True)

        # set initial transparency
        win.attributes("-alpha", 0.5)

        # window position
        win.geometry(f"{d}x{d}+{x - r}+{y - r}")

        # draw circle on canvas
        c = Canvas(win, width=d, height=d, highlightthickness=0, bg="black")
        c.pack(fill="both", expand=True)

        c.create_oval(OUTLINE_WIDTH // 2,
                      OUTLINE_WIDTH // 2,
                      d - OUTLINE_WIDTH // 2,
                      d - OUTLINE_WIDTH // 2,
                      outline="#ADD8E6",
                      width=OUTLINE_WIDTH)

        # fade-out animation 
        self.fade_out(win, 0.9, steps=15)

    def fade_out(self, win, alpha, steps=15):
        if steps <= 0:
            win.destroy()
            return
        alpha -= 0.05
        win.attributes("-alpha", max(alpha, 0))
        win.after(DURATION // 15, self.fade_out, win, alpha, steps - 1)


def main():
    root = Tk()
    app = ClickOverlay(root)

    listener = start_listener()

    try:
        root.mainloop()
    finally:
        listener.stop()


if __name__ == "__main__":
    main()
