class UserDao:

    def __init__(self, connection):
        self.connection = connection

    def get(self, name):
        with self.connection.cursor() as cursor:
            sql = "SELECT id, name, age FROM users where name = %s"
            cursor.execute(sql, name)

            result = cursor.fetchall()
            ret = []
            for r in result:
                ret.append(r)

            return ret
