import unittest
from authenticator import Authenticator

class TestAuthenticator(unittest.TestCase):
    def setUp(self):
        self.auth = Authenticator()
        self.auth.register("user1", "password123")
    
    def test_register(self):
        result = self.auth.register("user2", "mypassword")
        self.assertTrue(result)
        result = self.auth.register("user1", "newpassword")
        self.assertFalse(result)  # Username already taken
    
    def test_login(self):
        result = self.auth.login("user1", "password123")
        self.assertTrue(result)
        result = self.auth.login("user1", "wrongpassword")
        self.assertFalse(result)
        result = self.auth.login("nonexistent", "password")
        self.assertFalse(result)
    
    def test_change_password(self):
        result = self.auth.change_password("user1", "password123", "newpassword")
        self.assertTrue(result)
        result = self.auth.login("user1", "newpassword")
        self.assertTrue(result)
        result = self.auth.change_password("user1", "wrongpassword", "anotherpassword")
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()

