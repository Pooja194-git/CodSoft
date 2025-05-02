# simple_calculator.py

def get_number(prompt):
    """Prompts the user for a number and handles invalid input."""
    while True:
        try:
            # Attempt to convert the user's input to a floating-point number
            number_str = input(prompt)
            number_flt = float(number_str)
            return number_flt
        except ValueError:
            # If conversion fails, inform the user and loop again
            print("Invalid input. Please enter a valid number.")

def get_operation():
    """Prompts the user for an operation and validates it."""
    valid_operations = ['+', '-', '*', '/']
    while True:
        operation = input("Choose an operation (+, -, *, /): ")
        if operation in valid_operations:
            return operation
        else:
            print("Invalid operation. Please choose from +, -, *, /.")

# --- Main Program ---
print("--- Simple Calculator ---")

# 1. Get Inputs
num1 = get_number("Enter the first number: ")
num2 = get_number("Enter the second number: ")
operation = get_operation()

# 2. Perform Calculation
result = None  # Initialize result to None

if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    # Handle division by zero specifically
    if num2 == 0:
        print("\nError: Cannot divide by zero.")
    else:
        result = num1 / num2
# Note: An 'else' isn't strictly needed here because get_operation() ensures a valid operation

# 3. Display Result
if result is not None:  # Only display if a valid calculation occurred
    # Using an f-string for formatted output
    print(f"\nResult: {num1} {operation} {num2} = {result}")

print("\n--- Calculation Complete ---")