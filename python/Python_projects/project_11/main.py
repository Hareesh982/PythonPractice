import re
if __name__ == '__main__':
    text = input("Enter the text : ")
    pattern = input("Enter the pattern : ")
    c = re.compile(pattern)
    res = c.findall(text)
    print(res)
