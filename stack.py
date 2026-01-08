# Initialize an empty list to serve as the stack
stack = []

# 1. PUSH: Adding elements to the stack
stack.append("A")
stack.append("B")
stack.append("C")
print(f"Stack after pushes: {stack}")

# 2. PEEK: Looking at the top element without removing it
if stack:
    top_element = stack[-1]
    print(f"Top element (Peek): {top_element}")

# 3. POP: Removing the top element
removed_item = stack.pop()
print(f"Popped element: {removed_item}")
print(f"Stack after pop: {stack}")

# 4. IS EMPTY: Checking if stack is empty
is_empty = len(stack) == 0
print(f"Is stack empty? {is_empty}")
