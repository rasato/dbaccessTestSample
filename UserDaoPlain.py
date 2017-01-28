import pymysql.cursors

connection = pymysql.connect(host='localhost',
                             port=13306,
                             user='userfoo',
                             password='secret',
                             db='mydb',
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)

with connection.cursor() as cursor:
    print('start script')
    sql = "SELECT id, name, age FROM users"
    cursor.execute(sql)

    result = cursor.fetchall()
    for r in result:
        print(r)


connection.close()
