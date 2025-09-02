import sys
import threading
import time
from PyQt5 import QtWidgets, QtCore, QtGui
from pynput import mouse


class Overlay(QtWidgets.QWidget):
    showCircleSignal = QtCore.pyqtSignal(int, int, object)

    def __init__(self):
        super().__init__()

        
        self.showCircleSignal.connect(self.show_circle)

        # Fullscreen transparent overlay
        self.setWindowFlags(
            QtCore.Qt.FramelessWindowHint
            | QtCore.Qt.WindowStaysOnTopHint
            | QtCore.Qt.Tool
        )
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.showFullScreen()

        self.circles = []

    def show_circle(self, x, y, color=QtCore.Qt.red):
        circle = {"x": x, "y": y, "color": color}
        self.circles.append(circle)
        self.update()

        def remove():
            time.sleep(1)
            if circle in self.circles:
                self.circles.remove(circle)
                self.update()

        threading.Thread(target=remove, daemon=True).start()

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)

        for c in self.circles:
            pen = QtGui.QPen(QtGui.QColor(c["color"]))
            pen.setWidth(4)
            painter.setPen(pen)
            painter.setBrush(QtCore.Qt.NoBrush)
            painter.drawEllipse(QtCore.QPoint(c["x"], c["y"]), 20, 20)


def on_click(x, y, button, pressed):
    if pressed:
        color = QtCore.Qt.red if button == mouse.Button.left else QtCore.Qt.blue
        
        overlay.showCircleSignal.emit(x, y, color)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    overlay = Overlay()

    listener = mouse.Listener(on_click=on_click)
    listener.start()

    sys.exit(app.exec_())
