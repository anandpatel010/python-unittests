import unittest
from bank_account import BankAccount

class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount()
    
    def test_deposit(self):
        self.account.deposit(100.0)
        self.assertEqual(self.account.get_balance(), 100.0)
    
    def test_withdraw(self):
        self.account.deposit(200.0)
        self.account.withdraw(50.0)
        self.assertEqual(self.account.get_balance(), 150.0)
    
    def test_withdraw_insufficient_funds(self):
        self.account.deposit(100.0)
        with self.assertRaises(ValueError):
            self.account.withdraw(150.0)
    
    def test_get_balance(self):
        self.account.deposit(250.0)
        self.assertEqual(self.account.get_balance(), 250.0)
        self.account.withdraw(100.0)
        self.assertEqual(self.account.get_balance(), 150.0)

if __name__ == '__main__':
    unittest.main()

