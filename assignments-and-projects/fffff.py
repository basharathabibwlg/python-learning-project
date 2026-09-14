def staff_info():
    date = input("Enter Date: ")
    staff_id = input("Enter Staff ID: ")
    staff_name = input("Enter Staff Name: ")

    # Generate a unique requisition ID
    counter = 1
    requisition_id = 10000 + counter

    return date, staff_id, staff_name, requisition_id


# Call the function
date, staff_id, staff_name, requisition_id = staff_info()

print("\nPrinting Staff Information:")
print("Date:", date)
print("Staff ID:", staff_id)
print("Staff Name:", staff_name)
print("Requisition ID:", requisition_id)


task-2

def requisitions_total():
    # Call staff_info() from Task 1
    date, staff_id, staff_name, requisition_id = staff_info()

    total = 0

    print("\nEnter requisition items.")
    print("Type 'done' when finished.")

    while True:
        item = input("Enter item name: ")

        if item.lower() == "done":
            break

        price = float(input("Enter price: $"))
        total += price

    return total


# Call the function
total = requisitions_total()



