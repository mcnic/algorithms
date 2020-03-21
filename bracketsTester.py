from stack import Stack


def brackets_tester(str):
    stack = Stack()
    try:
        for c in str:
            if c == '(':
                stack.push(c)
            else:
                if c == ')':
                    stack.pop()
                else:
                    raise IndexError('wrong symbols')
    except IndexError:
        return False

    if stack.size() == 0:
        return True
    else:
        return False
