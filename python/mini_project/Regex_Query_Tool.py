import re

text_string = input("Enter a text string: ")
regex_pattern = input("Enter a regex pattern: ")

try:
    regex = re.compile(regex_pattern)
except re.error as e:
    print("Error in regex pattern: ", e)
    exit()

matches = regex.findall(text_string)

if len(matches) > 0:
    print("Matches found:")
    for match in matches:
        print(match)
else:
    print("No matches found.")
