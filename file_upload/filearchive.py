import mysql.connector
from mysql.connector import errorcode

class FileArchive:

    def __init__(self) -> None:

        dbconfig = {'host': '127.0.0.1',
                    'user': 'user',
                    'password': 'test',
                    'database': 'myDb', }

        self.configuration = dbconfig

    def __enter__(self) -> 'cursor':
        self.conn = mysql.connector.connect(**self.configuration)
        self.cursor = self.conn.cursor(buffered=True)
        return self

    def __exit__(self, exc_type, exc_val, exc_trace) -> None:
        self.conn.commit()
        self.cursor.close()
        self.conn.close()

    def query(self, sql):
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result

    def getAll(self):
        try:
            self.cursor.execute("SELECT * FROM attachment")
            result = self.cursor.fetchall()
        except mysql.connector.Error as err:
                print(err)
        return result

    def get(self, id):
        try:
            self.cursor.execute("SELECT * FROM attachment WHERE  id=(%s)", (id,))
            result = self.cursor.fetchone()
        except mysql.connector.Error as err:
                print(err)
        return result

    def delete(self, id):
        try:
            self.cursor.execute("DELETE FROM attachment WHERE  id=(%s)", (id,))
        except mysql.connector.Error as err:
                print(err)

    def add(self, attachment):
        try:
            sql = '''INSERT
            INTO
                attachment(id, size, date, mimetype, filename, code)
            VALUES
                (NULL, %s, %s, %s, %s, %s)'''
            self.cursor.execute(sql, attachment)
        except mysql.connector.Error as err:
                print(err)
