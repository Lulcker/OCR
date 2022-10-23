import sys
from MainWindow import Window
from DataBase import DataBase
from PyQt5.QtWidgets import *


def main():
    app = QApplication(sys.argv)

    data = DataBase.DataBaseCluster('SQLite/SQLiteBase.db')

    window = Window.MainWindow(data)
    window.show()
    app.exec()


if __name__ == '__main__':
    main()

