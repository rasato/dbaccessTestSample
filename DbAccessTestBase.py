import unittest
import pymysql.cursors
import UserDao

class DbAccessTestBase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.connection = pymysql.connect(host='localhost',
                                         port=13306,
                                         user='userfoo',
                                         password='secret',
                                         db='mydb',
                                         charset='utf8',
                                         cursorclass=pymysql.cursors.DictCursor)

    @classmethod
    def tearDownClass(cls):
        cls.connection.close()

    def recreateUsers(self):
        with self.connection.cursor() as cursor:
            recreate = "drop table if exists users;"
            recreate += "create table users (id INTEGER, name VARCHAR(20), age SMALLINT);"
            cursor.execute(recreate)

    def insertUsers(self, params):
        if len(params) == 0:
            return
        with self.connection.cursor() as cursor:
            insert = "insert into users (id, name, age) values (%s, %s, %s)"
            for param in params:
                cursor.execute(insert, param)
            self.connection.commit()
