import copy

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from PyQt5 import QtCore


class MainWindow(QMainWindow):

    def __init__(self, database):
        super(MainWindow, self).__init__()

        self.screen_()
        self.row_to_base_id = dict()
        self.database = database
        self.index_row = -1
        self.buttons()

        self.create_table()
        self.load_data()

        self.write_text_element()

    def screen_(self):
        self.setWindowTitle("Scanner")
        self.setFixedSize(QSize(1400, 800))

    def write_text_element(self):

        # displaying the text of the surname, name...

        text_surname = QLabel("Фамилия:", self)
        text_surname.setGeometry(350, 50, 200, 30)
        text_surname.setFont(QFont("SansSerif", 15))
        text_surname.setAlignment(Qt.AlignRight)

        text_name = QLabel("Имя:", self)
        text_name.setGeometry(350, 90, 200, 30)
        text_name.setFont(QFont("SansSerif", 15))
        text_name.setAlignment(Qt.AlignRight)

        text_patronymic = QLabel("Отчество:", self)
        text_patronymic.setGeometry(350, 130, 200, 30)
        text_patronymic.setFont(QFont("SansSerif", 15))
        text_patronymic.setAlignment(Qt.AlignRight)

        date_of_birth = QLabel("Дата рождения:", self)
        date_of_birth.setGeometry(350, 170, 200, 30)
        date_of_birth.setFont(QFont("SansSerif", 15))
        date_of_birth.setAlignment(Qt.AlignRight)

        place_of_birth = QLabel("Место рождения:", self)
        place_of_birth.setGeometry(350, 210, 200, 30)
        place_of_birth.setFont(QFont("SansSerif", 15))
        place_of_birth.setAlignment(Qt.AlignRight)

        place_of_registration = QLabel("Место регистрации:", self)
        place_of_registration.setGeometry(300, 250, 250, 30)
        place_of_registration.setFont(QFont("SansSerif", 15))
        place_of_registration.setAlignment(Qt.AlignRight)

        issued_by_whom = QLabel("Кем выдан:", self)
        issued_by_whom.setGeometry(350, 290, 200, 30)
        issued_by_whom.setFont(QFont("SansSerif", 15))
        issued_by_whom.setAlignment(Qt.AlignRight)

        date_of_issue = QLabel("Дата выдачи:", self)
        date_of_issue.setGeometry(850, 50, 200, 30)
        date_of_issue.setFont(QFont("SansSerif", 15))
        date_of_issue.setAlignment(Qt.AlignRight)

        series_and_number = QLabel("Серия и номер:", self)
        series_and_number.setGeometry(850, 90, 200, 30)
        series_and_number.setFont(QFont("SansSerif", 15))
        series_and_number.setAlignment(Qt.AlignRight)

        inn = QLabel("ИНН:", self)
        inn.setGeometry(850, 130, 200, 30)
        inn.setFont(QFont("SansSerif", 15))
        inn.setAlignment(Qt.AlignRight)

        snils = QLabel("СНИЛС:", self)
        snils.setGeometry(850, 170, 200, 30)
        snils.setFont(QFont("SansSerif", 15))
        snils.setAlignment(Qt.AlignRight)

        # data in db

        self.labels = [(QLineEdit("", self)) for x in range(12)]

        self.surname_bd = self.labels[0]
        self.surname_bd.setGeometry(570, 50, 250, 30)
        self.surname_bd.setFont(QFont("SansSerif", 15))
        self.surname_bd.setEnabled(False)

        self.name_bd = self.labels[1]
        self.name_bd.setGeometry(570, 90, 250, 30)
        self.name_bd.setFont(QFont("SansSerif", 15))
        self.name_bd.setEnabled(False)

        self.patronymic_bd = self.labels[2]
        self.patronymic_bd.setGeometry(570, 130, 250, 30)
        self.patronymic_bd.setFont(QFont("SansSerif", 15))
        self.patronymic_bd.setEnabled(False)

        self.date_of_birth_bd = self.labels[3]
        self.date_of_birth_bd.setGeometry(570, 170, 250, 30)
        self.date_of_birth_bd.setFont(QFont("SansSerif", 15))
        self.date_of_birth_bd.setEnabled(False)

        self.place_of_birth_bd = self.labels[4]
        self.place_of_birth_bd.setGeometry(570, 210, 250, 30)
        self.place_of_birth_bd.setFont(QFont("SansSerif", 15))
        self.place_of_birth_bd.setEnabled(False)

        self.place_of_registration_bd = self.labels[5]
        self.place_of_registration_bd.setGeometry(570, 250, 250, 30)
        self.place_of_registration_bd.setFont(QFont("SansSerif", 15))
        self.place_of_registration_bd.setEnabled(False)

        self.issued_by_whom_bd = self.labels[7]
        self.issued_by_whom_bd.setGeometry(570, 290, 250, 30)
        self.issued_by_whom_bd.setFont(QFont("SansSerif", 15))
        self.issued_by_whom_bd.setEnabled(False)

        self.date_of_issue_bd = self.labels[8]
        self.date_of_issue_bd.setGeometry(1070, 50, 250, 30)
        self.date_of_issue_bd.setFont(QFont("SansSerif", 15))
        self.date_of_issue_bd.setEnabled(False)

        self.series_and_number_bd = self.labels[6]
        self.series_and_number_bd.setGeometry(1070, 90, 250, 30)
        self.series_and_number_bd.setFont(QFont("SansSerif", 15))
        self.series_and_number_bd.setEnabled(False)

        self.inn_bd = self.labels[9]
        self.inn_bd.setGeometry(1070, 130, 250, 30)
        self.inn_bd.setFont(QFont("SansSerif", 15))
        self.inn_bd.setEnabled(False)

        self.snils_bd = self.labels[10]
        self.snils_bd.setGeometry(1070, 170, 250, 30)
        self.snils_bd.setFont(QFont("SansSerif", 15))
        self.snils_bd.setEnabled(False)

        self.photo_bd = self.labels[11]
        self.photo_bd.setGeometry(100, 100, 150, 30)

    def buttons(self):

        self.button_add = QPushButton("Добавить файл", self)
        self.button_add.setGeometry(900, 210, 150, 30)
        self.button_add.clicked.connect(self.click_add)

        self.button_edit = QPushButton("Редактировать", self)
        self.button_edit.setGeometry(900, 250, 150, 30)
        self.button_edit.setEnabled(False)
        self.button_edit.clicked.connect(self.click_edit)

        self.button_delete = QPushButton("Удалить", self)
        self.button_delete.setGeometry(900, 290, 150, 30)
        self.button_delete.setEnabled(False)
        self.button_delete.clicked.connect(self.delete_person_button)

        self.button_save = QPushButton("Сохранить", self)
        self.button_save.setGeometry(1120, 210, 150, 30)
        self.button_save.setEnabled(False)

    def click_add(self):
        pass

    def click_edit(self):
        self.surname_bd.setEnabled(True)
        self.name_bd.setEnabled(True)
        self.patronymic_bd.setEnabled(True)
        self.date_of_birth_bd.setEnabled(True)
        self.place_of_birth_bd.setEnabled(True)
        self.place_of_registration_bd.setEnabled(True)
        self.issued_by_whom_bd.setEnabled(True)
        self.date_of_issue_bd.setEnabled(True)
        self.series_and_number_bd.setEnabled(True)
        self.inn_bd.setEnabled(True)
        self.snils_bd.setEnabled(True)

    def click_save(self):
        pass

    def eventFilter(self, source, event):
        if event.type() == QtCore.QEvent.MouseButtonPress:
            if event.button() == QtCore.Qt.LeftButton:
                index = self.tableWidget.indexAt(event.pos())
                self.index_row = index.row()
                # parsing table
                for i in range(12):
                    self.labels[i].setText(self.tableWidget.item(self.index_row, i).text())

                if index.data():
                    self.button_edit.setEnabled(True)
                    self.button_delete.setEnabled(True)
                elif not index.data():
                    self.button_edit.setEnabled(False)
                    self.button_delete.setEnabled(False)

        return super(MainWindow, self).eventFilter(source, event)

    def create_table(self):
        self.tableWidget = QTableWidget(self)
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(12)
        self.tableWidget.setGeometry(50, 400, 1300, 350)
        self.tableWidget.setFixedSize(1300, 350)
        self.tableWidget.setObjectName("tableWidget")
        
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)

        self.tableWidget.viewport().installEventFilter(self)

        self.headerLabels = (["Фамилия", "Имя", "Отчество", "Дата Рождения", "Место Рождения", "Место регистрации", "Серия и Номер", "Кем выдан", "Дата выдачи", "ИНН", "СНИЛС", "ФОТО"])
        for i in range(len(self.headerLabels)):
            self.tableWidget.setHorizontalHeaderItem(i, QTableWidgetItem(self.headerLabels[i]))

    def load_data(self):
        result = self.database.get_persons()
        self.tableWidget.setRowCount(0)

        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            self.row_to_base_id[row_number] = row_data[0]
            for column_number, data in enumerate(row_data[1:]):
                self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    def delete_person_button(self):
        self.delete_messagebox()

    def delete_messagebox(self):
        self.msg_delete = QMessageBox()
        self.msg_delete.setWindowTitle("Удаление")
        self.msg_delete.setIcon(QMessageBox.Question)
        self.msg_delete.setText("Вы действительно хотите удалить пользователя?")
        self.msg_delete.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        res = self.msg_delete.exec_()

        if res == QMessageBox.Yes:
            self.database.delete_person(self.row_to_base_id[self.index_row])
        if res == QMessageBox.Cancel:
            pass


















