# Author: Sana Alyaseri
# Class: Software Development
# Task 4: Functions where one function calls another

# Function to add two numbers
def add(a, b):
    return a + b


# Function to multiply two numbers
def multiply(a, b):
    return a * b


# Function that calls add() and then multiply()
def add_and_multiply(a, b, c):
    total = add(a, b)
    result = multiply(total, c)
    return result


# Call the function
answer = add_and_multiply(2, 3, 4)

print("Result:", answer)