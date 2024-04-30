from math import e


if __name__ == "__main__":
    i = 0
    string = str(input("Enter the string : "))
    character = str(input("Enter a character : "))
    if len(character) == 1:
        if character in string:
            i = string.index(character)
            new_string = string[:i] + string[i+1:]
            print(new_string)
        else:
            print("Character not in string")
    else:
        print("Please enter a valid input")