items = {"1": ("Water", 20), "2": ("Soda", 25), "3": ("Chips", 30)}

choice = input("Select item (1-3): ")

if choice in items:
    payment = float(input("Enter payment: "))
    name, price = items[choice]
    print(f"Item: {name}")

    if payment < price:
        print("Insufficient payment")
    else:
        print(f"Change: {payment - price}")
else:
    print("Invalid selection")
