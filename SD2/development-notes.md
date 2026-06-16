# Development Notes – SD2 Calculator Application

## Requirements

The program needed to:

* Add two numbers
* Subtract two numbers
* Multiply two numbers
* Divide two numbers
* Validate user input
* Handle division by zero
* Display clear messages
* Provide a menu-driven interface

## Design Decisions

I created a `Calculator` class to group the calculator operations together.

Each operation was placed in its own method:

* `add_numbers()`
* `subtract_numbers()`
* `multiply_numbers()`
* `divide_numbers()`

I also created a separate method called `get_numbers()` to handle user input and validation.

This helped reduce repeated code and made the program easier to maintain.

## Challenges

One challenge was making sure the program accepted only valid numbers.

To solve this, I used `try/except` blocks to catch invalid input and repeatedly ask the user to enter a valid number.

Another challenge was handling division by zero.

The program raises a `ZeroDivisionError` and displays a clear message to the user instead of crashing.

## What I Learned

This project helped me practise:

* Object-Oriented Programming (OOP)
* User input validation
* Arithmetic operations
* Loops and conditional statements
* Exception handling
* Testing a program with different inputs
* Writing technical documentation

## Possible Improvements

Some ideas for future improvements:

* Add more mathematical operations
* Support calculations with more than two numbers
* Store calculation history
* Save results to a file
* Create a graphical user interface (GUI)
* Add automated tests

## Conclusion

This project gave me practical experience creating a menu-driven Python application.

It also helped me improve my understanding of user input validation, exception handling, and object-oriented programming.
