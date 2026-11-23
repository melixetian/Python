#!/usr/bin/env python3

"""
Программа проверяющая правильность расстановки скобок в строке

"""


def brackets(brac):
    stack = []
    for el in brac:
        if el in ["[", "(", "{", "<"]:
            stack.append(el)
        elif el in ["]", ")", "}", ">"]:
            if len(stack) > 0:
                top = stack.pop()
                if top + el not in ["[]", "()", "{}", "<>"]:
                    return False
            else:
                return False

    return len(stack) == 0


if brackets(input()):
    print("Success")
else:
    print("Fail")
