import DbAccessTestBase
import UserDaoPlain
import sys
import StringIO


class UserDaoTest(DbAccessTestBase.DbAccessTestBase):
    @classmethod
    def setUpClass(cls):
        super(UserDaoTest, cls).setUpClass()

    def setUp(self):
        self.recreateUsers()
        self.capture = StringIO.StringIO()
        sys.stdout = self.capture

    def tearDown(self):
        sys.stdout = sys.__stdout__

    def testEmpty(self):
        UserDaoPlain.user_dao_plain('./config/test.ini')

    def testGet(self):
        self.insertUsers([[1, 'tom', 31], [2, 'John', 25]])
        UserDaoPlain.user_dao_plain('./config/test.ini')
        self.assertEqual('', self.capture.getvalue())
