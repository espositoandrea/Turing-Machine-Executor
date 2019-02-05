from machine import Machine
from executor import Executor

turing_machine = Machine()

turing_machine.input_alphabet()
turing_machine.input_states()
turing_machine.input_program()

input_tape = turing_machine.input_tape_string()
print(input_tape)

executor = Executor(turing_machine, input_tape)
executor.exec()
