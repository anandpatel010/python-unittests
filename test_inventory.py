import unittest
from inventory import Inventory

class TestInventory(unittest.TestCase):
    def setUp(self):
        self.inventory = Inventory()
    
    def test_add_item(self):
        self.inventory.add_item("apple", 10)
        self.inventory.add_item("banana", 5)
        self.assertEqual(self.inventory.get_inventory()["apple"], 10)
        self.assertEqual(self.inventory.get_inventory()["banana"], 5)
    
    def test_remove_item(self):
        self.inventory.add_item("apple", 10)
        result = self.inventory.remove_item("apple", 5)
        self.assertTrue(result)
        self.assertEqual(self.inventory.get_inventory()["apple"], 5)

        result = self.inventory.remove_item("apple", 10)
        self.assertFalse(result)  # Not enough apples to remove
    
    def test_remove_nonexistent_item(self):
        result = self.inventory.remove_item("orange", 1)
        self.assertFalse(result)  # Cannot remove an item that doesn't exist
    
    def test_get_inventory(self):
        self.inventory.add_item("apple", 10)
        self.inventory.add_item("banana", 5)
        inventory = self.inventory.get_inventory()
        self.assertEqual(inventory, {"apple": 10, "banana": 5})

if __name__ == '__main__':
    unittest.main()
