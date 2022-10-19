import sys
from MainWindow import Window
from PyQt6.QtWidgets import *


def main():
    app = QApplication(sys.argv)

    window = Window.MainWindow()
    window.show()

    app.exec()


if __name__ == '__main__':
    main()

