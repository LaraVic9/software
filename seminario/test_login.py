import unittest
from login import login
from config import create_users_table, insert_user, user_exists

class TestLogin(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        create_users_table()
        insert_user('admin', '123456')

    def test_valid_credentials(self):
        username = 'admin'
        password = '123456'
        self.assertTrue(login(username, password))

    def test_invalid_credentials(self):
        username = 'admin'
        password = 'senhaerrada'
        self.assertFalse(login(username, password))

    # nao funcionano
    def test_empty_username(self):
        username = ''
        password = '123456'
        self.assertFalse(login(username, password))

    def test_empty_password(self):
        username = 'admin'
        password = ''
        self.assertFalse(login(username, password))

    def test_user_exists(self):
        self.assertTrue(user_exists('admin'))
        self.assertFalse(user_exists('não_existe'))

if __name__ == '__main__':
    unittest.main()
