import sqlite3


class ConnectionDBController():
    validN2 = True

    @staticmethod
    def getConnection():
        try:
            cnxn = sqlite3.connect("database.db")
            return cnxn
        except Exception as ex:
            raise ex

    @staticmethod
    def dict_factory(cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d
        