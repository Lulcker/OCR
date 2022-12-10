from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from PyQt5 import QtCore
from enum import Enum

from Windows import WindowsManager
from tools import file_manager

class SortType(Enum):
    ByName = 1
    ByUpdated = 2

class MainWindow(QMainWindow):
    def __init__(self, database, windows_manager):
        super(MainWindow, self).__init__()
        self.windows_manager = windows_manager
        self.database = database

        self.row_to_base_id = list()
        self.loaded = 0
        self.limit = 10
        self.index_row = -1
        self.screen_()
        self.buttons()
        self.write_text_element()
        self.create_table()
        self.sorting_type = SortType.ByUpdated
        self.load_data(reset_data=True)
        self.new_photo_path = ''

    def screen_(self):
        self.setWindowTitle("Scanner")
        self.setFixedSize(QSize(1400, 800))
        self.statusBar().setMinimumWidth(1400)
        self.statusBar().setMinimumHeight(800)
        self.setMaximumWidth(1400)
        self.setMaximumHeight(800)

    def write_text_element(self):

        textData = (
            ("Фамилия:", (350, 50, 200, 30)),
            ("Имя:", (350, 90, 200, 30)),
            ("Отчество:", (350, 130, 200, 30)),
            ("Дата рождения:", (350, 170, 200, 30)),
            ("Место рождения:", (350, 210, 200, 30)),
            ("Место регистрации:", (300, 250, 250, 30)),
            ("Серия и номер:", (350, 290, 200, 30)),
            ("Кем выдан:", (850, 50, 200, 30)),
            ("Дата выдачи:", (850, 90, 200, 30)),
            ("ИНН:", (850, 130, 200, 30)),
            ("СНИЛС:", (850, 170, 200, 30)),
        )

        for text, geometry in textData:
            label = QLabel(text, self)
            label.setGeometry(*geometry)
            label.setFont(QFont("SansSerif", 15))
            label.setAlignment(Qt.AlignRight)

        # data in db
        labelsGeometrys = (
            (570, 50, 250, 30),
            (570, 90, 250, 30),
            (570, 130, 250, 30),
            (570, 170, 250, 30),
            (570, 210, 250, 30),
            (570, 250, 250, 30),
            (570, 290, 250, 30),
            (1070, 50, 250, 30),
            (1070, 90, 250, 30),
            (1070, 130, 250, 30),
            (1070, 170, 250, 30),
        )

        input_restriction = QRegExpValidator(QRegExp("[а-яА-Я]{3,}")) # surname, name, fam,
        date_restriction = QRegExpValidator(QRegExp("^(0[1-9]|[12][0-9]|3[01])\-(0[1-9]|1[012])\-\d{4}$"))
        passport_restriction = QRegExpValidator(QRegExp("^[0-9]{4}\ [0-9]{6}$"))
        inn_restriction = QRegExpValidator(QRegExp("^[0-9]{12}$"))
        snils_restriction = QRegExpValidator(QRegExp("^[0-9]{3}\-[0-9]{3}\-[0-9]{3}\ [0-9]{2}$"))

        self.labels = [QLineEdit("", self) for x in range(12)]
        for i, label in enumerate(self.labels[:11]):
            label.setGeometry(*labelsGeometrys[i])
            label.setFont(QFont("SansSerif", 15))
        self.labels[11].close()

        self.labels[0].setValidator(input_restriction)
        self.labels[0].editingFinished.connect(lambda: self.labels[0].setText(self.labels[0].text().title()))
        self.labels[1].setValidator(input_restriction)
        self.labels[1].editingFinished.connect(lambda: self.labels[1].setText(self.labels[1].text().title()))
        self.labels[2].setValidator(input_restriction)
        self.labels[2].editingFinished.connect(lambda: self.labels[2].setText(self.labels[2].text().title()))

        self.labels[3].setValidator(date_restriction)
        self.labels[3].mousePressEvent = lambda x: self.labels[3].setInputMask("00-00-0000")

        self.labels[6].setValidator(passport_restriction)
        self.labels[6].mousePressEvent = lambda x: self.labels[6].setInputMask("0000 000000")

        self.labels[8].setValidator(date_restriction)
        self.labels[8].mousePressEvent = lambda x: self.labels[8].setInputMask("00-00-0000")

        self.labels[9].setValidator(inn_restriction)
        self.labels[9].mousePressEvent = lambda x: self.labels[9].setInputMask("000000000000")

        self.labels[10].setValidator(snils_restriction)
        self.labels[10].mousePressEvent = lambda x: self.labels[10].setInputMask("000-000-000 00")

        self.photo_bd = QLabel(self)
        self.photo_bd.setGeometry(50, 50, 200, 250)
        self.enabled_false()

    def buttons(self):

        self.button_add = QPushButton("Добавить файл", self)
        self.button_add.setGeometry(900, 210, 150, 30)
        self.button_add.clicked.connect(self.click_add)

        self.button_edit = QPushButton("Редактировать", self)
        self.button_edit.setGeometry(900, 250, 150, 30)
        self.button_edit.clicked.connect(self.click_edit)

        label = QLabel("Сортировать по:", self)
        label.setGeometry(860, 360, 300, 30)
        label.setFont(QFont("SansSerif", 15))
        label.setAlignment(Qt.AlignLeft)

        self.button_sort_name = QPushButton("Имени", self)
        self.button_sort_name.setGeometry(1050, 360, 150, 30)
        self.button_sort_name.clicked.connect(self.click_button_sort_name)

        self.button_sort_updated = QPushButton("Изменению", self)
        self.button_sort_updated.setGeometry(1200, 360, 150, 30)
        self.button_sort_updated.setEnabled(False)
        self.button_sort_updated.clicked.connect(self.click_button_sort_updated)

        self.button_delete = QPushButton("Удалить", self)
        self.button_delete.setGeometry(900, 290, 150, 30)
        self.button_delete.setEnabled(False)
        self.button_delete.clicked.connect(self.click_delete_person)

        self.button_save = QPushButton("Сохранить", self)
        self.button_save.setGeometry(1120, 210, 150, 30)
        self.button_save.setEnabled(False)
        self.button_save.clicked.connect(self.click_save)

        self.button_load_records = QPushButton("Загрузить ещё", self)
        self.button_load_records.setGeometry(49, 360, 150, 30)
        self.button_load_records.clicked.connect(self.click_edit_records)

        self.button_edit_photo = QPushButton("Изменить фото", self)
        self.button_edit_photo.setGeometry(100, 310, 120, 30)
        self.button_edit_photo.clicked.connect(self.click_button_edit_photo)

    def click_button_sort_name(self):
        self.button_sort_name.setEnabled(False)
        self.button_sort_updated.setEnabled(True)
        self.change_sorting_type(SortType.ByName)

    def click_button_sort_updated(self):
        self.button_sort_updated.setEnabled(False)
        self.button_sort_name.setEnabled(True)
        self.change_sorting_type(SortType.ByUpdated)

    def click_button_edit_photo(self):
        add_photo_for_edit = QFileDialog.getOpenFileNames(
            self,
            'Open File',
            'Users/',
            'JPG File(*.jpg);;JPEG File(*.jpeg);;PNG File(*.png)'
        )[0]
        self.new_photo_path = ''.join(add_photo_for_edit)
        self.photo_bd.setPixmap(QPixmap(self.new_photo_path).scaled(200, 250))

    def click_add(self):
        self.windows_manager.show_window(WindowsManager.WindowsNames.EditPersonWindow)

    def click_save(self):
        if self.new_photo_path:
            file_manager.save_file(self.new_photo_path, self.row_to_base_id[self.index_row], "photo.jpg")
        self.database.update_person([x.text() for x in self.labels[:-1]], self.row_to_base_id[self.index_row])
        if self.sorting_type == SortType.ByUpdated:
            if self.index_row != 0:
                self.tableWidget.removeRow(self.index_row)
                self.tableWidget.insertRow(0)
            self.row_to_base_id.insert(0, self.row_to_base_id.pop(self.index_row))
            for i in range(11):
                self.tableWidget.setItem(0, i, QTableWidgetItem(self.labels[i].text()))
        else:
            for i in range(11):
                self.tableWidget.setItem(self.index_row, i, QTableWidgetItem(self.labels[i].text()))

        self.index_row = -1
        self.clear_labels()

    def clear_labels(self):
        self.button_save.setEnabled(False)
        self.button_delete.setEnabled(False)
        self.button_edit.setEnabled(False)

        self.labels[3].setInputMask("")
        self.labels[6].setInputMask("")
        self.labels[8].setInputMask("")
        self.labels[9].setInputMask("")
        self.labels[10].setInputMask("")
        for label in self.labels:
            label.clear()
        self.enabled_false()

    def click_edit(self):
        for label in self.labels[:11]:
            label.setEnabled(True)

        self.button_save.setEnabled(True)
        self.button_edit_photo.setEnabled(True)

    def click_delete_person(self):
        self.msg_delete = QMessageBox()
        self.msg_delete.setWindowTitle("Удаление")
        self.msg_delete.setIcon(QMessageBox.Question)
        self.msg_delete.setText("Вы действительно хотите удалить пользователя?")
        self.msg_delete.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        res = self.msg_delete.exec_()

        if res == QMessageBox.Yes:
            self.database.delete_person(self.row_to_base_id[self.index_row])
            file_manager.delete_person_data(self.row_to_base_id[self.index_row])
            self.tableWidget.removeRow(self.index_row)
            self.index_row = -1
            for i in range(self.index_row, len(self.row_to_base_id) - 1):
                self.row_to_base_id[i] = self.row_to_base_id[i + 1]
            self.row_to_base_id.pop()
            self.enabled_false()
            self.button_delete.setEnabled(False)
            self.button_save.setEnabled(False)
            self.button_edit.setEnabled(False)
            for line in self.labels:
                line.setText('')
        if res == QMessageBox.Cancel:
            pass

    def click_edit_records(self):
        self.load_data()

    def change_sorting_type(self, new_type=SortType.ByUpdated):
        if self.sorting_type == new_type:
            return
        self.sorting_type = new_type
        self.clear_labels()
        self.load_data(reset_data=True)

    def eventFilter(self, source, event):
        if event.type() == QtCore.QEvent.MouseButtonPress:
            if event.button() == QtCore.Qt.LeftButton:
                index = self.tableWidget.indexAt(event.pos())
                if index.row() < 0:
                    return super(MainWindow, self).eventFilter(source, event)
                self.index_row = index.row()
                self.new_photo_path = ''
                # parsing table
                for i in range(11):
                    self.labels[i].setText(self.tableWidget.item(self.index_row, i).text())
                self.photo_bd.setPixmap(
                    QPixmap(
                        file_manager.get_file_path(
                            self.row_to_base_id[self.index_row],
                            "photo.jpg",
                        ),
                    ).scaled(200, 250))

                if index.data():
                    self.button_edit.setEnabled(True)
                    self.button_delete.setEnabled(True)
                elif not index.data():
                    self.button_edit.setEnabled(False)
                    self.button_delete.setEnabled(False)

        return super(MainWindow, self).eventFilter(source, event)

    def create_table(self):
        self.tableWidget = QTableWidget(self)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(11)
        self.tableWidget.setGeometry(50, 400, 1300, 350)
        self.tableWidget.setFixedSize(1300, 350)
        
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.tableWidget.viewport().installEventFilter(self)

        headers = (
            "Фамилия", "Имя", "Отчество", "Дата Рождения",
            "Место Рождения", "Место регистрации", "Серия и Номер",
            "Кем выдан", "Дата выдачи", "ИНН", "СНИЛС"
        )
        for i, header in enumerate(headers):
            self.tableWidget.setHorizontalHeaderItem(i, QTableWidgetItem(header))
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)
        column = (
            (0, 100),
            (1, 100),
            (2, 120),
            (9, 120),
            (10, 120)
        )
        for i, col in column:
            self.tableWidget.setColumnWidth(i, col)

    def load_data(self, reset_data=False):
        if reset_data:
            self.loaded = 0
            self.tableWidget.setRowCount(0)
            self.row_to_base_id = []
        result = self.database.get_persons(self.loaded, self.limit, self.sorting_type)
        for row_number, row_data in enumerate(result.fetchall()):
            if row_data[0] in self.row_to_base_id:
                continue
            else:
                self.row_to_base_id.append(row_data[0])
            self.tableWidget.insertRow(self.tableWidget.rowCount())
            self.loaded += 1
            for column_number, data in enumerate(row_data[1:12]):
                self.tableWidget.setItem(
                    self.tableWidget.rowCount() - 1,
                    column_number,
                    QTableWidgetItem(str(data))
                )

    def add_new_person(self, person_data):
        self.tableWidget.insertRow(0)
        self.row_to_base_id.insert(0, person_data[0])
        for column_number, data in enumerate(person_data[1:]):
            self.tableWidget.setItem(0, column_number, QTableWidgetItem(str(data)))

    def enabled_false(self):
        for label in self.labels[:11]:
            label.setEnabled(False)
        self.photo_bd.clear()
        self.button_edit_photo.setEnabled(False)

