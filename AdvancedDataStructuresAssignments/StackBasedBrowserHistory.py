back_stack = []
forward_stack = []

current = "A"
back_stack.append(current)

current = "B"
back_stack.append(current)

current = "C"
back_stack.append(current)

# Back
forward_stack.append(back_stack.pop())
current = back_stack[-1]

# Forward
back_stack.append(forward_stack.pop())
current = back_stack[-1]

print(f"Current Page: {current}")