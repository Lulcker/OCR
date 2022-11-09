from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from PyQt5 import QtCore

from Windows import WindowsManager


class MainWindow(QMainWindow):
    def __init__(self, database, windows_manager):
        super(MainWindow, self).__init__()
        self.windows_manager = windows_manager
        self.database = database

        self.row_to_base_id = list()
        self.last_time_loaded = '2999-01-01 00:00:00'
        self.limit = 10
        self.index_row = -1

        self.screen_()
        self.buttons()
        self.write_text_element()
        self.create_table()
        self.load_data()

    def screen_(self):
        self.setWindowTitle("Scanner")
        self.setFixedSize(QSize(1400, 800))

    def write_text_element(self):

        # displaying the text of the surname, name...
        textData = (
            ("Фамилия:", (350, 50, 200, 30)),
            ("Имя:", (350, 90, 200, 30)),
            ("Отчество:", (350, 130, 200, 30)),
            ("Дата рождения:", (350, 170, 200, 30)),
            ("Место рождения:", (350, 210, 200, 30)),
            ("Место регистрации:", (300, 250, 250, 30)),
            ("Кем выдан:", (350, 290, 200, 30)),
            ("Дата выдачи:", (850, 50, 200, 30)),
            ("Серия и номер:", (850, 90, 200, 30)),
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

        self.labels = [QLineEdit("", self) for x in range(12)]
        for i, label in enumerate(self.labels[:11]):
            label.setGeometry(*labelsGeometrys[i])
            label.setFont(QFont("SansSerif", 15))
        self.labels[11].close()

        self.photo_bd = QLabel(self)
        self.photo_bd.setGeometry(50, 50, 200, 250)
        self.enabled_false()

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

    def click_button_edit_photo(self):
        add_photo_for_edit = QFileDialog.getOpenFileNames(
            self,
            'Open File',
            'Users/',
            'JPG File(*.jpg);;JPEG File(*.jpeg);;PNG File(*.png)'
        )[0]
        photo_path = ''.join(add_photo_for_edit)
        self.labels[11].setText(''.join(add_photo_for_edit))
        self.photo_bd.setPixmap(QPixmap(photo_path).scaled(200, 250))

    def click_add(self):
        self.windows_manager.show_window(WindowsManager.WindowsNames.EditPersonWindow)

    def click_save(self):
        self.database.update_person([x.text() for x in self.labels], self.row_to_base_id[self.index_row])
        for i in range(12):
            self.tableWidget.item(self.index_row, i).setText(self.labels[i].text())
        self.button_save.setEnabled(False)
        self.button_delete.setEnabled(False)
        self.button_edit.setEnabled(False)
        [x.clear() for x in self.labels]
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
            self.tableWidget.removeRow(self.index_row)
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

    def eventFilter(self, source, event):
        if event.type() == QtCore.QEvent.MouseButtonPress:
            if event.button() == QtCore.Qt.LeftButton:
                index = self.tableWidget.indexAt(event.pos())
                self.index_row = index.row()
                if self.index_row < 0:
                    return super(MainWindow, self).eventFilter(source, event)
                # parsing table
                for i in range(12):
                    self.labels[i].setText(self.tableWidget.item(self.index_row, i).text())
                self.photo = self.labels[11].text()
                self.photo_bd.setPixmap(QPixmap(self.photo).scaled(200, 250))

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
        self.tableWidget.setColumnCount(12)
        self.tableWidget.setGeometry(50, 400, 1300, 350)
        self.tableWidget.setFixedSize(1300, 350)
        
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)

        self.tableWidget.viewport().installEventFilter(self)

        headers = (
            "Фамилия", "Имя", "Отчество", "Дата Рождения",
            "Место Рождения", "Место регистрации", "Серия и Номер",
            "Кем выдан", "Дата выдачи", "ИНН", "СНИЛС", "ФОТО"
        )
        for i, header in enumerate(headers):
            self.tableWidget.setHorizontalHeaderItem(i, QTableWidgetItem(header))

    def load_data(self):
        result = self.database.get_persons(self.last_time_loaded, self.limit)
        if self.last_time_loaded == '2999-01-01 00:00:00':
            self.tableWidget.setRowCount(0)
            self.row_to_base_id = []
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(self.tableWidget.rowCount())
            self.row_to_base_id.append(row_data[0])
            self.last_time_loaded = row_data[13]
            for column_number, data in enumerate(row_data[1:13]):
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

