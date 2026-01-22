# ===============================
# Billing System
# ===============================

TAX_RATE = 0.14
RECEIPTS_FILE = r"C:\Users\user\.vscode\Pharmacy\all_receipts.txt"
MEDICINES_FILE = r"C:\Users\user\.vscode\Pharmacy\medicines.txt"


# ===============================
# Load inventory from file
# name,price,quantity,expiry
# ===============================
def load_inventory_from_file():
    inventory = {}

    with open(MEDICINES_FILE, "r") as file:
        for line in file:
            line = line.strip()
            if line == "":
                continue

            name, price, qty, expiry = line.split(",")

            inventory[name.strip()] = {
                "price": float(price),
                "qty": int(qty),
                "expiry": expiry
            }

    return inventory


# ===============================
# Get client name
# ===============================
def get_client_name():
    print("Welcome to Zewail Pharmacy")
    client_name = input("Enter Client Name: ").strip()
    return client_name


# ===============================
# Add items to cart
# ===============================
def add_to_cart(inventory):
    cart = []

    print("\n" + "=" * 62)
    print("Available Medicines")
    print("=" * 62)
    print(f"{'Name':<15}{'Price':>10}{'Expiry':>11}")
    print("-" * 62)

    for name, data in inventory.items():
        print(
            f"{name:<15}"
            f"{data['price']:>10.2f}"
            f"{data['expiry']:>15}"
        )

    print("=" * 62)

    while True:
        item_name = input("\nEnter medicine name (Enter to finish): ").strip()
        if item_name == "":
            break

        if item_name not in inventory:
            print("❌ Medicine not found")
            continue

        while True:
            qty = input("Enter quantity: ")
            if qty.isdigit() and 0 < int(qty) <= inventory[item_name]["qty"]:
                qty = int(qty)
                break
            else:
                print("❌ Invalid quantity")

        cart.append({
            "name": item_name,
            "price": inventory[item_name]["price"],
            "qty": qty
        })

        inventory[item_name]["qty"] -= qty
        print("✅ Added to cart")

    return cart


# ===============================
# Calculate prices
# ===============================
def calculate_total_price(cart):
    subtotal = 0

    for item in cart:
        subtotal += item["price"] * item["qty"]

    tax_amount = subtotal * TAX_RATE
    total = subtotal + tax_amount

    return {
        "subtotal": subtotal,
        "tax": tax_amount,
        "total": total
    }


# ===============================
# Print receipt
# ===============================
def print_receipt(client_name, cart, price_info):
    print("\n" + "=" * 40)
    print("        Zewail Pharmacy Receipt")
    print("=" * 40)
    print(f"Client: {client_name}\n")

    # Header
    print(f"{'Item':<15}{'Qty':>5}{'Price':>10}")
    print("-" * 40)

    # Items
    for item in cart:
        total_price = item["price"] * item["qty"]
        print(f"{item['name']:<15}{item['qty']:>5}{total_price:>10.2f}")

    print("-" * 40)
    print(f"{'Subtotal':<20}{price_info['subtotal']:>20.2f}")
    print(f"{'Tax (14%)':<20}{price_info['tax']:>20.2f}")
    print("=" * 40)
    print(f"{'TOTAL':<20}{price_info['total']:>20.2f}")
    print("=" * 40)
    print(" Thank you for visiting Zewail Pharmacy!")
    print("=" * 40 + "\n")


# ===============================
# Save receipt to file
# ===============================
def save_receipt_file(client_name, cart, price_info):
    with open(RECEIPTS_FILE, "a", encoding="utf-8") as file:
        file.write("\n" + "=" * 40 + "\n")
        file.write("        Zewail Pharmacy Receipt\n")
        file.write("=" * 40 + "\n")
        file.write(f"Client: {client_name}\n\n")

        # Header
        file.write(f"{'Item':<15}{'Qty':>5}{'Price':>10}\n")
        file.write("-" * 40 + "\n")

        # Items
        for item in cart:
            total_price = item["price"] * item["qty"]
            file.write(
                f"{item['name']:<15}{item['qty']:>5}{total_price:>10.2f}\n"
            )

        file.write("-" * 40 + "\n")
        file.write(f"{'Subtotal':<20}{price_info['subtotal']:>20.2f}\n")
        file.write(f"{'Tax (14%)':<20}{price_info['tax']:>20.2f}\n")
        file.write("=" * 40 + "\n")
        file.write(f"{'TOTAL':<20}{price_info['total']:>20.2f}\n")
        file.write("=" * 40 + "\n")
        file.write(" Thank you for visiting Zewail Pharmacy!\n")
        file.write("=" * 40 + "\n")

def save_inventory_to_file(inventory):
    with open(MEDICINES_FILE, "w", encoding="utf-8") as file:
        for name, data in inventory.items():
            file.write(
                f"{name},{data['price']},{data['qty']},{data['expiry']}\n"
            )
