import unittest
from todo_list import TodoList

class TestTodoList(unittest.TestCase):
    def setUp(self):
        self.todo_list = TodoList()
    
    def test_add_task(self):
        self.todo_list.add_task("Buy groceries")
        self.assertIn("Buy groceries", self.todo_list.list_tasks())
    
    def test_remove_task(self):
        self.todo_list.add_task("Walk the dog")
        self.todo_list.remove_task("Walk the dog")
        self.assertNotIn("Walk the dog", self.todo_list.list_tasks())
    
    def test_list_tasks(self):
        self.todo_list.add_task("Read a book")
        self.todo_list.add_task("Write code")
        tasks = self.todo_list.list_tasks()
        self.assertIn("Read a book", tasks)
        self.assertIn("Write code", tasks)
        self.assertEqual(len(tasks), 2)

if __name__ == '__main__':
    unittest.main()

