menu = {
    "momo": 150,
    "chowmein": 120,
    "pizza": 350,
    "burger": 200,
    "fried rice": 180,
    "thukpa": 160,
    "sandwich": 130,
    "coffee": 100
}

order = []
TAX_RATE = 0.13


def display_menu():
    print("\n--- Restaurant Menu ---")

    for item, price in menu.items():
        print(item.title(), "- Rs.", price)


def add_item(item, quantity):
    price = menu[item]

    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero.")

    order.append({
        "item": item,
        "quantity": quantity,
        "price": price
    })

    print(item.title(), "added to order.")


def calculate_bill():
    subtotal = sum(
        item["price"] * item["quantity"]
        for item in order
    )

    tax = subtotal * TAX_RATE
    total = subtotal + tax

    return subtotal, tax, total


def display_order():
    print("\n--- Final Order ---")

    if not order:
        print("No items ordered.")
        return

    for item in order:
        amount = item["price"] * item["quantity"]

        print(
            item["item"].title(),
            "x", item["quantity"],
            "= Rs.", amount
        )

    subtotal, tax, total = calculate_bill()

    print("\nSubtotal: Rs.", round(subtotal, 2))
    print("Tax (13%): Rs.", round(tax, 2))
    print("Final Bill: Rs.", round(total, 2))


while True:
    display_menu()

    food_item = input(
        "\nEnter food item (or 'done' to finish): "
    ).strip().lower()

    if food_item == "done":
        break

    try:
        quantity = int(input("Enter quantity: "))
        add_item(food_item, quantity)

    except KeyError:
        print("Error: Food item is not on the menu.")

    except ValueError as error:
        print("Invalid quantity:", error)

display_order()