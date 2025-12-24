import model
import unittest


class TestTaskLogic(unittest.TestCase):
    def test_add_task(self):
        tasks = {}
        result = model.add_task(tasks, "Test Task")
        self.assertEqual(result[1], "Test Task")

    def test_delete_and_reindex(self):
        tasks = {1: "Stay", 2: "Delete Me"}
        result = model.delete_task(tasks, 2)
        self.assertEqual(len(result), 1)
        self.assertNotIn(2, result)

    def test_delete_non_existent(self):
        tasks = {1: "Task A"}
        result = model.delete_task(tasks, 99)  # 99 doesn't exist
        self.assertEqual(len(result), 1)  # Should still have 1 task

if __name__ == "__main__":
    unittest.main()
