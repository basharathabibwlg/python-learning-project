# initialize the requisition counter
requisition-counter = 10000

def staff-info():
    global requisition-counter

    # collect staff information
    date = input("enter the date:")
    staff-id = input("enter the staff id:")
    staff-name = input("enter the staff name:")

    # Generate the unique requisition id
    requisition-counter += 1
    requisition-id = requisition-counter

    # Return all information
    return date, staff-id, staff-name, requisition-id


# call the function
date, staff-id, staff-name, requisition-id = staff-info()

# display the staff information
print("\nprinting staff information:")
print("date:", date)
print("staff id:", staff-id )
print("staff name:", staff-name)
print("requisition id:", requisition-id)