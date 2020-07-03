'Write an if statement to determine whether a variable holding a year is a leap year.'

def main():
    leap_year()

def leap_year():
    year = int(input("Enter a year: "))

    #Leap year check using if-else statement

    # if (year % 4) == 0:
    #     print("{0} is not a leap year".format(year))
    # elif (year % 100) == 0:
    #     print("{0} is not a leap year".format(year))
    # elif (year % 400) == 0:
    #     print("{0} is a leap year".format(year))
    # else:
    #     print("{0} is not a leap year".format(year))

    if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
        print("{0} is leap year".format(year))
    else:
        print("{0} is not leap year".format(year))

if __name__== "__main__":
    main()