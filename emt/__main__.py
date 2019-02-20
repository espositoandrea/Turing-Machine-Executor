import argparse
from colorama import Fore, Style, init
from pyfiglet import figlet_format
from machine import Machine
from executor import Executor
from textwrap import fill

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
