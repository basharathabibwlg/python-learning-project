#Counter

counter = 0
def staff_info():
    global counter

    print("\nPrint the information:\n")

    date = input("Enter Date (DD/MM/YYYY): ")
    staff_id = input("Enter staff ID: ")
    staff_name = input("Enter staff Name: ")

    counter = counter + 1
    requistion_id = 10000 + counter

    print("\nDate:",date)
    print("staff ID:", staff_id)
    print("staff Name:", staff_name)
    print("Requistion ID:", requistion_id)

    return date, staff_id, staff_name, requistion_id


def requistions_total():
    date, staff_id, staff_name, requistion_id = staff_info()

    total = 0

    print("\nEnter requistion items.")
    print("Type 'done' when you have finished.\n")

    while True:
        item_name = input("Enter item name: ")

        if item_name.lower() == "done":
            break
        price = float(input("Enter item price: $"))
        total = total + price

    print("\nTotal : $" + str(total))

    return date, staff_id, staff_name, requistion_id, total

def requistion_approval():
    date, staff_id, staff_name, requistion_id,total = requistions_total()

    status = "pending"
    approval_refrence = ""

    if total < 500:
        status = "Approved"

        approval_refrence = staff_id + str(requistion_id)[-3:]

    print("\nTotal: $" + str(total))
    print("Status:", status)

    if status == "Approved":
        print("Approval Refrence Number:", approval_refrence)

    return date, staff_id, staff_name, requistion_id, total, status, approval_refrence

def display_requistions():

    date, staff_id, staff_name, requistion_id, total, status, approval_refrence = requistion_approval()

    print("\nPrinting Requisitions:\n")

    print("Date:",date)
    print("Requistion ID:", requistion_id)
    print("Staff ID", staff_id)
    print("Staff Name:", staff_name)
    print("Total: $" + str(total))
    print("status:",status)

    if status == "Approved":
        print("Approval Reference Number :", approval_refrence)

display_requistions()
