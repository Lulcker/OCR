import sqlite3
import uuid


class DataBaseCluster:

    def __init__(self, path_to_database):
        self.database = sqlite3.connect(path_to_database)
        self.request = self.database.cursor()
        self.init_table()

    def init_table(self):
        self.request.execute(
            """
            CREATE TABLE IF NOT EXISTS persons(
                id TEXT PRIMARY KEY,
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
                updated DATETIME DEFAULT CURRENT_TIMESTAMP
            );
            """
        )
        self.database.commit()

    def insert_person(self, person_data):
        id = str(uuid.uuid4())

        self.request.execute(
            """
                INSERT INTO persons(
                    id,
                    surname, 
                    name_, 
                    patronymic, 
                    date_of_birth, 
                    place_of_birth, 
                    place_of_registration, 
                    series_and_number, 
                    issued_by_whom, 
                    date_of_issue, 
                    inn, 
                    snils
                ) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
            """,
            [id] + person_data,
        )
        self.database.commit()
        return id

    def get_persons(self, time, limit):
        return self.request.execute(
            """
                SELECT 
                    * 
                FROM persons 
                WHERE updated < ?
                ORDER BY updated DESC
                LIMIT ?;
            """,
            [time, limit]
        )

    def sorted_surname_asc(self):
        qq = self.request.execute(
            """
                SELECT * 
                  FROM persons
                 ORDER BY surname ASC;
            """
        )
        self.database.commit()
        return qq

    def sorted_surname_desc(self):
        qq = self.request.execute(
            """
                SELECT * 
                  FROM persons
                 ORDER BY surname DESC;
            """
        )
        self.database.commit()
        return qq

    def delete_person(self, id):
        self.request.execute("""DELETE FROM persons WHERE id == ?;""", [id])
        self.database.commit()

    def update_person(self, mass, id):
        self.request.execute(
            """
                UPDATE persons 
                    SET 
                        surname = ?, 
                        name_ = ?, 
                        patronymic = ?, 
                        date_of_birth = ?, 
                        place_of_birth = ?, 
                        place_of_registration = ?, 
                        series_and_number = ?, 
                        issued_by_whom = ?, 
                        date_of_issue = ?, 
                        inn = ?,
                        snils = ?,
                        updated = CURRENT_TIMESTAMP
                    WHERE id = ?
            """,
            mass + [id],
        )
        self.database.commit()










