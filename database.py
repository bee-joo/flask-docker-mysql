import mysql.connector


class Database:
    def __init__(self, host: str, user: str, password: str, db: str):
        self.__host = host
        self.__user = user
        self.__password = password
        self.__db = db
        self._conn = None


    def initdb(self):
        mydb = mysql.connector.connect(host=self.__host,
                                       user=self.__user,
                                       password=self.__password)
        cursor = mydb.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {self.__db}")
        cursor.close()

        self._conn = mysql.connector.connect(host=self.__host,
                                       user=self.__user,
                                       password=self.__password,
                                       database=self.__db)
        cursor = self._conn.cursor()
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS widgets (name VARCHAR(255), description VARCHAR(255))"
        )
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS logs (datetime VARCHAR(255), client_info VARCHAR(255))"
        )
        cursor.close()


    def find_all_as_dict(self, table: str) -> list:
        cursor = self._conn.cursor()
        cursor.execute(f"SELECT * FROM {table}")
        
        row_headers = [i[0] for i in cursor.description]
        data = cursor.fetchall()
        result = []

        for row in data:
            result.append(dict(zip(row_headers, row)))

        cursor.close()
        return result


    def add(self, table: str, value1, value2) -> int:
        cursor = self._conn.cursor()
        try:
            cursor.execute(f"INSERT INTO {table} VALUES ('{value1}', '{value2}')")
            self._conn.commit()
        except Exception as e:
            print(e)
        finally:
            res = cursor.rowcount
            cursor.close()
            return res
