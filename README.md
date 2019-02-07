# A Turing Machine Executor (EMT)<!-- omit in toc -->

A simple executor of _(almost)_ every Turing machine.

- [The Name](#the-name)
- [The Reasons](#the-reasons)
- [How To Use EMT](#how-to-use-emt)
  - [Installing](#installing)
  - [Using The Executor](#using-the-executor)
    - [The Parameters](#the-parameters)
    - [Inputting the Alphabet](#inputting-the-alphabet)
    - [Inputting the States](#inputting-the-states)
- [Known Bugs and Limitations](#known-bugs-and-limitations)

## The Name

**EMT** stands for _Esecutore di Macchine di Turing_, that is the Italian for _"Turing Machine Executor"_.

## The Reasons

To be completely honest I was just really bored and I needed a way to spend my time while learning new languages.

## How To Use EMT

### Installing

To install the executor, you must first install Python 3.7+. After that, simply clone this repository, open your favorite console in the repository's folder and run:

```shell
python setup.py install
```

After that, you can start the executor by simply writing the following command:

```shell
python emt
```

### Using The Executor

#### The Parameters

The executor can be started with some parameters. This is a list of them with a short explaination of what they do.

| Parameter                | Description                                                                            |
| :----------------------- | :------------------------------------------------------------------------------------- |
| `-h`, `--help`           | Prints a help message and a list of all the parameters available                       |
| `-s`, `--show-all-steps` | While executing, EMT will print step by steap each operation it does on the input tape |

#### Inputting the Alphabet

You can input the alphabet of the machine when prompted to by simply writing all the needed characters separated by spaces. Note that the alphabet can only consist of single characters. The _blank_ character is inserted by default into the alphabet and it's represented by the character `^`.

#### Inputting the States

You can input the states by simply writing a name for all the states separated by a space. The _initial state_ is included by default and it's represented with the name `q0`.

## Known Bugs and Limitations

- [ ] This executor can only start right before the input string
- [ ] This executor is not much _user friendly_
