# If Condition Examples

# Example 1: Simple if statement
age = 18
if age >= 18:
    print("You are an adult")

# Example 2: if-else statement
score = 45
if score >= 50:
    print("You passed")
else:
    print("You failed")

# Example 3: if-elif-else statement
marks = 75
if marks >= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: F")

# Example 4: Multiple conditions with and operator
temperature = 25
humidity = 60
if temperature > 20 and humidity < 70:
    print("Weather is pleasant")

# Example 5: Multiple conditions with or operator
day = "Saturday"
if day == "Saturday" or day == "Sunday":
    print("It's weekend!")

# Example 6: Nested if statements
num = 10
if num > 0:
    if num % 2 == 0:
        print("Positive and even number")
    else:
        print("Positive and odd number")
