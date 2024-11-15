# Simple calculator that greets the user and adds two numbers
def main():
    # Greet the user
    name = input("Enter your name: ")
    print(f"Hello, {name}! Let's add two numbers.")

    # Get two numbers from the user
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        return

    # Calculate the sum
    result = num1 + num2

    # Display the result
    print(f"{name}, the sum of {num1} and {num2} is {result}.")

if __name__ == "__main__":
    main()
