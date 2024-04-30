#Question-6
#Read about infix, prefix, and postfix expressions. Write a program to convert postfix to prefix expression.



def postfix_to_prefix(expression):
    stack = []
    operators = ['+', '-', '*', '/', '^']
    for i in expression:
        if i not in operators:
            stack.append(i)
        else:
            j = stack.pop()
            k = stack.pop()
            stack.append(i + k + j)
    return stack.pop()

postfix = input("Enter the postfix expression : ")
prefix_expression = postfix_to_prefix(postfix)
print("Prefix expression:", prefix_expression)



#*********************OUTPUT********************

# Enter the postfix expression: abc*de-/+
# Prefix expression: +a/*bc-de


