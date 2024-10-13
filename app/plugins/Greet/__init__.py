import logging
from app.commands import Command


class GreetCommand(Command):
    def execute(self):
        logging.info(f"Hello! Welcome To Interactive Calculator")

        print("     Hello! Welcome To Interactive Calculator")
def register():
    return GreetCommand