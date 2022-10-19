import sys
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
import requests

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.write_text_element()
        self.screen()

    def screen(self):
        self.setWindowTitle("Scanner")
        self.setFixedSize(QSize(1350, 800))

    def write_text_element(self):
        # displaying photo



        # displaying the text of the surname
        text_surname = QLabel("Фамилия:", self)
        text_surname.setGeometry(300, 50, 200, 20)
        text_surname.setFont(QFont("SansSerif", 15))

        # displaying the text of the name
        text_name = QLabel("Имя:", self)
        text_name.setGeometry(300, 90, 200, 20)
        text_name.setFont(QFont("SansSerif", 15))

        # displaying the text of the patronymic
        text_patronymic = QLabel("Отчество:", self)
        text_patronymic.setGeometry(300, 130, 200, 20)
        text_patronymic.setFont(QFont("SansSerif", 15))

        # displaying the text of the date_of_birth
        date_of_birth = QLabel("Дата рождения:", self)
        date_of_birth.setGeometry(300, 170, 200, 20)
        date_of_birth.setFont(QFont("SansSerif", 15))

        # displaying the text of the place_of_registration
        place_of_birth = QLabel("Место рождения:", self)
        place_of_birth.setGeometry(300, 210, 200, 20)
        place_of_birth.setFont(QFont("SansSerif", 15))

        # displaying the text of the place_of_registration
        place_of_registration = QLabel("Место регистрации:", self)
        place_of_registration.setGeometry(300, 250, 200, 20)
        place_of_registration.setFont(QFont("SansSerif", 15))



