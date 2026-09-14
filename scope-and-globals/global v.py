# Author: Sana Alyaseri
# Class: Software Development
# Example 5: Using global variable to share data between functions

total_sum = 0

def add_to_sum(num):
    global total_sum
    total_sum += num
    print(f"Total inside function: {total_sum}")

def display_sum():
    print(f"Total sum: {total_sum}")


# Call the function
add_to_sum(5)
add_to_sum(10)
add_to_sum(20)
display_sum()
