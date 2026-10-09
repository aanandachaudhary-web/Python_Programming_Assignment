products = {
    "laptop": {"price": 80000, "quantity": 5},
    "mouse": {"price": 1000, "quantity": 10},
    "keyboard": {"price": 2000, "quantity": 8},
    "monitor": {"price": 15000, "quantity": 4},
    "headphone": {"price": 2500, "quantity": 6},
    "charger": {"price": 1500, "quantity": 7}
}

cart = {}


def add_product(name, quantity):
    product = products[name]

    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero.")

    if quantity > product["quantity"]:
        print("Not enough stock available.")
        return

    cart[name] = cart.get(name, 0) + quantity
    product["quantity"] -= quantity

    print(name, "added to cart successfully.")


def calculate_total():
    total = 0

    for name, quantity in cart.items():
        total += products[name]["price"] * quantity

    return total


def display_cart():

    if not cart:
        print("Your cart is empty.")
        return

    for name, quantity in cart.items():
        price = products[name]["price"]
        print(name, "x", quantity, "=", price * quantity)

    print("Final Bill: Rs.", calculate_total())


while True:

    for name, details in products.items():
        print(name, "- Rs.", details["price"],
              "- Stock:", details["quantity"])

    product_name = input(
        "\nEnter product name (or 'done' to finish): "
    ).strip().lower()

    if product_name == "done":
        break

    try:
        quantity = int(input("Enter quantity: "))
        add_product(product_name, quantity)

    except KeyError:
        print("Error: Product does not exist.")

    except ValueError as error:
        print("Invalid quantity:", error)

display_cart()