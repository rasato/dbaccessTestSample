import DbAccessTestBase
import UserDaoPlain

class UserDaoTest(DbAccessTestBase.DbAccessTestBase):

    @classmethod
    def setUpClass(cls):
        super(UserDaoTest, cls).setUpClass()

    def setUp(self):
        self.recreateUsers()

    def testEmpty(self):
        UserDaoPlain

    def testGet(self):
        self.insertUsers([[1, 'tom', 31], [2, 'John', 25]])
        UserDaoPlain

