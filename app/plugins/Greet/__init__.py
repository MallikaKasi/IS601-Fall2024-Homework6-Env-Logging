from app.commands import Command


class GreetCommand(Command):
    def execute(self):
        print("     Hello! Welcome To Interactive Calculator")
def register():
    return GreetCommand