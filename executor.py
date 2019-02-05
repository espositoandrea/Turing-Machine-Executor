import machine

class Executor:
    def __init__(self, turing_machine, input_tape):
        self.__machine = turing_machine
        self.__output = input_tape
    
    def exec(self):
        pass