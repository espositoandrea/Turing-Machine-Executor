# EMT’s code documentation!

## Class: Machine


#### class machine.Machine()
The Turing’s machine.


### get_alphabet()
Get the alphabet of the machine.


* **Returns**

    The alphabet of the machine.



### get_blank()
Get the blank character of the machine.


* **Returns**

    The blank character.



### get_first_state()
Get the first state of the machine (the initial state).


* **Returns**

    The initial state.



### get_program()
Get the program of the machine.


* **Returns**

    The program of the machine.



### get_states()
Get the states of the machine.


* **Returns**

    The states of the machine.



### static is_direction(to_check: str)
Check if a string represents a valid direction for a Turing machine.


* **Parameters**

    **to_check** – The string to be checked.



* **Returns**

    True if the string is “L” or “R” (case insensitive), False otherwise.



### is_halt(state: str)
Check if a state is an halting state for the machine.


* **Parameters**

    **state** – The state to be checked.



* **Returns**

    True if the state is an halting state, False otherwise.



* **Raise**

    ValueError if the state is not a valid state for the machine.



### is_state(to_check: str)
Check if a string is a valid state for the machine.


* **Parameters**

    **to_check** – The string to be checked.



* **Returns**

    True if the string is in the set of states, False otherwise.



### is_symbol(to_check: str)
Check if a character is a valid symbol for the machine.


* **Parameters**

    **to_check** – The character to be checked.



* **Returns**

    True if the character is in the alphabet of the machine, False otherwise.



### set_alphabet(new_alpha: str)
Set the alphabet of the Turing machine.


* **Parameters**

    **new_alpha** – The new alphabet



### set_halting_states(halting_states: List[str])
Set the machine’s halting states.


* **Parameters**

    **halting_states** – The halting states.



### set_program(new_program: Dict[Tuple[str, str], Optional[Tuple[str, str, str]]])
Set the program of the machine.


* **Parameters**

    **new_program** – The program



### set_states(new_states: List[str])
Set the machine’s states.


* **Parameters**

    **new_states** – The new states.
