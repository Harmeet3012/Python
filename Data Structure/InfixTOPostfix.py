def toPostfix(inf):
    # push '(' to the top of the stack
    stack=['(']

    # converting inf i.e. infix expression to a list format
    i=0
    infix = []
    while i<len(inf):
        if inf[i] in ('(',')','+','-','*','/','^'):
            infix.append(inf[i])
            i+=1
        else:
            j=i
            num = ""
            while j<len(inf) and inf[j] not in ('(',')','+','-','*','/','^'):
                num+=inf[j]
                j+=1
            infix.append(num)
            i=j

    # adding ')' to the end of postfix expression
    print("INFIX ",infix)
    infix.append(')')
    # Check for converted infix expression E.g. - a+b should become a + b )
    #i=0
    #while i<len(infix):
    #    print(infix[i])
    #    i+=1

    expr = ['(',')','^','*','/','+','-']
    postfix= []
    i=0
    while i<len(infix):

        # if it is an operand
        if infix[i] not in expr:
            postfix.append(infix[i])

        # if ( is encountered
        elif infix[i] == '(':
            stack.insert(0,'(')

        # if operator is encountered
        elif infix[i] in ('^','*','/','+','-'):
            # print("Stack ",stack)
            # if + or - operator is encountered, then pop + - * / ^
            if infix[i] in ('+','-'):
                while stack[0] in ('^','*','/','+','-'):
                    temp = stack[0]
                    stack.pop(0)
                    postfix.append(temp)
                stack.insert(0,infix[i])

            # if * or / operator is encountered, then pop * / ^
            elif infix[i] in ['*','/']:
                while stack[0] in ('^','*','/'):
                    temp = stack[0]
                    stack.pop(0)
                    postfix.append(temp)
                stack.insert(0,infix[i])

            # if ^ operator is encountered, then pop ^
            elif infix[i] == '^':
                while stack[0] == '^':
                    temp = stack[0]
                    stack.pop(0)
                    postfix.append(temp)
                stack.insert(0,infix[i])

        # if ) is encountered then pop all the opeartors until ( is encountered
        elif infix[i] == ')':
            #print("before ) ",stack)
            while stack[0] != '(':
                temp = stack[0]
                stack.pop(0)
                postfix.append(temp)
            if stack[0] == '(':
                stack.pop(0)
            #print("after )",stack)
        i+=1

    # print postfix
    print("POSTFIX",postfix)

    # convert postfix(list) to string
    postfix_expr=""
    for e in postfix:
        postfix_expr=postfix_expr+e+" "
    print("POSTFIX EXPRESSION",postfix_expr)
    return postfix


if __name__=="__main__":
    infix = input("Enter Exp")
    postfix=toPostfix(infix)

