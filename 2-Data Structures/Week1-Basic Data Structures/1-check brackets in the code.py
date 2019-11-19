# Use Python3


from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            bracket = Bracket(next, i)
            opening_brackets_stack.append(bracket)
        if next in ")]}":
            if not opening_brackets_stack:
                return i + 1
            top = opening_brackets_stack.pop()
            if (top.char == '(' and next != ')') or (top.char == '[' and next != ']') or (top.char == '{' and next != '}'):
                return i + 1
    if opening_brackets_stack:
        return opening_brackets_stack[0].position + 1
    return "Success"


def main():
    text = input()
    mismatch = find_mismatch(text)
    print(mismatch)


if __name__ == "__main__":
    main()
