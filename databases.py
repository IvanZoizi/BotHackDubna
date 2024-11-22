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

    def get_policy(self, user_id):
        return self.cur.execute("""SELECT * FROM user_policy WHERE user_id = ?""", (user_id,)).fetchone()

    def new_policy(self, user_id, code, name):
        self.cur.execute("""INSERT INTO user_policy VALUES(?, ?, ?)""", (user_id, code, name))
        self.con.commit()

    def get_communal_services(self, user_id):
        return self.cur.execute("""SELECT * FROM user_communal_services WHERE user_id = ?""", (user_id,)).fetchone()

    def new_communal_services(self, user_id):
        if not self.get_communal_services(user_id):
            self.cur.execute("""INSERT INTO user_communal_services(user_id) VALUES(?)""", (user_id,))
            self.con.commit()

    def edit_communal_services(self, user_id, column, data):
        self.cur.execute(f"""UPDATE user_communal_services SET {column} = ? WHERE user_id = ?""", (data, user_id))
        self.con.commit()