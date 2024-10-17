import logging
from icecream import ic
from app.commands import Command
from app import App


class GreetCommand(Command):
    def execute(self):
        logging.info(f"Invoked Greet Operation")
        logging.debug(ic(App))
        logging.info(f"Hello! Welcome To Interactive Calculator")

        print("     Hello! Welcome To Interactive Calculator")
def register():
    return GreetCommand