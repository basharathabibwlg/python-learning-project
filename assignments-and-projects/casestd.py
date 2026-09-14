# Initialize the item ID counter
item_counter = 1000

def add_inventory_item():
    global item_counter

    # Ask the staff member to enter item details
    item_name = input("Enter item name: ")
    quantity = int(input("Enter quantity: "))
    price_per_item = float(input("Enter price per item: $"))

    # Generate a unique Item ID
    item_id = item_counter
    item_counter += 1

    # Return all information
    return item_name, item_id, quantity, price_per_item


# Call the function
item_name, item_id, quantity, price_per_item = add_inventory_item()

# Display the inventory item
print("\nInventory Item:")
print("Item Name:", item_name)
print("Item ID:", item_id)
print("Quantity:", quantity)
print("Price per Item: $", price_per_item)