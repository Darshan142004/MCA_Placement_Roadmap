stack = []

while True:
    print("\n--- STACK OPERATIONS ---")
    print("1. Push (Add)")
    print("2. Pop (Remove)")
    print("3. Display Stack")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        item = input("Enter the value to push: ")
        stack.append(item)
        print(f"{item} added to stack.")


    elif choice == '2':
        if len(stack) == 0:
            print("Stack is empty! Nothing to pop.")
        else:
            removed = stack.pop()
            print(f"Popped element: {removed}")

    elif choice == '3':
        print(f"Current Stack: {stack}")

    elif choice == '4':
        print("Exiting program.")
        break

    else:
        print("Invalid choice, please try again.")
