import sqlite3


class DataBase:
    def __init__(self, path):
        self.con = sqlite3.connect(path)
        self.cur = self.con.cursor()

    def get_educational_user(self, name, surname):
        return self.cur.execute("""SELECT * FROM user_education WHERE name = ? AND surname = ?""", (name, surname))

    def new_educational_user(self, user_id, name, surname, fatherhood, year, type):
        self.cur.execute("""INSERT INTO user_education VALUES(?, ?, ?, ?, ?, ?)""",
                         (user_id, name, surname, fatherhood, year, type))
        self.con.commit()

    def get_educational_user_data(self, user_id):
        return self.cur.execute("""SELECT * FROM user_education WHERE user_id = ?""", (user_id,)).fetchall()