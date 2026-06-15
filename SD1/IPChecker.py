"""
Author: Maria Caro
Class: Software Development - Programming and Design Principles 5N2927
Program: IPv4 Address Validator and Classifier
Description:
    This program asks the user to enter an IPv4 address (x.x.x.x).
    It checks that:
      1) The address has 4 parts separated by dots
      2) Each part is numeric
      3) Each part is in the range 0 to 255
    If the address is valid, it prints the IP class (A, B, C, D, E, or Loopback).
Last edited: 2026-01-26
"""


class IPAddressChecker:
    # This class contains methods to validate and classify IPv4 addresses.

    def __init__(self):
        # Constructor (initializer): runs when we do IPAddressChecker().
        # We can put setup code here later if needed.
        pass

    def has_ipv4_format(self, ip_text):
        # Splits the string by "." and checks it has exactly 4 parts.
        # Returns the list of parts if correct, otherwise returns None.
        parts = ip_text.split(".")
        if len(parts) != 4:
            return None
        else:
            return parts

    def parts_are_numeric(self, parts):
        # Checks each part contains digits only (0-9).
        # Example: "12" is numeric, "12a" is not.
        for part in parts:
            if not part.isdigit():
                return False
        return True

    def parts_in_range(self, parts):
        # Converts each part to an integer and checks the range 0 to 255.
        for part in parts:
            num = int(part)  # safe because we call this after parts_are_numeric()
            if num < 0 or num > 255:
                return False
        return True

    def get_ip_class(self, parts):
        # Uses the first octet (first part) to determine the IP class.
        first = int(parts[0])
        ipClass = ""

        if first == 127:
            ipClass = "Loopback"
        elif 1 <= first <= 126:
            ipClass = "A"
        elif 128 <= first <= 191:
            ipClass = "B"
        elif 192 <= first <= 223:
            ipClass = "C"
        elif 224 <= first <= 239:
            ipClass = "D"
        elif 240 <= first <= 255:
            ipClass = "E"
        else:
            # This covers uncommon/unspecified cases like first octet = 0
            ipClass = "Unknown"

        return ipClass


def main():
    # Create an object from the class so we can use its methods
    checker = IPAddressChecker()

    # Main menu loop: keeps running until the user chooses Exit
    while True:
        print("\n--- IP ADDRESS MENU ---")
        print("1. Check an IPv4 address")
        print("2. Exit")

        # Read the user's menu choice and strip extra spaces
        choice = input("Choose an option (1-2): ").strip()

        if choice == "1":
            # Ask user for an IP address and remove extra spaces
            ip = input("Enter an IP address with format (x.x.x.x): ").strip()

            # Step 1: Check format and get the 4 parts
            parts = checker.has_ipv4_format(ip)
            if parts is None:
                print("Invalid format: must be x.x.x.x (4 parts).")
                continue

            # Step 2: Check all parts are numbers
            if checker.parts_are_numeric(parts) == False:
                print("Invalid IP: all 4 parts must be numbers.")
                continue

            # Step 3: Check each number is in the valid range 0-255
            if checker.parts_in_range(parts) == False:
                print("Invalid IP: each number must be between 0 and 255.")
                continue

            # Step 4: If valid, classify the IP address
            ip_class = checker.get_ip_class(parts)
            print(f"{ip} is a valid IP Address of type Class {ip_class}")

        elif choice == "2":
            # Exit option
            print("Goodbye")
            break
        else:
            # Any other input is not a valid menu option
            print("Invalid choice, try again")


# Run the program
if __name__ == "__main__":
    main()
