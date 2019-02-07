class Machine:
    def __init__(self):
        self.__alphabet = ["^"]
        self.__states = {"q0": "q0"}
        self.__program = {}

    def input_alphabet(self):
        new_alpha = input("Insert alphabet (blank is ^): ").split()
        self.__alphabet += new_alpha

    def input_states(self):
        new_states = input("Insert state's names (initial is q0): ").split()
        for i in range(len(new_states)):
            self.__states[new_states[i]] = new_states[i]

    def __check_symbol(self, to_check):
        return to_check and self.__alphabet.__contains__(to_check)

    def __check_state(self, to_check):
        return to_check and self.__states.__contains__(to_check)

    def __check_direction(self, to_check):
        return to_check and ["L", "S", "R"].__contains__(to_check.upper())

    def input_program(self):
        print("""Insert the operations in the form of s d q (in this order, separated by spaces): 
s   the symbol that will be written 
d   the direction that has to be taken after writing s (in {L, S, R}, where S will stop the execution) 
q   the new state. 
Leave the line blank to ignore that particular symbol/state combination.""")

        for state in self.__states:
            for char in self.__alphabet:
                print("Symbol: {0} --- State: {1}".format(char, state))
                triplet = self.__input_triplet()
                if triplet is not None:
                    self.__program[(char, self.__states[state])] = triplet

    def __input_triplet(self):
        line = input()
        triplet = None
        if line:
            splitted = (line.split()+ [None]*3)[:3]
            has_to_end_while = self.__check_symbol(splitted[0]) and self.__check_direction(splitted[1]) and self.__check_state(splitted[2])
            triplet = (splitted[0], splitted[1].upper(), self.__states[splitted[2]]) if has_to_end_while else None
            while not has_to_end_while:
                line = input()
                if line:
                    splitted = (line.split()+ [None]*3)[:3]
                    has_to_end_while = self.__check_symbol(splitted[0]) and self.__check_direction(splitted[1]) and self.__check_state(splitted[2])
                    triplet = (splitted[0], splitted[1].upper(), self.__states[splitted[2]]) if has_to_end_while else None
                else:
                    has_to_end_while = True
                    triplet = None

        return triplet

    def input_tape_string(self):
        tape = list(input("Insert an input for the machine: "))
        fault = False

        for char in tape:
            if not self.__alphabet.__contains__(char):
                fault = True

        while fault:
            tape = input(
                "Error. Insert a valid input for the machine: ").split()
            fault = False
            for char in tape:
                if not self.__alphabet.__contains__(char):
                    fault = True

        return tape

    def get_program(self):
        return self.__program

    def get_first_state(self):
        return self.__states["q0"]

    def get_blank(self):
        return self.__alphabet[0]
