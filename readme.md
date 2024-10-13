## Welcome to Command-Plugin based Calculator Application With Environment Variables Loading Concept

This is the interactive Calculator that performs 

Addition

Subtraction

Multiplication

Division

### This Calclulatore can run in 2 modes

1) Interactive Mode which is implemneted using plugins

2) Implementation of command pattern and REPL

Added a main.py file to serve as an entry point to this program and provided command line utilities.

Covers REPL and command patterns with four basic commands add, subtract, multiply and divide.

Implements a menu command to list available command and usage example.

Implemented Greet and Exit Commands

Uses Plugin architecture to dynamically load new plugins.

### Testing Commands:

pytest 

pytest --pylint

pytest --pylint --cov

pytest tests/test_main.py.


### Run the Applications:
To run the Interactive Calculator: python main.py I

To perfomr the calculation directly from Command Line:  python main.py 2 3 add


### Test Results:

Add test Result Image

