import DbAccessTestBase
import UserDao

class UserDaoTest(DbAccessTestBase.DbAccessTestBase):

    @classmethod
    def setUpClass(cls):
        super(UserDaoTest, cls).setUpClass()
        cls.userDao = UserDao.UserDao(cls.connection)

    def setUp(self):
        self.recreateUsers()

    def testEmpty(self):
        actual = self.userDao.get(1)
        self.assertEqual(len(actual), 0)

    def testGet(self):
        self.insertUsers([[1, 'tom', 31], [2, 'John', 25]])
        actual = self.userDao.get('tom')
        self.assertEqual(actual[0]['age'], 31)

