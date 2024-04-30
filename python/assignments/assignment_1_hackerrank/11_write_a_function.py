# An extra day is added to the calendar almost every four years as February 29,
# and the day is called a leap day. It corrects the calendar for the fact that our planet 
# takes approximately 365.25 days to orbit the sun. A leap year contains a leap day.


def is_leap(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                leap = True
            else:
                leap = False
        else:
            leap = True
    else:
        leap = False

    return leap

year = int(input())
print(is_leap(year))


# *************SAMPLE_INPUT***************

# 1990

# ***************OUTPUT******************

# False


