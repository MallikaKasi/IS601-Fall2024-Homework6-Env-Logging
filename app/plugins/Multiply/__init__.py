from app.commands import Command

class MultiplyCommand(Command):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def execute(self):
        print(f"    The result of Multiplying {self.a} * {self.b} = {self.a * self.b}")

def register():
    return MultiplyCommand
