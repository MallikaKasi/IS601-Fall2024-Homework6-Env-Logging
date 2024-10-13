'''Testing Commands '''

import unittest
from unittest.mock import MagicMock, patch
from app.commands import CommandHandler, Command

# A mock command to simulate the behavior of a real command class
class MockCommand(Command):
    '''Testing Operations '''

    def __init__(self, *args):
        self.args = args

    def execute(self):
        print("Command executed with arguments:", self.args)

# Test cases for the CommandHandler class
class TestCommandHandler(unittest.TestCase):
    '''Testing Operations '''

    def setUp(self):
        # Initialize a CommandHandler before each test
        self.command_handler = CommandHandler()

    def test_register_command(self):
        '''Testing Operations '''
        # Create a mock command instance and register it
        mock_command = MockCommand()
        self.command_handler.register_command("test_command", mock_command)

        # Verify that the command was registered
        self.assertIn("test_command", self.command_handler.commands)
        self.assertIs(self.command_handler.commands["test_command"], mock_command)

    def test_execute_command(self):
        '''Testing Operations '''
        # Create a mock command and register it
        mock_command = MockCommand()
        mock_command.execute = MagicMock()
        self.command_handler.register_command("test_command", mock_command)

        # Execute the command and check if execute() was called
        self.command_handler.execute_command("test_command")
        mock_command.execute.assert_called_once()

    @patch('app.importlib.import_module')
    def test_load_plugin_success(self, mock_import_module):
        '''Testing Operations '''
        # Mock the plugin module to simulate a successful plugin load
        mock_plugin_module = MagicMock()
        mock_plugin_module.register.return_value = MockCommand
        mock_import_module.return_value = mock_plugin_module

        command_class = self.command_handler.load_plugin('mock_plugin')

        # Check that the register function was called and returned the correct command class
        self.assertEqual(command_class, MockCommand)

    @patch('app.importlib.import_module')
    def test_create_command(self, mock_import_module):
        '''Testing Operations '''
        # Mock the plugin module and its command class
        mock_plugin_module = MagicMock()
        mock_plugin_module.register.return_value = MockCommand
        mock_import_module.return_value = mock_plugin_module

        # Create a command using the handler
        command_instance = self.command_handler.create_command('mock_plugin', 'arg1', 'arg2')

        # Ensure that the command instance was created and registered
        self.assertIsInstance(command_instance, MockCommand)
        self.assertIn('mock_plugin', self.command_handler.commands)


if __name__ == '__main__':
    unittest.main()
