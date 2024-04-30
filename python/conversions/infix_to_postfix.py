
def infix_to_postfix(infix):
    operators = ['(',')','^','*','/','+','-']
    priority = {
        '+' : 1,
        '-' : 1,
        '/' : 2,
        '*' : 2,
        '^' : 3
    }
    stack = []
    postfix = ''
    
    for character in infix:
        if character not in operators:
            postfix = postfix + character
        elif character == '(':
            stack.append('(')
        elif character == ')':
            while stack and stack[-1] != '(':
                postfix += stack.pop()
            stack.pop()
        else:
            while stack and stack[-1] != '(' and priority[character] <= priority[stack[-1]]:
                postfix += stack.pop()
            stack.append(character)
    while stack:
        postfix += stack.pop()
    return postfix

if __name__ == '__main__':
    infix = input("Enter infix expression : ")
    postfix = infix_to_postfix(infix)
    print("Infix : ",infix)
    print("Postfix notation : ",postfix)
