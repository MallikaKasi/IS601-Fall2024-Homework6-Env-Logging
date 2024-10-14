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

Added Loading Environment Variables

Logging using Logger library

Continuous Integration

Added workflow in GitHub Actions to run tests on GitHub automaticly

### Testing Commands:

pytest 

pytest --pylint

pytest --pylint --cov

pytest tests/test_main.py.


### Run the Applications:
To run the Interactive Calculator: python main.py I

To perfomr the calculation directly from Command Line:  python main.py 2 3 add


### Test Results:

![image](https://github.com/user-attachments/assets/1dc929b9-acb1-4eb2-af0d-e08c35ef9678)
![image](https://github.com/user-attachments/assets/6d483887-aff6-4e55-a44f-ccd181d81bf5)
![image](https://github.com/user-attachments/assets/cc98b3c3-321b-4110-877d-8d445faaa142)



