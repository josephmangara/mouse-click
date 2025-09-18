import sys
import time
from PyQt5 import QtWidgets, QtCore, QtGui
from pynput import mouse


class Overlay(QtWidgets.QWidget):
    showCircleSignal = QtCore.pyqtSignal(int, int, object)

    def __init__(self):
        super().__init__()
        self.showCircleSignal.connect(self.show_circle)

        # Frameless, transparent overlay
        self.setWindowFlags(
            QtCore.Qt.FramelessWindowHint
            | QtCore.Qt.WindowStaysOnTopHint
            | QtCore.Qt.Tool
            | QtCore.Qt.BypassWindowManagerHint
        )
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents)

        # Cover the whole screen
        screen = QtWidgets.QApplication.primaryScreen().geometry()
        self.setGeometry(screen)

        self.circles = []
        self.show()

    def show_circle(self, x, y, color=QtCore.Qt.red):
        circle = {"x": x, "y": y, "color": color, "created": time.time()}
        self.circles.append(circle)
        self.update()

        # remove after 1s
        QtCore.QTimer.singleShot(1000, lambda: self.remove_circle(circle))

    def remove_circle(self, circle):
        if circle in self.circles:
            self.circles.remove(circle)
            self.update()

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)

        for c in self.circles:
            pen = QtGui.QPen(QtGui.QColor(c["color"]))
            pen.setWidth(4)
            painter.setPen(pen)
            painter.setBrush(QtCore.Qt.NoBrush)
            painter.drawEllipse(QtCore.QPoint(c["x"], c["y"]), 20, 20)


class MouseWorker(QtCore.QThread):
    clicked = QtCore.pyqtSignal(int, int, object)

    def run(self):
        def on_click(x, y, button, pressed):
            if pressed:
                color = QtCore.Qt.red if button == mouse.Button.left else QtCore.Qt.blue
                self.clicked.emit(x, y, color)

        with mouse.Listener(on_click=on_click) as listener:
            listener.join()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    overlay = Overlay()

    worker = MouseWorker()
    worker.clicked.connect(overlay.show_circle)
    worker.start()

    sys.exit(app.exec_())
