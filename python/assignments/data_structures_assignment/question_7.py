# Question-7
# Write a program to convert prefix expression to infix expression.



def prefix_to_infix(expression):
    stack = []
    operators = ['+', '-', '*', '/', '^']
    for i in reversed(expression):
        if i not in operators:
            stack.append(i)
        else:
            j = stack.pop()
            k = stack.pop()
            stack.append('(' + j + i + k + ')')
    return stack.pop()


prefix = input("Enter the prefix expression : ")
infix = prefix_to_infix(prefix)
print("Infix expression : ", infix)



#***********************OUTPUT**********************

# Enter the prefix expression: +a/*bc-de
# Infix expression:  (a+((b*c)/(d-e)))
