from src.models.user import UserModel
from tests.base_test import BaseTest

class UserTest(BaseTest):
    def test_create_user(self):
        user = UserModel('test_username', 'A12345678')

        self.assertEqual(user.username, 'test_username',
                         "The name of the user after creation does not equal the constructor argument.")
        self.assertEqual(user.password, 'A12345678',
                         "The password of the user after creation does not equal the constructor argument.")
