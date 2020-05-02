from DataStructure.InfixTOPostfix import *

def solvePostfix(postfix):

    #print(postfix)
    i=0
    stack = []
    expr = ['*','/','+','-','^']
    while i<len(postfix):
        if postfix[i] not in expr:
            stack.insert(0,postfix[i])
            #print(stack)
        elif postfix[i] in expr:
            if postfix[i] == '+':
                top = int(stack[1]) + int(stack[0])
            elif postfix[i] == '-':
                top = int(stack[1]) - int(stack[0])
            elif postfix[i] == '*':
                top = int(stack[1]) * int(stack[0])
            elif postfix[i] == '/':
                top = int(stack[1]) / int(stack[0])
            elif postfix[i] == '^':
                top = pow(int(stack[1]),int(stack[0]))
            stack.pop(0)
            stack.pop(0)
            stack.insert(0, top)
            #print(stack)
        i+=1

    print("Result :",stack[0])


infix = input("Enter Exp")
postfix = toPostfix(infix)
solvePostfix(postfix)
