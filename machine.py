class Machine:
    def __init__(self):
        self.alphabet = ["@"]
        self.states = {"q0": 0}
        self.program = {}

    def set_alphabet(self, new_alpha):
        self.alphabet += new_alpha

    def set_states(self, new_states):
        for i in range(len(new_states)):
            self.states[new_states[i]] = i + 1

    def input_alphabet(self):
        new_alpha = input("Insert alphabet (blank is @): ").split()
        self.alphabet = ["@"] + new_alpha

    def input_states(self):
        new_states = input("Insert state's names (initial is q0): ").split()
        for i in range(len(new_states)):
            self.states[new_states[i]] = i + 1

    def input_symbol(self):
        symbol = input("Insert symbol: ")
        while not self.alphabet.__contains__(symbol) and symbol:
            symbol = input("Error. Insert valid symbol: ")
        return symbol

    def input_state(self):
        state = input("Insert state: ")
        while not self.states.__contains__(state) and state:
            state = input("Error. Insert valid state: ")
        return state

    def input_direction(self):
        direction = input("Insert direction (L, S or R): ").upper()
        while not ["L", "S", "R"].__contains__(direction) and direction:
            direction = input(
                "Error. Insert valid direction (L, S or R): ").upper()
        return direction

    def input_program(self):
        print("""Insert the operations in the form of (s, d, q): 
s   the symbol that will be written 
d   the direction that has to be taken after writing s (in {L, S, R}, where S will stop the execution) 
q   the new state. 
Leave one of the options blank to ignore the particular symbol/state combination.""")

        for state in self.states:
            for char in self.alphabet:
                print("Symbol: {0} --- State: {1}".format(char, state))
                symbol_to_write = self.input_symbol()
                if not symbol_to_write:
                    break
                direction = self.input_direction()
                if not direction:
                    break
                new_state = self.input_state()
                if not new_state:
                    break
                self.program[(char, state)] = (
                    symbol_to_write, direction, new_state)

    def input_tape_string(self):
        tape = input("Insert an input for the machine: ").split()
        fault = False

        for char in tape:
            if not self.alphabet.__contains__(char):
                fault = True

        while fault:
            tape = input(
                "Error. Insert a valid input for the machine: ").split()
            fault = False
            for char in tape:
                if not self.alphabet.__contains__(char):
                    fault = True

        return tape
