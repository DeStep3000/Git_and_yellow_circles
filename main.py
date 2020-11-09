import sys

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication
from random import randint


class Circle:
    def __init__(self, x, y, d):
        self.x = x
        self.y = y
        self.d = d

    def draw(self, painter):
        painter.setBrush(QColor(255, 238, 0))
        painter.setPen(QColor(255, 238, 0))
        painter.drawEllipse(self.x, self.y, self.d, self.d)


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        uic.loadUi('UI.ui', self)
        self.objects = []
        self.pushButton.clicked.connect(self.run)

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        for obj in self.objects:
            obj.draw(painter)
        painter.end()

    def run(self):
        x = randint(50, 600)
        y = randint(20, 600)
        d = randint(20, 50)
        self.objects.append(Circle(x, y, d))
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())