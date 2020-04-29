"""
CTEC 121
Robert Ballenger
Module 2 Lab 2
4/29/20 Demo Code for Class
"""

""" IPO template
Input(s): list/description
Process: description of what function does
Output: return value and description
"""




from math import *
def main():

    print("\ndemo use of type()")
    print("Ah you scrolled away and I can't see what you did anymore. bummer.")

    print("\ndemo from input() Canvas page")
    # Get a string
    aString = input("Enter a string of characters: ")
    print(aString)

    # Print 2 blank lines
    # print("\n\n")

    # Get an integer
    # int() does not except numbers with decimals or non-numeric strings
    myInt = int(input("Enter a number: "))
    print(myInt)

    # Print 2 blank lines
    # print("\n\n")

    # Get a floating point number
    myFloat = float(input("Enter a number (decimals are ok): "))
    print(myFloat)

    # Print 2 blank lines
    # print("\n\n")

    # Evaluate an expression entered
    # Enter 3+4
    aNumber = eval(input("Enter a number or a numeric expressions: "))
    print(aNumber)

    # Print 2 blank lines
    # print("\n\n")

    x, y = eval(input("Enter two numbers separated by a comma: "))
    print(x, y)
    print(type(x))
    print()

    x, y = input("provide two values: ").split()
    print(x, y)
    print(type(x))
    print()

    # demo definite loops
    for i in [10, 1, 2, 3]:
        print(i)
    print()

    for count in range(4):
        print(count)
    print()

    for i in range(2, 11, 2):
        print(i)
    print()


main()
