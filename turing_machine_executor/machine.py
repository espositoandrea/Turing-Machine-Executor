from typing import List, Dict, Tuple, Optional


class Machine:
    """
    The Turing's machine.
    """

    def __init__(self):
        """
        Create a new Turing machine with an empty alphabet, an empty set of states,
        an empty program function and no initial state.
        """
        self.__alphabet = []
        self.__states = {}
        self.__program = {}
        self.__initial_state = ""

    def set_alphabet(self, new_alpha: str) -> None:
        """
        Set the alphabet of the Turing machine.

        :param new_alpha: The new alphabet
        """
        self.__alphabet = new_alpha

    def set_states(self, new_states: List[str]) -> None:
        """
        Set the machine's states.

        :param new_states: The new states.
        """
        self.__initial_state = new_states[0]
        for state in new_states:
            self.__states[state] = False

    def set_halting_states(self, halting_states: List[str]) -> None:
        """
        Set the machine's halting states.

        :param halting_states: The halting states.
        """
        for state in halting_states:
            self.__states[state] = True

    def is_symbol(self, to_check: str) -> bool:
        """
        Check if a character is a valid symbol for the machine.

        :param to_check: The character to be checked.
        :return: True if the character is in the alphabet of the machine, False otherwise.
        """
        return to_check and self.__alphabet.__contains__(to_check)

    def is_state(self, to_check: str) -> bool:
        """
        Check if a string is a valid state for the machine.

        :param to_check: The string to be checked.
        :return: True if the string is in the set of states, False otherwise.
        """
        return to_check and self.__states.__contains__(to_check)

    @staticmethod
    def is_direction(to_check: str) -> bool:
        """
        Check if a string represents a valid direction for a Turing machine.

        :param to_check: The string to be checked.
        :return: True if the string is "L" or "R" (case insensitive), False otherwise.
        """
        return to_check and ["L", "R"].__contains__(to_check.upper())

    def is_halt(self, state: str) -> bool:
        """
        Check if a state is an halting state for the machine.

        :param state: The state to be checked.
        :return: True if the state is an halting state, False otherwise.
        :raise: ValueError if the state is not a valid state for the machine.
        """
        if not self.is_state(state):
            raise ValueError("The state is not a state of the turing machine (state not in self.states)")
        return self.__states[state]

    def set_program(self, new_program: Dict[Tuple[str, str], Optional[Tuple[str, str, str]]]) -> None:
        """
        Set the program of the machine.

        :param new_program: The program
        """
        self.__program = new_program

    def get_program(self) -> Dict[Tuple[str, str], Optional[Tuple[str, str, str]]]:
        """
        Get the program of the machine.

        :return: The program of the machine.
        """
        return self.__program

    def get_first_state(self) -> str:
        """
        Get the first state of the machine (the initial state).

        :return: The initial state.
        """
        return self.__initial_state

    def get_states(self) -> Dict[str, bool]:
        """
        Get the states of the machine.

        :return: The states of the machine.
        """
        return self.__states

    def get_alphabet(self) -> List[str]:
        """
        Get the alphabet of the machine.

        :return: The alphabet of the machine.
        """
        return self.__alphabet

    def get_blank(self) -> str:
        """
        Get the blank character of the machine.

        :return: The blank character.
        """
        return self.__alphabet[0]
