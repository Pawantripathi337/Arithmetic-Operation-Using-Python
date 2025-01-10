def calculator():
    print("Welcome to the Calculator Program!")
    print("Please select the operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    try:
        # Input operation choice
        choice = int(input("Enter the number corresponding to the operation (1/2/3/4): "))

        if choice not in [1, 2, 3, 4]:
            print("Invalid choice! Please select a valid operation.")
            return

        # Input two numbers
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # Perform the chosen operation
        if choice == 1:
            result = num1 + num2
            print(f"The result of addition is: {result}")
        elif choice == 2:
            result = num1 - num2
            print(f"The result of subtraction is: {result}")
        elif choice == 3:
            result = num1 * num2
            print(f"The result of multiplication is: {result}")
        elif choice == 4:
            if num2 == 0:
                print("Error! Division by zero is not allowed.")
            else:
                result = num1 / num2
                print(f"The result of division is: {result}")

    except ValueError:
        print("Invalid input! Please enter numeric values for numbers and a valid option for operations.")

# Run the calculator function
calculator()