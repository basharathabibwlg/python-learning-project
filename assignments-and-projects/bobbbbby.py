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
printing staff information
date:03/04/2024
staff name:john paul
requisition_id:10001


print("\nPrinting Staff Information:")
print("Date:", date)
print("Staff ID:", staff_id)
print("Staff Name:", staff_name)
print("Requisition ID:", requisition_id)