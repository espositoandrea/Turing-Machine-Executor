import argparse
from machine import Machine
from executor import Executor

parser = argparse.ArgumentParser(description="Execute and test a Turing machine")
parser.add_argument("-s", "--show-all-steps", dest="show_all_steps", action="store_true", help="Show all the steps the machine does to end its loop.")
args = parser.parse_args()

turing_machine = Machine()

turing_machine.input_alphabet()
turing_machine.input_states()
turing_machine.input_program()

input_tape = turing_machine.input_tape_string()

executor = Executor(turing_machine, input_tape)
print("Begun:", end=" ")
executor.print_tape(input_tape)
executor.exec(step_by_step=args.show_all_steps)

print("Ended:", end=" ")
executor.print_tape(executor.get_output())
