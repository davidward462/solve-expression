import pytest

def infixToPostfix(expression):
        # Take an expression in the form of a string, where tokens are separated by spaces.
        # This way we can deal with multidigit numbers without writing a tokenizer yet.
        tokens = expression.split()

        # output will be a postfix expression in a list for now.
        output = [] # like a queue
        stack = []
        operators = {"+":1, "-":1, "*":2, "/":2}

        for token in tokens:
                print(f"token: {token}")
                if token.isnumeric():
                        output.append(token)
                elif token == '(':
                        # put opening bracket on the stack
                        stack.append(token)
                elif token == ')':
                        # if we get a closing bracket, pop everything from the stack until we get to the opening bracket.
                        while stack and stack[-1] != '(':
                                output.append(stack.pop())
                        # pop the opening bracket
                        stack.pop()
                else:
                        # token is an operator
                        while stack and operators.get(stack[-1], 0) >= operators.get(token, 0):
                                # While there is something on the stack and the precedence of the operator on top of the stack
                                # is less than the operator we are currently looking at, pop from the stack onto the output.
                                output.append(stack.pop())
                        # always put the current operator on the stack.
                        stack.append(token)
                print(output)
                print(stack)

        while stack:
                output.append(stack.pop())

        joined = joinList(output)
        print(joined)
        return joined

def solvePostfix(expression):
        stack = []
        operators = {"+", "-", "*", "/"}
        tokens = expression.split()
        for token in tokens:
                if token.isnumeric():
                        # number
                        stack.append(int(token))
                else:
                        # operator
                        b = stack.pop()
                        a = stack.pop()
                        match token:
                                case "+":
                                        stack.append(a + b)
                                case "-":
                                        stack.append(a - b)
                                case "*":
                                        stack.append(a * b)
                                case "/":
                                        # truncate towards zero
                                        stack.append(int(a / b))
        return stack[-1]

def joinList(l):
        return ' '.join(l)

def solve(expression):
        return solvePostfix(infixToPostfix(expression))

@pytest.mark.parametrize("expression, expected", [
        ("1 + 2", "1 2 +"),
        ("1 + 2 * 3", "1 2 3 * +"),
        ("( 1 + 2 ) * 3", "1 2 + 3 *"),
        ("990 + 10", "990 10 +"),
        ("", ""),
        (" ", ""),
        ("1000", "1000")
        ])

def test_infixToPostfix(expression, expected):
        assert infixToPostfix(expression) == expected


@pytest.mark.parametrize("expr, expt", [
        ("1 2 +", 3)
        ])

def test_solvePostfix(expr, expt):
        assert solvePostfix(expr) == expt


@pytest.mark.parametrize("expression, expected", [
        ("1 + 1", 2)
        ])

def test_solve(expression, expected):
        assert solve(expression) == expected
