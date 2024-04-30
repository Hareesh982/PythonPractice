# You are given a string and your task is to swap cases. In other words, convert all
# lowercase letters to uppercase letters and vice versa.


def swap_case(s):
    swap = ''
    for i in s:
        if i.islower():
            swap += i.upper()
        elif i.isupper():
            swap += i.lower()
        else:
            swap += i
    return swap

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)


#*******************SAMPLE_INPUT*******************

# HackerRank.com presents "Pythonist 2".

#***************OUTPUT*****************

# hACKERrANK.COM PRESENTS "pYTHONIST 2".
