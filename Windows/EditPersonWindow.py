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

        self.mass_labels = [(QLineEdit("", self)) for x in range(12)]

        self.surname_add = self.mass_labels[0]
        self.surname_add.setGeometry(520, 50, 200, 30)
        self.surname_add.setPlaceholderText("Введите фамилию")
        self.surname_add.setValidator(input_restriction)
        self.surname_add.setObjectName("фамилия")

        self.name_add = self.mass_labels[1]
        self.name_add.setGeometry(520, 90, 200, 30)
        self.name_add.setPlaceholderText("Введите имя")
        self.name_add.setValidator(input_restriction)
        self.name_add.setObjectName("имя")

        self.patronymic_add = self.mass_labels[2]
        self.patronymic_add.setGeometry(520, 130, 200, 30)
        self.patronymic_add.setPlaceholderText("Введите отчество")
        self.patronymic_add.setValidator(input_restriction)
        self.patronymic_add.setObjectName("отчество")

        self.date_of_birth_add = self.mass_labels[3]
        self.date_of_birth_add.setGeometry(520, 170, 200, 30)
        self.date_of_birth_add.setPlaceholderText("Введите дату рождения")
        self.date_of_birth_add.mousePressEvent = self.mouse_pressed_date_of_birth
        self.date_of_birth_add.setObjectName("дата рождения")

        self.place_of_birth_add = self.mass_labels[4]
        self.place_of_birth_add.setGeometry(520, 210, 200, 30)
        self.place_of_birth_add.setPlaceholderText("Введите место рождения")
        self.place_of_birth_add.setObjectName("место рождения")

        self.place_of_registration_add = self.mass_labels[5]
        self.place_of_registration_add.setGeometry(520, 250, 200, 30)
        self.place_of_registration_add.setPlaceholderText("Введите место регистрации")
        self.place_of_registration_add.setObjectName("место регистрации")

        self.issued_by_whom_add = self.mass_labels[7]
        self.issued_by_whom_add.setGeometry(520, 290, 200, 30)
        self.issued_by_whom_add.setPlaceholderText("Введите кем выдан")
        self.issued_by_whom_add.setObjectName("кем выдан")

        self.date_of_issue_add = self.mass_labels[8]
        self.date_of_issue_add.setGeometry(970, 50, 200, 30)
        self.date_of_issue_add.setPlaceholderText("Введите когда выдан")
        self.date_of_issue_add.mousePressEvent = self.mouse_pressed_date_of_issue
        self.date_of_issue_add.setObjectName("когда выдан")

        self.series_and_number_add = self.mass_labels[6]
        self.series_and_number_add.setGeometry(970, 90, 200, 30)
        self.series_and_number_add.setPlaceholderText("Введите серию и номер паспорта")
        self.series_and_number_add.mousePressEvent = self.mouse_pressed_series
        self.series_and_number_add.setObjectName("серия и номер паспорта")

        self.inn_add = self.mass_labels[9]
        self.inn_add.setGeometry(970, 130, 200, 30)
        self.inn_add.setPlaceholderText("Введите ИНН")
        self.inn_add.mousePressEvent = self.mouse_pressed_inn
        self.inn_add.setObjectName("ИНН")

        self.snils_add = self.mass_labels[10]
        self.snils_add.setGeometry(970, 170, 200, 30)
        self.snils_add.setPlaceholderText("Введите СНИЛС")
        self.snils_add.mousePressEvent = self.mouse_pressed_snils
        self.snils_add.setObjectName("СНИЛС")

        self.photo_add = self.mass_labels[11]
        self.photo_add.setGeometry(100, 50, 200, 30)
        self.photo_add.setObjectName("фото")

    def buttons(self):

        self.button_add_image = QPushButton("Добавить фото\n для сканирования", self)
        self.button_add_image.setGeometry(800, 210, 150, 40)
        self.button_add_image.clicked.connect(self.click_add)

        self.save_add = QPushButton("Сохранить", self)
        self.save_add.setGeometry(800, 260, 150, 30)
        self.save_add.clicked.connect(self.click_save_add)

    def mouse_pressed_date_of_birth(self, event):
        self.date_of_birth_add.setInputMask("00-00-0000")

    def mouse_pressed_date_of_issue(self, event):
        self.date_of_issue_add.setInputMask("00-00-0000")

    def mouse_pressed_snils(self, event):
        self.snils_add.setInputMask("000-000-000 00")

    def mouse_pressed_inn(self, event):
        self.inn_add.setInputMask("000000000000")

    def mouse_pressed_series(self, event):
        self.series_and_number_add.setInputMask("0000 000000")

    def click_add(self):
        QFileDialog.getOpenFileNames(self, 'Open File', 'Users/', 'JPG File(*.jpg);;JPEG File(*.jpeg);;PNG File(*.png)')

    def click_save_add(self):
        self.mass_add = [x.text() for x in self.mass_labels]

        if self.check_data():
            self.database.insert_person(self.mass_add)
            self.close()
            [x.clear() for x in self.mass_labels]
        else:
            pass

    def check_data(self):
        lineEdits = self.findChildren(QLineEdit)
        text = ''

        for line_error in lineEdits:
            if not line_error.text():
                text = f'{text}Заполните поле {line_error.objectName()}\n'

        if text:
            msg = QMessageBox.information(self, "Внимание! Не все поля заполнены", text)
        else:
            return True

    '''@staticmethod
    def bad_input():
        msg_badinput = QMessageBox()
        msg_badinput.setWindowTitle("Ошибка")
        msg_badinput.setIcon(QMessageBox.Warning)
        msg_badinput.setText("Неправильный ввод! Исправьте данные")
        msg_badinput.setStandardButtons(QMessageBox.Ok)
        res = msg_badinput.exec_()
        if res == QMessageBox.Ok:
            pass'''


