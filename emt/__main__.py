import argparse
from colorama import Fore, Style, init
from pyfiglet import figlet_format
from machine import Machine
from executor import Executor

if __name__ == "__main__":
    init()

    parser = argparse.ArgumentParser(description="Execute and test a Turing machine")
    parser.add_argument("-s", "--show-all-steps", dest="show_all_steps", action="store_true", help="Show all the steps the machine does to end its loop.")
    args = parser.parse_args()

    print(Fore.RED + figlet_format("EMT", font="epic") + Style.RESET_ALL)

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
