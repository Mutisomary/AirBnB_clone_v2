import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand

class TestHBNBCommandMethods(unittest.TestCase):

    def setUp(self):
        self.cmd = HBNBCommand()
        self.patcher = patch('sys.stdout', new_callable=StringIO)
        self.mock_stdout = self.patcher.start()

    def tearDown(self):
        self.patcher.stop()

    def test_do_quit(self):
        with self.assertRaises(SystemExit):
            self.cmd.do_quit("")

    def test_do_EOF(self):
        with self.assertRaises(SystemExit):
            self.cmd.do_EOF("")

    def test_do_create(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.cmd.do_create("User name='John' age=30")
            output = mock_stdout.getvalue().strip()
            self.assertTrue(output.startswith("b"))

    def test_do_show(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.cmd.do_show("User 123")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    def test_do_destroy(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.cmd.do_destroy("User 123")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    def test_do_all(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.cmd.do_all("User")
            output = mock_stdout.getvalue().strip()
            self.assertTrue(output.startswith("["))

    def test_do_count(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.cmd.do_count("User")
            output = mock_stdout.getvalue().strip()
            self.assertTrue(output.isdigit())

    def test_do_update(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.cmd.do_update("User 123 name 'Alice'")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

if __name__ == '__main__':
    unittest.main()
