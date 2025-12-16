# Restaurant Menu Order System

menu = {
    1: ("Veg Burger", 80),
    2: ("Paneer Pizza", 200),
    3: ("Chicken Biryani", 250),
    4: ("Fried Rice", 150),
    5: ("Tea", 30),
    6: ("Coffee", 50)
}

order = {}
total_cost = 0

print("====== WELCOME TO RESTAURANT ======\n")
print("MENU CARD")

for item_no, item in menu.items():
    print(f"{item_no}. {item[0]} - ₹{item[1]}")

while True:
    choice = int(input("\nEnter item number to order: "))

    if choice in menu:
        qty = int(input("Enter quantity: "))

        item_name = menu[choice][0]
        item_price = menu[choice][1]

        if item_name in order:
            order[item_name]["qty"] += qty
            order[item_name]["price"] += item_price * qty
        else:
            order[item_name] = {
                "qty": qty,
                "price": item_price * qty
            }

        print(f"{item_name} added to cart.")

    else:
        print("Invalid item number!")

    more = input("Do you want to order more? (yes/no): ").lower()
    if more != "yes":
        break

print("\nYOUR ORDER")

for item, details in order.items():
    print(f"{item} | Quantity: {details['qty']} | Price: ₹{details['price']}")
    total_cost += details["price"]

print("\nTotal Amount to Pay: ₹", total_cost)
print("\nThank you! Visit Again")
