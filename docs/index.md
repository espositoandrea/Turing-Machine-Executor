# EMT - Turing Machine Executor<!-- omit in toc -->

Welcome to the EMT documentation!

Here you can get more information on the app and on its source code.

This documentation can be subdivided in two parts:

1. Preliminary definitions on which this software is based
2. Code documentation / User manual

The two parts are then splitted in various files. They are accessible through the sidebar or using the following menu.

- [Preliminary Definitions](#preliminary-definitions)
  - [The Turing Machine](#the-turing-machine)
    - [Formal Definition](#formal-definition)
  - [The Turing Machine's Executor](#the-turing-machines-executor)
- [Definition](#definition)
- [The Software](#the-software)
  - [How to Use EMT](#how-to-use-emt)
    - [Preliminary](#preliminary)
    - [Downloading and Starting](#downloading-and-starting)
    - [Using EMT](#using-emt)
      - [Command Line Arguments](#command-line-arguments)

## Preliminary Definitions

### The Turing Machine

#### Formal Definition

One of the main classes of this app is the class `Machine`, that is the Turing Machine representation.

A Turing Machine _M_ is defined as a 7-tuple:

_M = (Q, S, &lambda;, I, &delta; q<sub>0</sub>, F)_

Where:

- _Q_ is a finite, non-empty set of *states*
- _S_ is a finite, non-empty set of *symbols* called *alphabet*
- _&lambda; &isin; S_ is the *blank* symbol of the alphabet
- _I = S &setminus; { &lambda; }_ is a subset of symbols that are allowed to appear in the input tape
- _&delta; = (Q &setminus; F) &times; S &#8603; Q &times; S &times; { L, R }_ is a partial function called the *transition function*, where _L_ is left shift, _R_ is right shift. If _&delta;_ is not defined on the current state and the current tape symbol, then the machine halts.
- _q<sub>0</sub> &isin; Q_ is the *initial state* of the machine
- _F &sube; Q_ is a non-empty subset of _Q_ that contains the *final states* of the machine: the initial tape is *accepted* by _M_ if it halts in a state of _F_.

### The Turing Machine's Executor

## Definition

A Turing Machine's Executor is an automaton (that may or may not be a machine) that, given an _input tape_, executes step by step the program of a Turing Machine. For this reason, an executor _E_ can be defined as a _pair_ _E=(M, I)_, where _M_ is a [Turing Machine](The-Machine) and _I_ is a sequence of characters that are in the "input" alphabet of the machine _M_. 

## The Software

### How to Use EMT

#### Preliminary

Make sure that you have installed Python 3.7+ and that its location is available in the Path variable of your system. To check for it, run the following command in your favorite console:

```shell
python --version
```

#### Downloading and Starting

1. Download the [latest release](http://github.com/espositoandrea/Turing-Machine-Executor/releases/latest) and unzip it.
2. Open your favorite console in the folder that contains the unzipped files and run

    ```shell
    python setup.py install
    ```

3. Type the following command to start the executor:

    ```shell
    emt
    ```

    Or, as an alternative:

    ```shell
    turing-machine-executor
    ```

#### Using EMT

The executor will prompt you to insert the machine using this method:

1. It will ask for the alphabet of the machine.
   1. **NOTE:** the first symbol that you insert will be considered as the _blank_ (_&lambda;_) symbol (see the [Turing Machine's definition](The-Machine#formal-definition) for more information).
   2. **:warning: WARNING:** duplicates are _not_ managed in any way. The Executor behaviour is unpredicted.
2. It will ask for the list of states
   1. **NOTE:** the first state that you insert will be considered as the _initial state_ (see the [Turing Machine's definition](The-Machine#formal-definition) for more information).
   2. **NOTE:** duplicates will be ignored (if a _state_ is inserted more than once, only the first one inserted will be considered).
3. Once all the states are inserted, it will ask to mark the _halting states_.
   1. Note that the machine will stop as soon as an halting state is reached.
4. It will ask for the machine's program in the following way: for each combination of symbol and state, it will ask for a triplet _(s, d, q)_, where:
   - _s_ is the symbol that will be written in the place of the once read
   - _d_ is the direction that the machine will follow
   - _q_ is the new state that the machine will reach after the movement
     - If _q_ is an halting state, the machine will be stopped and the executor will print the output
   - **NOTE:** if the input is empty, then the combination sybol-state will be ignored. Use this information with caution.
5. It will ask for an input tape to execute the program.
   1. **NOTE:** do _not_ insert the tape using spaces: each space will be considered as a character of the input.

##### Command Line Arguments

Here is a list of arguments and options with which EMT can be launched.

<dl>
    <dt>
        <code>-h</code>, <code>--help</code>
    </dt>
    <dd>
        <p>Prints an help message.</p>
    </dd>
    <dt>
        <code>-v</code>, <code>--version</code>
    </dt>
    <dd>
        <p>Prints EMT's version.</p>
    </dd>
    <dt>
        <code>-a</code>, <code>--all</code>
    </dt>
    <dd>
        <p>If this option is active, the machine will not print only the input and the output, but it will print every step that it does to reach the output <i>(by default this option is disabled)</i>.</p>
    </dd>
</dl>
