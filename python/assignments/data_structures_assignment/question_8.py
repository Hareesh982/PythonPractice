# Question-8
# Write a program to check if all the brackets are closed in a given code snippet.



def flower_brackets(snippet):
    if '{' in snippet or '}' in snippet:
        if snippet.count('{') == snippet.count('}'):
            return "Balanced"
        else:
            return "Not balanced"
    else:
        return "Not balanced"

def square_brackets(snippet):
    if ('[' in snippet or ']' in snippet) and ('{' not in snippet) and ('}' not in snippet):
        if snippet.count('[') == snippet.count(']'):
            return "Balanced"
        else:
            return "Not balanced"
    elif '[' in snippet or ']' in snippet:
        if snippet.count('[') == snippet.count(']'):
            return flower_brackets(snippet)
        else:
            return "Not balanced"
    else:
        return flower_brackets(snippet)

def open_brackets(snippet):
    a = '('
    b = ')'
    if (a in snippet or b in snippet) and ('[' not in snippet) and (']' not in snippet) and ('{' not in snippet) and ('}' not in snippet):
        if snippet.count(a) == snippet.count(b):
            return "Balanced"
        else:
            return "Not balanced"
    elif a in snippet or b in snippet:
        if snippet.count(a) == snippet.count(b):
            return square_brackets(snippet)
        else:
            return "Not balanced"
    else:
        return square_brackets(snippet)

if __name__ == '__main__':
    snippet = input("Enter the code snippet : ")
    res = open_brackets(snippet)
    print(res)



