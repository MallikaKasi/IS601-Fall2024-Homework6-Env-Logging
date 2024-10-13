from app.commands import Command

class SubtractCommand(Command):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def execute(self):
        print(f"    The result of Subtracting  {self.a} - {self.b} = {self.a - self.b}")

def register():
    return SubtractCommand
