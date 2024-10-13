## Welcome to Command-Plugin based Calculator Application 

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
## (venv) mallikakasi@HOME:~/NJIT-FALL-2024/IS601-Projects/Week5/Week5_Project$ pytest
======================================================================== test session starts =========================================================================

tests/test_main.py::test_calculate_and_print[5-3-add-The result of 5 add 3 is equal to 8] PASSED                                                               [ 55%]

tests/test_operations.py::test_operation[a3-b3-add-expected3] PASSED                                                                                           [ 95%]

tests/test_operations.py::test_operation[a4-b4-add-expected4] PASSED                                                                                           [ 97%]

tests/test_operations.py::test_divide_by_zero PASSED                                                                                                           [100%]

========================================================================= 40 passed in 0.21s =========================================================================
## (venv) mallikakasi@HOME:~/NJIT-FALL-2024/IS601-Projects/Week5/Week5_Project$ pytest --pylint 
======================================================================== test session starts =========================================================================

tests/test_operations.py::test_operation[a3-b3-subtract-expected3] PASSED                                                                                      [ 95%]

tests/test_operations.py::test_operation[a4-b4-add-expected4] PASSED                                                                                           [ 97%]

tests/test_operations.py::test_divide_by_zero PASSED                                                                                                           [100%]

=================================================================== 40 passed, 8 skipped in 1.24s ====================================================================
## (venv) mallikakasi@HOME:~/NJIT-FALL-2024/IS601-Projects/Week5/Week5_Project$ pytest --pylint --cov 
======================================================================== test session starts =========================================================================

---------- coverage: platform linux, python 3.10.12-final-0 ----------
Name                             Stmts   Miss  Cover
----------------------------------------------------

app/__init__.py                     83     71    14%

tests/test_main.py                  51      4    92%

tests/test_operations.py            11      0   100%
----------------------------------------------------

TOTAL                              418     92    78%
=================================================================== 40 passed, 8 skipped in 1.80s ====================================================================
## (venv) mallikakasi@HOME:~/NJIT-FALL-2024/IS601-Projects/Week5/Week5_Project$ pytest --num_records=10
======================================================================== test session starts =========================================================================


tests/test_operations.py::test_operation[a98-b98-multiply-expected98] PASSED                                                                                   [ 99%]

tests/test_operations.py::test_operation[a99-b99-divide-expected99] PASSED                                                                                     [ 99%]

tests/test_operations.py::test_divide_by_zero PASSED                                                                                                           [100%]

======================================================================== 230 passed in 0.81s =========================================================================
## (venv) mallikakasi@HOME:~/NJIT-FALL-2024/IS601-Projects/Week5/Week5_Project$ python main.py 
## (venv) venvmallikakasi@HOME:~/NJIT-FALL-2024/IS601-Projects/Week5/Week5_Project$ python main.py
 
      Welcome to Command-Plugin based Calculator Application:    
           

Usage of this Calculator:

    To start the Interactive Calculator: python main.py I 

    To perform the calculation Using Direct Commamd Line:

       python main.py <number1> <number2> add

       python main.py <number1> <number2> subtract

       python main.py <number1> <number2> multiply

       python main.py <number1> <number2> divide


(venv) venvmallikakasi@HOME:~/NJIT-FALL-2024/IS601-Projects/Week5/Week5_Project$ python main.py 2 3 add

The result of 2 add 3 is equal to 5

(venv) venvmallikakasi@HOME:~/NJIT-FALL-2024/IS601-Projects/Week5/Week5_Project$ python main.py 2 3 subtract

The result of 2 subtract 3 is equal to -1

(venv) venvmallikakasi@HOME:~/NJIT-FALL-2024/IS601-Projects/Week5/Week5_Project$ python main.py I


Option To Perform Interative Calculation:
        
              
Available Calculator Commands:
 

        Type Add : To Perform Add Operation 

        Type Divide : To Perform Divide Operation 

        Type Exit : To Perform Exit Operation 

        Type Greet : To Perform Greet Operation 

        Type Menu : To Perform Menu Operation 

        Type Multiply : To Perform Multiply Operation 

        Type Subtract : To Perform Subtract Operation 
 
Choose an option : Add

   Enter the first number: 23

   Enter the second number: 23

    The result of adding 23.0 + 23.0 = 46.0

 
Type C : to Continue , Type E : to Exit  

C

Choose an option : Divide

   Enter the first number: 40

   Enter the second number: 5

    The result of Dividing 40.0 / 5.0 = 8.0
 

Type C : to Continue , Type E : to Exit  
C

Choose an option : Greet

     Hello! Welcome To Interactive Calculator
 

Type C : to Continue , Type E : to Exit  
C

Choose an option : Menu
              
Available Calculator Commands:
 

        Type Add : To Perform Add Operation 

        Type Divide : To Perform Divide Operation 

        Type Exit : To Perform Exit Operation 

        Type Greet : To Perform Greet Operation 

        Type Menu : To Perform Menu Operation 

        Type Multiply : To Perform Multiply Operation 

        Type Subtract : To Perform Subtract Operation 
 
 
Type C : to Continue , Type E : to Exit  
E

Exiting...Goodbye!!!!!

(venv) venvmallikakasi@HOME:~/NJIT-FALL-2024/IS601-Projects/Week5/Week5_Project$

