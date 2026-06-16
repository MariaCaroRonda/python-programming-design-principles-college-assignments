# Development Notes – SD1 IPv4 Address Validator and Classifier

## Requirements

The program needed to:

* Ask the user to enter an IPv4 address
* Validate the address format
* Check numeric values
* Check valid ranges
* Identify the IP class
* Display clear messages

## Design Decisions

I created an `IPAddressChecker` class to separate the validation and classification logic.

The validation process was divided into several methods:

* `has_ipv4_format()`
* `parts_are_numeric()`
* `parts_in_range()`
* `get_ip_class()`

This made each method responsible for one task and made the code easier to understand and maintain.

## Challenges

One challenge was making sure invalid addresses were rejected before classification.

To solve this, I performed validation in stages before identifying the IP class.

I also needed to handle invalid inputs such as:

* Missing octets
* Non-numeric values
* Numbers outside the valid range

## What I Learned

This project helped me practise:

* Object-Oriented Programming (OOP)
* User input validation
* String manipulation
* Loops and conditional statements
* Creating and using classes
* Testing a program with valid and invalid data

## Possible Improvements

Some ideas for future improvements:

* Add IPv6 validation
* Save results to a file
* Create a graphical user interface (GUI)
* Add automated tests

During testing and review, I identified a couple of areas that could be improved:

* The validation process is split across several methods, which results in multiple validation checks in the main program loop. This could be refactored into a simpler validation workflow.
* Addresses beginning with `0` are currently classified as `Unknown`. The classification logic could be extended to handle these addresses more clearly.

## Conclusion

This project gave me practical experience with Python programming, input validation, and object-oriented programming.

It also helped me understand the importance of checking user input before processing data and organising code into smaller, reusable methods.
