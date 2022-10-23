import sqlite3


class DataBaseCluster:

    def __init__(self, path_to_database):
        self.database = sqlite3.connect(path_to_database)
        self.request = self.database.cursor()
        self.init_table()

    def init_table(self):
        self.request.execute("""CREATE TABLE IF NOT EXISTS persons(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            surname TEXT NOT NULL,
            name_ TEXT,
            patronymic TEXT,
            date_of_birth TEXT,
            place_of_birth TEXT,
            place_of_registration TEXT,
            series_and_number TEXT,
            issued_by_whom TEXT,
            date_of_issue TEXT,
            inn INTEGER,
            snils TEXT, 
            photo TEXT);""")
        self.database.commit()

        '''surname = "Nikolay"
        name_ = "Venediktov"
        patronymic = "Aleksandrovich"
        date_of_birth = "14.02.2004"
        place_of_birth = "г.Москва"
        place_of_registration = "Moskow"
        series_and_number = "4518 522287"
        issued_by_whom = "Gu MVD"
        date_of_issue = "27.02.2018"
        inn = 7676767
        snils = "37737-774"
        photo = "hfhfh"
        person_data = (surname, name_, patronymic, date_of_birth, place_of_birth, place_of_registration, series_and_number, issued_by_whom, date_of_issue, inn, snils, photo)

        self.insert_person(person_data)'''

    def insert_person(self, person_data):
        self.request.execute("""INSERT INTO persons(surname, name_, patronymic, date_of_birth, place_of_birth, place_of_registration, series_and_number, issued_by_whom, date_of_issue, inn, snils, photo) 
                                     VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);""", person_data)
        self.database.commit()

    def get_persons(self):
        return self.request.execute("SELECT * FROM persons;")

    def delete_person(self, id):
        self.request.execute("""DELETE FROM persons WHERE id ==?;""", [id])
        self.database.commit()









