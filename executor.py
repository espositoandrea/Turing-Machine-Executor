import machine

class Executor:
    def __init__(self, turing_machine, input_tape):
        self.machine = turing_machine
        self.input = input_tape
    
    def exec(self):
        pass