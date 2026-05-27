def stack_push(stack, item):
    new_stack = []
    for element in stack:
        new_stack.append(element)
    new_stack.append(item)
    return new_stack

def stack_pop(stack):
    if len(stack) == 0:
        return None, []
    new_stack = []
    for i in range(len(stack) - 1):
        new_stack.append(stack[i])
    return stack[-1], new_stack

def stack_peek(stack):
    if len(stack) == 0:
        return None
    return stack[len(stack) - 1]

def is_balanced(text):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    for char in text:
        if char in '([{':
            stack = stack_push(stack, char)
        elif char in ')]}':
            top, stack = stack_pop(stack)
            if top != pairs[char]:
                return False
    return len(stack) == 0

print(is_balanced("({[]})"))
print(is_balanced("({[})"))
print(stack_peek([1, 2, 3]))
