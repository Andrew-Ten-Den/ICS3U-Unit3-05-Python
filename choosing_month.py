#!/usr/bin/env python3

# Created by: Andrew Ten-Den
# Created on: March 2022
# This program lets the user pick a number that corresponds with a month


def main():
    # this function lets the user pick a number that corresponds with a month

    # input
    month_number = int(input("Enter a number of the month (ex: 3 is March): "))

    # process & output
    if month_number == 1:
        print("January")

    elif month_number == 2:
        print("February")

    elif month_number == 3:
        print("March")

    elif month_number == 4:
        print("April")

    elif month_number == 5:
        print("May")

    elif month_number == 6:
        print("June")

    elif month_number == 7:
        print("July")

    elif month_number == 8:
        print("August")

    elif month_number == 9:
        print("September")

    elif month_number == 10:
        print("October")

    elif month_number == 11:
        print("November")

    elif month_number == 12:
        print("December")

    else:
        print("No idea!")

    print("")
    print("Done")


if __name__ == "__main__":
    main()
