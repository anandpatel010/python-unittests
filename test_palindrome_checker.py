import unittest
from palindrome_checker import PalindromeChecker

class TestPalindromeChecker(unittest.TestCase):
    def setUp(self):
        self.checker = PalindromeChecker()
    
    def test_palindrome(self):
        self.assertTrue(self.checker.is_palindrome("A man, a plan, a canal, Panama"))
        self.assertTrue(self.checker.is_palindrome("racecar"))
        self.assertTrue(self.checker.is_palindrome("12321"))
    
    def test_non_palindrome(self):
        self.assertFalse(self.checker.is_palindrome("hello"))
        self.assertFalse(self.checker.is_palindrome("world"))
        self.assertFalse(self.checker.is_palindrome("Python"))
    
    def test_empty_string(self):
        self.assertTrue(self.checker.is_palindrome(""))
    
    def test_single_character(self):
        self.assertTrue(self.checker.is_palindrome("a"))
        self.assertTrue(self.checker.is_palindrome("1"))

if __name__ == '__main__':
    unittest.main()
