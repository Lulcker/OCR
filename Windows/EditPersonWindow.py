from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from PyQt5 import QtCore

from Windows import WindowsManager
from tools import file_manager

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
        self.setFixedSize(QSize(1200, 450))

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
        input_restriction = QRegExpValidator(QRegExp("[а-яА-Я]{3,}"))
        date_restriction = QRegExpValidator(QRegExp("^(0[1-9]|[12][0-9]|3[01])\-(0[1-9]|1[012])\-\d{4}$"))
        passport_restriction = QRegExpValidator(QRegExp("^[0-9]{4}\ [0-9]{6}$"))
        inn_restriction = QRegExpValidator(QRegExp("^[0-9]{12}$"))
        snils_restriction = QRegExpValidator(QRegExp("^[0-9]{3}\-[0-9]{3}\-[0-9]{3}\ [0-9]{2}$"))
        self.mass_labels = [(QLineEdit("", self)) for x in range(12)]

        self.surname_add = self.mass_labels[0]
        self.surname_add.setGeometry(520, 50, 200, 30)
        self.surname_add.setPlaceholderText("Введите фамилию")
        self.surname_add.setValidator(input_restriction)
        self.surname_add.editingFinished.connect(lambda: self.surname_add.setText(self.surname_add.text().title()))
        self.surname_add.setObjectName("фамилия")

        self.name_add = self.mass_labels[1]
        self.name_add.setGeometry(520, 90, 200, 30)
        self.name_add.setPlaceholderText("Введите имя")
        self.name_add.setValidator(input_restriction)
        self.name_add.editingFinished.connect(lambda: self.name_add.setText(self.name_add.text().title()))
        self.name_add.setObjectName("имя")

        self.patronymic_add = self.mass_labels[2]
        self.patronymic_add.setGeometry(520, 130, 200, 30)
        self.patronymic_add.setPlaceholderText("Введите отчество")
        self.patronymic_add.setValidator(input_restriction)
        self.patronymic_add.editingFinished.connect(lambda: self.patronymic_add.setText(self.patronymic_add.text().title()))
        self.patronymic_add.setObjectName("отчество")

        self.date_of_birth_add = self.mass_labels[3]
        self.date_of_birth_add.setGeometry(520, 170, 200, 30)
        self.date_of_birth_add.setPlaceholderText("Введите дату рождения")
        self.date_of_birth_add.setValidator(date_restriction)
        self.date_of_birth_add.mousePressEvent = lambda x: self.date_of_birth_add.setInputMask("00-00-0000")
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
        self.date_of_issue_add.setValidator(date_restriction)
        self.date_of_issue_add.mousePressEvent = lambda x: self.date_of_issue_add.setInputMask("00-00-0000")
        self.date_of_issue_add.setObjectName("когда выдан")

        self.series_and_number_add = self.mass_labels[6]
        self.series_and_number_add.setGeometry(970, 90, 200, 30)
        self.series_and_number_add.setPlaceholderText("Введите серию и номер паспорта")
        self.series_and_number_add.mousePressEvent = lambda x: self.series_and_number_add.setInputMask("0000 000000")
        self.series_and_number_add.setValidator(passport_restriction)
        self.series_and_number_add.setObjectName("серия и номер паспорта")

        self.inn_add = self.mass_labels[9]
        self.inn_add.setGeometry(970, 130, 200, 30)
        self.inn_add.setPlaceholderText("Введите ИНН")
        self.inn_add.mousePressEvent = lambda x: self.inn_add.setInputMask("000000000000")
        self.inn_add.setValidator(inn_restriction)
        self.inn_add.setObjectName("ИНН")

        self.snils_add = self.mass_labels[10]
        self.snils_add.setGeometry(970, 170, 200, 30)
        self.snils_add.setPlaceholderText("Введите СНИЛС")
        self.snils_add.mousePressEvent = lambda x: self.snils_add.setInputMask("000-000-000 00")
        self.snils_add.setValidator(snils_restriction)
        self.snils_add.setObjectName("СНИЛС")

        self.photo_add = self.mass_labels[11]
        self.photo_add.setObjectName("фото")
        self.photo_add.close()

        self.photo_person = QLabel(self)
        self.photo_person.setGeometry(50, 70, 200, 250)

    def buttons(self):

        self.button_add_image_passport = QPushButton("Добавить фото паспорта\n для сканирования", self)
        self.button_add_image_passport.setGeometry(780, 210, 170, 45)
        self.button_add_image_passport.clicked.connect(self.click_add_img_passport)

        self.button_add_image_inn = QPushButton("Добавить фото ИНН\n для сканирования", self)
        self.button_add_image_inn.setGeometry(780, 265, 170, 45)
        self.button_add_image_inn.clicked.connect(self.click_add_img_inn)

        self.button_add_image_snils = QPushButton("Добавить фото СНИЛС\n для сканирования", self)
        self.button_add_image_snils.setGeometry(780, 320, 170, 45)
        self.button_add_image_snils.clicked.connect(self.click_add_img_snils)

        self.button_save_add = QPushButton("Сохранить", self)
        self.button_save_add.setGeometry(1000, 210, 150, 30)
        self.button_save_add.clicked.connect(self.click_save_add)

        self.button_add_image_person = QPushButton("Добавить фото", self)
        self.button_add_image_person.setGeometry(100, 20, 150, 30)
        self.button_add_image_person.clicked.connect(self.click_add_photo_face)

    def click_add_img_passport(self):
        QFileDialog.getOpenFileNames(self, 'Open File', 'Users/', 'JPG File(*.jpg);;JPEG File(*.jpeg);;PNG File(*.png)')
        # потом переделать, когда Ванина часть будет готова

    def click_add_img_inn(self):
        QFileDialog.getOpenFileNames(self, 'Open File', 'Users/', 'JPG File(*.jpg);;JPEG File(*.jpeg);;PNG File(*.png)')
        # потом переделать, когда Ванина часть будет готова

    def click_add_img_snils(self):
        QFileDialog.getOpenFileNames(self, 'Open File', 'Users/', 'JPG File(*.jpg);;JPEG File(*.jpeg);;PNG File(*.png)')
        # потом переделать, когда Ванина часть будет готова

    def click_add_photo_face(self):
        photo_face = QFileDialog.getOpenFileNames(self, 'Open File', 'Users/', 'JPG File(*.jpg);;JPEG File(*.jpeg);;PNG File(*.png)')[0]
        self.photo_add.setText(''.join(photo_face))
        self.photo_person.setPixmap(QPixmap(self.photo_add.text()).scaled(200, 250))

    def click_save_add(self):
        person_data = [x.text() for x in self.mass_labels]
        if self.check_data():
            person_id = self.database.insert_person(person_data[:-1])
            file_manager.save_file(person_data[11], person_id, "photo.jpg")
            [x.clear() for x in self.mass_labels]
            self.photo_person.clear()
            person_data.insert(0, person_id)
            self.windows_manager.get_window(WindowsManager.WindowsNames.MainWindow).add_new_person(person_data[:-1])
            self.close()

    def check_data(self):
        lineEdits = self.findChildren(QLineEdit)
        text = ''
        for line_error in lineEdits:
            if (not line_error.text()) or not line_error.hasAcceptableInput():
                text = f'{text}Заполните поле {line_error.objectName()}\n'

        if text:
            msg = QMessageBox.information(self, "Внимание! Не все поля заполнены", text)
        else:
            return True



