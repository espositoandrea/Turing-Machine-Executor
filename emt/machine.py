class Machine:
    def __init__(self):
        self.__alphabet = ["^"]
        self.__states = {"q0": "q0"}
        self.__program = {}

    def set_alphabet(self, new_alpha):
        self.__alphabet += new_alpha

    def set_states(self, new_states):
        for i in range(len(new_states)):
            self.__states[new_states[i]] = new_states[i]

    def is_symbol(self, to_check):
        return to_check and self.__alphabet.__contains__(to_check)

    def is_state(self, to_check):
        return to_check and self.__states.__contains__(to_check)

    def is_direction(self, to_check):
        return to_check and ["L", "S", "R"].__contains__(to_check.upper())

    def set_program(self, new_program):
        self.__program = new_program

    def get_program(self):
        return self.__program

    def get_first_state(self):
        return self.__states["q0"]
    def get_states(self):
        return self.__states
    def get_alphabet(self):
        return self.__alphabet

    def get_blank(self):
        return self.__alphabet[0]
