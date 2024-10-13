from app.commands import Command

class AddCommand(Command):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def execute(self):
        print(f"    The result of adding {self.a} + {self.b} = {self.a + self.b}")

def register():
    return AddCommand
