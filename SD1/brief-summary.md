# Brief Summary: SD1 IPv4 Address Validator and Classifier

## Module

Programming and Design Principles 5N2927

## Assignment Title

Skills Demonstration 1: Design, code and test a Python program that validates and classifies IPv4 addresses.

## Task Summary

The task was to create a Python program that asks the user to enter an IPv4 address and checks whether it is valid.

An IPv4 address is valid if it:

- Contains four numerical values
- Uses dots to separate each value
- Has exactly four parts
- Contains only numeric values
- Has each value within the range 0 to 255

If the IP address is valid, the program then classifies it using the first octet.

The classification rules are:

- Class A: first octet from 1 to 126
- Loopback: first octet is 127
- Class B: first octet from 128 to 191
- Class C: first octet from 192 to 223
- Class D: first octet from 224 to 239
- Class E: first octet from 240 to 255

## Main Requirements

The assignment required:

- A working Python program
- A user-friendly interface
- Clear prompts and output messages
- IP address validation
- IP address classification
- Clear comments in the source code
- A simple algorithm
- A flowchart
- Pseudocode
- A data dictionary
- Testing and debugging evidence
- An evaluation of the completed program

## Implementation Summary

My solution uses an `IPAddressChecker` class with separate methods for each main part of the program.

The program checks:

- Whether the IP address has four parts
- Whether each part is numeric
- Whether each number is between 0 and 255
- Which class the IP address belongs to

The program also uses a menu-driven interface so the user can choose whether to check an IP address or exit the program.

## Result

Distinction — 30/30

## Tutor Feedback Summary

The feedback highlighted:

- Excellent use of object-oriented programming
- Thorough commenting throughout the code
- Comprehensive test cases with screenshots
- Testing that covered boundary values and invalid inputs
- Detailed pseudocode and flowchart

The feedback also noted possible improvements:

- The validation logic is divided across several methods, which creates several `if` checks in the main loop
- Addresses starting with `0` are classified as `Unknown`

## What I Learned

This assignment helped me practise:
- Splitting strings in Python
- Validating user input
- Using loops and conditional statements
- Creating and using a Python class
- Writing separate methods for different validation tasks
- Checking numeric ranges
- Designing a menu-driven console program
- Testing a program with valid, invalid, and boundary data
- Documenting a Python programming assignment

