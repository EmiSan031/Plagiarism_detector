def stack_push(stack, item):
    return stack + [item]

def stack_pop(stack):
    return (None, []) if not stack else (stack[-1], stack[:-1])

def stack_peek(stack):
    return stack[-1] if stack else None

def is_balanced(text):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    for char in text:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack or stack.pop() != pairs[char]:
                return False
    return not stack

print(is_balanced("({[]})"))
print(is_balanced("({[})"))
print(stack_peek([1, 2, 3]))
