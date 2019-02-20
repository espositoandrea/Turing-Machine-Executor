import argparse
from colorama import Fore, Style, init
from pyfiglet import figlet_format
from machine import Machine
from executor import Executor
from textwrap import fill, dedent


def input_alphabet(turing_machine):
    new_alpha = input("Insert alphabet (blank is ^): ").split()
    turing_machine.set_alphabet(new_alpha)


def input_states(turing_machine):
    new_states = input("Insert state's names (initial is q0): ").split()
    turing_machine.set_states(new_states)


def input_program(turing_machine):
    def input_triplet():
        line = input("Insert triplet: ")
        triplet = None
        if line:
            splitted = (line.split() + [None]*3)[:3]
            has_to_end_while = turing_machine.is_symbol(splitted[0]) and turing_machine.is_direction(
                splitted[1]) and turing_machine.is_state(splitted[2])
            triplet = (splitted[0], splitted[1].upper(), turing_machine.get_states()[
                       splitted[2]]) if has_to_end_while else None
            while not has_to_end_while:
                line = input("Error. Reinsert triplet: ")
                if line:
                    splitted = (line.split() + [None]*3)[:3]
                    has_to_end_while = turing_machine.is_symbol(splitted[0]) and turing_machine.is_direction(
                        splitted[1]) and turing_machine.is_state(splitted[2])
                    triplet = (splitted[0], splitted[1].upper(), turing_machine.get_states()[
                               splitted[2]]) if has_to_end_while else None
                else:
                    has_to_end_while = True
                    triplet = None
        else:
            print("Line is empty. Combination skypped.")

        return triplet

    print(dedent('''\
        Insert the operations in the form of s d q (in this order, separated by spaces):
        s   the symbol that will be written
        d   the direction that has to be taken after writing s (in {L, S, R}, where S will stop the execution)
        q   the new state.
        Leave the line blank to ignore that particular symbol/state combination.'''))
    program = {}
    for state in turing_machine.get_states():
        for char in turing_machine.get_alphabet():
            print(f"Symbol: {char} --- State: {state}")
            triplet = input_triplet()
            program[(char, turing_machine.get_states()[state])] = triplet
    turing_machine.set_program(program)


def input_tape_string(turing_machine):
    tape = list(input("Insert an input for the machine: "))
    fault = False

    for char in tape:
        if not turing_machine.is_symbol(char):
            fault = True

    while fault:
        tape = input("Error. Insert a valid input for the machine: ").split()
        fault = False
        for char in tape:
            if not turing_machine.is_symbol(char):
                fault = True

    return tape


if __name__ == "__main__":
    init()

    parser = argparse.ArgumentParser(
        description="Execute and test a Turing machine")
    parser.add_argument("-v", "--version", dest="version",
                        action="store_true", help="Prints the software's version.")
    parser.add_argument("-a", "--all", dest="show_all_steps",
                        action="store_true", help="Show all the steps the machine does to end its loop.")
    args = parser.parse_args()

    if args.version:
        import pkg_resources
        version = pkg_resources.require("emt")[0].version
        print(
            Fore.RED + figlet_format(f"EMT v.{version}", font="epic") + Style.RESET_ALL)
        print(f"EMT - The Turing Machine Executor, version {version}")
        print("\nEMT  Copyright (C) 2019  Andrea Esposito\n" +
              fill("This program comes with ABSOLUTELY NO WARRANTY. "
                   "This is free software, and you are welcome to redistribute "
                   "it under certain conditions. "
                   "Visit the LICENSE file for more information."))
        exit()

    print(Fore.RED + figlet_format("EMT", font="epic") + Style.RESET_ALL)

    turing_machine = Machine()

    input_alphabet(turing_machine)
    input_states(turing_machine)
    input_program(turing_machine)

    input_tape = input_tape_string(turing_machine)

    executor = Executor(turing_machine, input_tape)
    print("Begun:", end=" ")
    executor.print_tape(input_tape)
    executor.exec(step_by_step=args.show_all_steps)

    print("Ended:", end=" ")
    executor.print_tape(executor.get_output())
