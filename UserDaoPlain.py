import pymysql.cursors
import sys
import ConfigParser


def user_dao_plain(configPath):
    inifile = ConfigParser.SafeConfigParser()
    inifile.read(configPath)

    connection = pymysql.connect(host=inifile.get('connection', 'host'),
                                 port=inifile.getint('connection', 'port'),
                                 user=inifile.get('connection', 'user'),
                                 password=inifile.get('connection', 'password'),
                                 db='mydb',
                                 charset='utf8',
                                 cursorclass=pymysql.cursors.DictCursor)

    with connection.cursor() as cursor:
        print('start script')
        sql = "SELECT id, name, age FROM users"
        cursor.execute(sql)

        result = cursor.fetchall()
        print(result)

    connection.close()


if __name__ == '__main__':
    user_dao_plain('./config/local.ini')
