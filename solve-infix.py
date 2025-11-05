def infixToPostfix(expression):
        # Take an expression in the form of a string, where tokens are separated by spaces.
        # This way we can deal with multidigit numbers without writing a tokenizer yet.
        tokens = expression.split()

        # output will be a postfix expression in a list for now.
        output = []
        opStack = []
        operators = {"+":1, "-":1, "*":2, "/":2}

        for token in tokens:
                print(f"token: {token}")
                if token.isnumeric():
                        output.append(token)
                else:
                        # token is an operator
                        while opStack and operators[opStack[-1]] <= operators[token]:
                                # While there is something on the stack and the precedence of the operator on top of the stack
                                # is less than the operator we are currently looking at, pop from the stack onto the output.
                                output.append(opStack.pop())
                        # always put the current operator on the stack.
                        opStack.append(token)

        while opStack:
                output.append(opStack.pop())
        return output


a = infixToPostfix("1 + 2")
print(a)

