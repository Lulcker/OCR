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
        date_of_issue.setGeometry(900, 50, 200, 30)
        date_of_issue.setFont(QFont("SansSerif", 15))
        date_of_issue.setAlignment(Qt.AlignRight)

        series_and_number = QLabel("Серия и номер:", self)
        series_and_number.setGeometry(900, 90, 200, 30)
        series_and_number.setFont(QFont("SansSerif", 15))
        series_and_number.setAlignment(Qt.AlignRight)

        inn = QLabel("ИНН:", self)
        inn.setGeometry(900, 130, 200, 30)
        inn.setFont(QFont("SansSerif", 15))
        inn.setAlignment(Qt.AlignRight)

        snils = QLabel("СНИЛС:", self)
        snils.setGeometry(900, 170, 200, 30)
        snils.setFont(QFont("SansSerif", 15))
        snils.setAlignment(Qt.AlignRight)

        #label = QLabel("", self)
        #label.setFont(QFont("SansSerif", 15))
        self.labels = [(QLabel("", self)) for x in range(12)]

        self.surname_bd = self.labels[0]
        self.surname_bd.setGeometry(600, 50, 250, 30)
        self.surname_bd.setFont(QFont("SansSerif", 15))
        #self.labels[0].setGeometry(600, 50, 250, 30)
        self.labels[1].setGeometry(600, 90, 250, 30)
        self.labels[2].setGeometry(600, 130, 250, 30)
        self.labels[3].setGeometry(600, 170, 250, 30)
        self.labels[4].setGeometry(600, 210, 250, 30)
        self.labels[5].setGeometry(600, 250, 250, 30)
        self.labels[6].setGeometry(1120, 290, 250, 30)
        self.labels[7].setGeometry(1120, 50, 250, 30)
        self.labels[8].setGeometry(1120, 90, 250, 30)
        self.labels[9].setGeometry(1120, 130, 250, 30)
        self.labels[10].setGeometry(1120, 170, 250, 30)
        self.labels[11].setGeometry(100, 100, 250, 30)

    def buttons(self):

        self.button_add = QPushButton("Добавить файл", self)
        self.button_add.setGeometry(900, 210, 150, 30)
        self.button_add.clicked.connect(self.click_add)

        self.button_edit = QPushButton("Редактировать", self)
        self.button_edit.setGeometry(900, 250, 150, 30)
        self.button_edit.setEnabled(False)

        self.button_delete = QPushButton("Удалить", self)
        self.button_delete.setGeometry(900, 290, 150, 30)
        self.button_delete.setEnabled(False)
        self.button_delete.clicked.connect(self.delete_person_button)

    def click_add(self):
        print("q")
        self

    def click_edit(self):
        self.button_edit.setEnabled(True)

    def eventFilter(self, source, event):
        if event.type() == QtCore.QEvent.MouseButtonPress:
            if event.button() == QtCore.Qt.LeftButton:
                index = self.tableWidget.indexAt(event.pos())
                self.index_row = index.row()
                # parsing table
                for i in range(12):
                    self.labels[i].setText(self.tableWidget.item(self.index_row, i).text())
                    #print(self.labels[i])

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
        self.database.delete_person(self.row_to_base_id[self.index_row])
















