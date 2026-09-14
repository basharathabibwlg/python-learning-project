# initiazlize the requisition counter
requisition-counter = 10000


def staff-info():
    global requisition-counter

    date = input("enter the date (dd/mm/yy):")
    staff-id = input("enter the staff id:")
    staff-name = input("enter the staff name:")

    # generate requisition id
    requisition-counter += 1
    requisition-id = requisition-counter

    return date, staff-id, staff-name, requisition-id


def requisition-total():
    # call staff information
    date, staff-id, staff-name,requisition-id = staff-info()

    # start total at 0
    total = 0

    # ask how many items the staff members wants to enter
    number-of-items = int(input("enter the number requisition item":))

    # eneter each item and its price 
    for i in range(number-of-item):
        item-name = input("enter item name:")
        price = float(input("enter price:$"))

        total = total + price 

    # return the total 
    return total

# call the requisition-total function
total = requisition-total()

# display the total
print("total requisition valu: ${;.of}".format(total))