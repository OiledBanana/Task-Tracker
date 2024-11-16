import unittest
from unittest.mock import patch, mock_open
import json
import datetime
from task import TaskManager

class TestTaskManager(unittest.TestCase):

    def setUp(self):
        # Sample tasks to use in tests
        self.sample_tasks = [
            {"id": 1, "description": "Buy groceries", "status": "todo", "createdAt": "2024-11-10T12:00:00", "updatedAt": "2024-11-10T12:30:00"},
            {"id": 2, "description": "Clean the house", "status": "in-progress", "createdAt": "2024-11-10T13:00:00", "updatedAt": "2024-11-10T13:30:00"}
        ]

    @patch('task_manager.os.path.exists', return_value=True)
    @patch('task_manager.open', new_callable=mock_open, read_data=json.dumps([]))
    def test_load_tasks_empty(self, mock_file, mock_exists):
        tasks = TaskManager.load_tasks()
        self.assertEqual(tasks, [])
        mock_file.assert_called_once_with("tasks.json", "r")

    @patch('task_manager.os.path.exists', return_value=True)
    @patch('task_manager.open', new_callable=mock_open, read_data=json.dumps(self.sample_tasks))
    def test_load_tasks_with_data(self, mock_file, mock_exists):
        tasks = TaskManager.load_tasks()
        self.assertEqual(tasks, self.sample_tasks)
        mock_file.assert_called_once_with("tasks.json", "r")

    @patch('task_manager.open', new_callable=mock_open)
    def test_save_task(self, mock_file):
        TaskManager.save_task(self.sample_tasks)
        mock_file.assert_called_once_with("tasks.json", "w")
        mock_file().write.assert_called_once_with(json.dumps(self.sample_tasks, indent=4))

    @patch('task_manager.TaskManager.load_tasks', return_value=[])
    @patch('task_manager.TaskManager.save_task')
    def test_add_task(self, mock_save, mock_load):
        description = "Write a report"
        with patch('task_manager.datetime.datetime') as mock_datetime:
            mock_datetime.now.return_value = datetime.datetime(2024, 11, 10, 14, 0, 0)
            TaskManager.add_task(description)
        mock_save.assert_called_once()
        added_task = mock_save.call_args[0][0][0]
        self.assertEqual(added_task["description"], description)
        self.assertEqual(added_task["status"], "todo")
        self.assertEqual(added_task["createdAt"], "2024-11-10T14:00:00")

    @patch('task_manager.TaskManager.load_tasks', return_value=self.sample_tasks)
    @patch('task_manager.TaskManager.save_task')
    def test_update_task(self, mock_save, mock_load):
        task_id = 1
        new_description = "Buy groceries and cook dinner"
        TaskManager.update_task(task_id, new_description)
        mock_save.assert_called_once()
        updated_task = mock_save.call_args[0][0][0]
        self.assertEqual(updated_task["description"], new_description)

    @patch('task_manager.TaskManager.load_tasks', return_value=self.sample_tasks)
    @patch('task_manager.TaskManager.save_task')
    def test_delete_task(self, mock_save, mock_load):
        task_id = 1
        TaskManager.delete_task(task_id)
        mock_save.assert_called_once()
        saved_tasks = mock_save.call_args[0][0]
        self.assertEqual(len(saved_tasks), 1)
        self.assertNotIn({"id": 1, "description": "Buy groceries", "status": "todo"}, saved_tasks)

    @patch('task_manager.TaskManager.load_tasks', return_value=self.sample_tasks)
    def test_list_tasks(self, mock_load):
        with patch('builtins.print') as mock_print:
            TaskManager.list_tasks()
        mock_print.assert_called()
        self.assertEqual(len(mock_print.mock_calls), len(self.sample_tasks))

    @patch('task_manager.TaskManager.load_tasks', return_value=self.sample_tasks)
    @patch('task_manager.TaskManager.save_task')
    def test_mark_task(self, mock_save, mock_load):
        task_id = 1
        status = "done"
        TaskManager.mark_task(task_id, status)
        mock_save.assert_called_once()
        marked_task = mock_save.call_args[0][0][0]
        self.assertEqual(marked_task["status"], status)

if __name__ == "__main__":
    unittest.main()
