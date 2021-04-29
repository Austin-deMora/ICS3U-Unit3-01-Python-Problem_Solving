#!/usr/bin/env python3

# Created by: Austin de Mora
# Created on: April 2021
# This program calculates the sum of two numbers

import math


def main():
    # This function calculates the total of 2 numbers

    # Input
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))

    # process
    total = a + b

    # Output
    print("")
    print("Total of the two numbers is {}".format(total))


if __name__ == "__main__":
    main()
