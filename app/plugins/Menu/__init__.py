# app/plugins/menu.py

from app.commands import Command
from app.commands import CommandHandler

class MenuCommand(Command):
    def __init__(self, command_handler: CommandHandler):
        self.command_handler = command_handler

    def execute(self):
        self.command_handler.list_commands()

def register():
    return MenuCommand  # Return the class, not an instance
