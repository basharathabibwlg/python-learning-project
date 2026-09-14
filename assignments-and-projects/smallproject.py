# initialize a global counter
registration_counter = 50001

def student_registration():
    global registration_counter

    # collect student information
    date = input("Enter the registration date (dd/mm/yyyy): ")
    student_id = input("Enter the student ID: ")
    student_name = input("Enter the student name: ")
    course_name = input("Enter the course name: ")

    # generate the registration ID
    registration_id = registration_counter
    registration_counter += 1

    # display information
    print("\nPrinting Student Registration Information:")
    print(f"Date: {date}")
    print(f"Student ID: {student_id}")
    print(f"Student Name: {student_name}")
    print(f"Course Name: {course_name}")
    print(f"Registration ID: {registration_id}")


# call the function
student_registration()




# Initialize a global counter
registration_counter = 5000

def student_registration():
    global registration_counter

    # Generate the registration ID using the counter value
    registration_id = registration_counter
    registration_counter += 1  # Increment the counter for the next registration

    # Collect information from the user
    date = input("Enter the registration date (dd/mm/yyyy): ")
    student_id = input("Enter the student ID: ")
    student_name = input("Enter the student name: ")
    course_name = input("Enter the course name: ")

    # Return the collected information and registration ID
    return date, student_id, student_name, course_name, registration_id


# Call the function and get the data
date, student_id, student_name, course_name, registration_id = student_registration()

# Print the information outside the function
print("\nPrinting Student Registration Information:")
print(f"Date: {date}")
print(f"Student ID: {student_id}")
print(f"Student Name: {student_name}")
print(f"Course Name: {course_name}")
print(f"Registration ID: {registration_id}")    