from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from PyQt5 import QtCore

from Windows import WindowsManager


class EditPersonWindow(QWidget):
    def __init__(self, database, windows_manager):
        super(EditPersonWindow, self).__init__()
        self.windows_manager = windows_manager
        self.database = database

        self.screen_()
        self.ui_widgets()
        self.buttons()

    def screen_(self):
        self.setWindowTitle("Add person")
        self.setFixedSize(QSize(1200, 700))

    def ui_widgets(self):
        text_surname_add = QLabel("Фамилия:", self)
        text_surname_add.setGeometry(300, 50, 200, 30)
        text_surname_add.setFont(QFont("SansSerif", 15))
        text_surname_add.setAlignment(Qt.AlignRight)

        text_name_add = QLabel("Имя:", self)
        text_name_add.setGeometry(300, 90, 200, 30)
        text_name_add.setFont(QFont("SansSerif", 15))
        text_name_add.setAlignment(Qt.AlignRight)

        text_patronymic_add = QLabel("Отчество:", self)
        text_patronymic_add.setGeometry(300, 130, 200, 30)
        text_patronymic_add.setFont(QFont("SansSerif", 15))
        text_patronymic_add.setAlignment(Qt.AlignRight)

        text_date_of_birth_add = QLabel("Дата рождения:", self)
        text_date_of_birth_add.setGeometry(300, 170, 200, 30)
        text_date_of_birth_add.setFont(QFont("SansSerif", 15))
        text_date_of_birth_add.setAlignment(Qt.AlignRight)

        text_place_of_birth_add = QLabel("Место рождения:", self)
        text_place_of_birth_add.setGeometry(300, 210, 200, 30)
        text_place_of_birth_add.setFont(QFont("SansSerif", 15))
        text_place_of_birth_add.setAlignment(Qt.AlignRight)

        text_place_of_registration_add = QLabel("Место регистрации:", self)
        text_place_of_registration_add.setGeometry(250, 250, 250, 30)
        text_place_of_registration_add.setFont(QFont("SansSerif", 15))
        text_place_of_registration_add.setAlignment(Qt.AlignRight)

        text_issued_by_whom_add = QLabel("Кем выдан:", self)
        text_issued_by_whom_add.setGeometry(300, 290, 200, 30)
        text_issued_by_whom_add.setFont(QFont("SansSerif", 15))
        text_issued_by_whom_add.setAlignment(Qt.AlignRight)

        text_date_of_issue_add = QLabel("Дата выдачи:", self)
        text_date_of_issue_add.setGeometry(750, 50, 200, 30)
        text_date_of_issue_add.setFont(QFont("SansSerif", 15))
        text_date_of_issue_add.setAlignment(Qt.AlignRight)

        text_series_and_number_add = QLabel("Серия и номер:", self)
        text_series_and_number_add.setGeometry(750, 90, 200, 30)
        text_series_and_number_add.setFont(QFont("SansSerif", 15))
        text_series_and_number_add.setAlignment(Qt.AlignRight)

        text_inn_add = QLabel("ИНН:", self)
        text_inn_add.setGeometry(750, 130, 200, 30)
        text_inn_add.setFont(QFont("SansSerif", 15))
        text_inn_add.setAlignment(Qt.AlignRight)

        text_snils_add = QLabel("СНИЛС:", self)
        text_snils_add.setGeometry(750, 170, 200, 30)
        text_snils_add.setFont(QFont("SansSerif", 15))
        text_snils_add.setAlignment(Qt.AlignRight)

        # для ограничения ввода цифр в поля с букавками!
        input_restriction = QRegExpValidator(self)
        reg = QRegExp("[а-яА-Я]{25}")
        input_restriction.setRegExp(reg)

        self.surname_add = QLineEdit("", self)
        self.surname_add.setGeometry(520, 50, 200, 30)
        self.surname_add.setPlaceholderText("Введите фамилию")
        self.surname_add.setValidator(input_restriction)

        self.name_add = QLineEdit("", self)
        self.name_add.setGeometry(520, 90, 200, 30)
        self.name_add.setPlaceholderText("Введите имя")
        self.name_add.setValidator(input_restriction)

        self.patronymic_add = QLineEdit("", self)
        self.patronymic_add.setGeometry(520, 130, 200, 30)
        self.patronymic_add.setPlaceholderText("Введите отчество")
        self.patronymic_add.setValidator(input_restriction)

        self.date_of_birth_add = QLineEdit("", self)
        self.date_of_birth_add.setGeometry(520, 170, 200, 30)
        self.date_of_birth_add.setPlaceholderText("Введите дату рождения")
        self.date_of_birth_add.setInputMask("00-00-0000")

        self.place_of_birth_add = QLineEdit("", self)
        self.place_of_birth_add.setGeometry(520, 210, 200, 30)
        self.place_of_birth_add.setPlaceholderText("Введите место рождения")

        self.place_of_registration_add = QLineEdit("", self)
        self.place_of_registration_add.setGeometry(520, 250, 200, 30)
        self.place_of_registration_add.setPlaceholderText("Введите регистрацию")

        self.issued_by_whom_add = QLineEdit("", self)
        self.issued_by_whom_add.setGeometry(520, 290, 200, 30)
        self.issued_by_whom_add.setPlaceholderText("Введите кем выдан")

        self.date_of_issue_add = QLineEdit("", self)
        self.date_of_issue_add.setGeometry(970, 50, 200, 30)
        self.date_of_issue_add.setPlaceholderText("Введите когда выдан")

        self.series_and_number_add = QLineEdit("", self)
        self.series_and_number_add.setGeometry(970, 90, 200, 30)
        self.series_and_number_add.setPlaceholderText("Введите серию и номер паспорта")
        self.series_and_number_add.setInputMask("0000 000000")

        self.inn_add = QLineEdit("", self)
        self.inn_add.setGeometry(970, 130, 200, 30)
        self.inn_add.setPlaceholderText("Введите ИНН")
        self.inn_add.setInputMask("000000000000")

        self.snils_add = QLineEdit("", self)
        self.snils_add.setGeometry(970, 170, 200, 30)
        self.snils_add.setPlaceholderText("Введите СНИЛС")
        self.snils_add.setInputMask("000-000-000 00")

        self.photo_add = QLineEdit("", self)
        self.photo_add.setGeometry(100, 50, 200, 30)

        self.mass_add = [self.surname_add.text(), self.name_add.text(), self.patronymic_add.text(), self.date_of_birth_add.text(), self.place_of_birth_add.text(), self.place_of_registration_add.text(), self.issued_by_whom_add.text(), self.date_of_issue_add.text(), self.series_and_number_add.text(), self.inn_add.text(), self.snils_add.text(), self.photo_add.text()]

    def buttons(self):

        self.button_add_image = QPushButton("Добавить фото\n для сканирования", self)
        self.button_add_image.setGeometry(800, 210, 150, 40)

        self.save_add = QPushButton("Сохранить", self)
        self.save_add.setGeometry(800, 260, 150, 30)
        self.save_add.clicked.connect(self.click_save_add)

    def click_add(self):
        pass

    def click_save_add(self):
        if self.check_data():
            self.database.insert_person(self.mass_add)
            self.close()
        else:
            self.bad_input()

    def check_data(self):
        #здесь прописать проверку введенных полей
        return False

    @staticmethod
    def bad_input():
        msg_badinput = QMessageBox()
        msg_badinput.setWindowTitle("Ошибка")
        msg_badinput.setIcon(QMessageBox.Question)
        msg_badinput.setText("Неправильный ввод! Исправьте данные")
        msg_badinput.setStandardButtons(QMessageBox.Ok)
        res = msg_badinput.exec_()
        if res == QMessageBox.Ok:
            pass


