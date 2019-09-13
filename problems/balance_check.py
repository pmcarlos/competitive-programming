def balance_check(s):
    """Check wether a string is balanced by open - close brackets."""
    if len(s) % 2 != 0:
        return False
    opening = set("({[")
    matches = (("(", ")"), ("[", "]"), ("{", "}"))
    stack = []  # Use stack to check LIFO

    for paren in s:
        if paren in opening:
            stack.append(paren)
        else:
            if len(stack) == 0:
                return False

            last_open = stack.pop()
            if (last_open, paren) not in matches:
                raise Exception("String is not balanced")

    return len(stack) == 0
