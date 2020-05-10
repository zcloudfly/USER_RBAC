from pymysql import *


class MysqlHelper:
    def __init__(self, host='localhost', port=3306, db='rbac', user='root', passwd='123456', charset='utf8'):
        self.host = host
        self.port = port
        self.db = db
        self.user = user
        self.passwd = passwd
        self.charset = charset

    def open(self):
        self.conn = connect(host=self.host,
                            port=self.port,
                            user=self.user,
                            passwd=self.passwd,
                            db=self.db,
                            charset=self.charset)
        self.cursor = self.conn.cursor()

    def close(self):
        self.cursor.close()
        self.conn.close()

    def cud(self, sql, params):
        try:
            self.open()

            self.cursor.execute(sql, params)

            self.conn.commit()

            self.close()
        except Exception as e:
            print(e)

    def all(self, sql, params=[]):
        try:
            self.open()

            self.cursor.execute(sql, params)

            result = self.cursor.fetchall()

            self.close()

            return result

        except Exception as e:
            print(e)
