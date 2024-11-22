import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPainter, QColor

from random import randint
class Circle(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('circle.ui', self)
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)
        print('Changes')

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()


    def paint(self):
        self.do_paint = True
        self.repaint()


    def draw_circle(self, qp):
        qp.setBrush(QColor(randint(0,255), randint(0,255), randint(0,255)))
        size = randint(100, 400)
        qp.drawEllipse(250, 200, size, size)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Circle()
    ex.show()
    sys.exit(app.exec())

