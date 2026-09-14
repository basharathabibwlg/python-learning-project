# Simple Hello World Program
# This is a basic Python program to demonstrate variables and print statements

def greet(name):
    """
    Function to greet a person
    """
    print(f"Hello, {name}! Welcome to Python Learning Project")

def add_numbers(num1, num2):
    """
    Function to add two numbers
    """
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
    return result

def main():
    """
    Main function - Entry point of the program
    """
    print("=== Welcome to Python Learning ===\n")
    
    # Call greet function
    greet("Basharat")
    
    print("\n--- Simple Calculator ---")
    # Call add_numbers function
    add_numbers(10, 20)
    add_numbers(5, 15)
    
    print("\n--- Working with Variables ---")
    # Variables
    name = "Python Learner"
    age = 20
    city = "Pakistan"
    
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"City: {city}")
    
    print("\n=== Program Completed ===")

# Entry point of the program
if __name__ == "__main__":
    main()
