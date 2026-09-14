# Global counter for requisition ID
requisition_counter = 1


# Task 1: Staff information
def staff_info():
    global requisition_counter

    date = input("Enter the registration date (19/08/26
    ): ")
    staff_id = input("Enter staff ID: ")
    staff_name = input("Enter staff name: ")

    # Generate requisition ID
    requisition_id = 10000 + requisition_counter
    requisition_counter += 1

    return date, staff_id, staff_name, requisition_id


# Task 2: Calculate requisition total
def requisitions_total():
    # Call staff_info
    date, staff_id, staff_name, requisition_id = staff_info()

    total = 0

    number_of_items = int(input("Enter the number of requisition items: "))

    for i in range(number_of_items):
        item_name = input("Enter item name: ")
        price = float(input("Enter item price: $"))

        total += price

    return date, staff_id, staff_name, requisition_id, total


# Task 3: Requisition approval
def requisition_approval():
    # Call requisitions_total
    date, staff_id, staff_name, requisition_id, total = requisitions_total()

    # Default status
    status = "Pending"
    approval_reference_number = "Not Available"

    # Automatically approve if total is less than $500
    if total < 500:
        status = "Approved"

        # Staff ID + last three characters of requisition ID
        approval_reference_number = staff_id + str(requisition_id)[-3:]

    return date, requisition_id, staff_id, staff_name, total, status, approval_reference_number


# Task 4: Display requisition
def display_requisitions():
    date, requisition_id, staff_id, staff_name, total, status, approval_reference_number = requisition_approval()

    print("\nPrinting Requisitions:")
    print("Date:", date)
    print("Requisition ID:", requisition_id)
    print("Staff ID:", staff_id)
    print("Staff Name:", staff_name)
    print(f"Total: ${total:.0f}")
    print("Status:", status)
    print("Approval Reference Number:", approval_reference_number)


# Call the display function
display_requisitions()