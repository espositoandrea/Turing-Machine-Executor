import machine

class Executor:
    def __init__(self, turing_machine, input_tape):
        self.__machine = turing_machine
        self.__output = [turing_machine.get_blank()] + input_tape + [turing_machine.get_blank()]
    
    def exec(self, step_by_step = False):
        program = self.__machine.get_program()
        current_state = self.__machine.get_first_state()
        i = 0
        direction = "R"
        if step_by_step:
            print(current_state, end=": ")
            print(self.__output)
        while direction != "S":
            read = self.__output[i]
            direction = program[(read, current_state)][1]
            self.__output[i] = program[(read, current_state)][0]
            current_state = program[(read, current_state)][2]
            i = i + 1 if direction == "R" else i - 1
            if i >= len(self.__output):
                self.__output += ([self.__machine.get_blank()] * (i - len(self.__output) + 1))
            if step_by_step:
                print(current_state, end=": ")
                print(self.__output)

    
    def get_output(self):
        return self.__output

    def print_tape(self, tape):
        printed_something = False
        for char in tape:
            if char != self.__machine.get_blank() or printed_something:
                print(char, end="")
        print()