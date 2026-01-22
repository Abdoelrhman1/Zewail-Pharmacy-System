import user_management as user_sys
import medicine_management as medicine_management  
import billing as bil

def login_terminal():
    print("Welcome to Zewail Pharmacy")
    print("=== Login ===")
    username = input("Username: ").strip().lower()
    password = input("Password: ")

    user = user_sys.authenticate_user(username, password)
    if user:
        print(f"\nWelcome {user['username']} ({user['role']})")
        main_menu_terminal(user)
    else:
        print("❌ Invalid login")


def main_menu_terminal(user):
    while True:
        print("\n=== Main Menu ===")
        print("1. Medicine Management")
        print("2. Billing System")
        if user["role"] == "admin":
            print("3. Admin Controls")
        print("0. Logout")

        choice = input("Choose: ")

        if choice == "1":
            medicine_menu_terminal()
        elif choice == "2":
            billing_terminal()
        elif choice == "3" and user["role"] == "admin":
            admin_menu_terminal()
        elif choice == "0":
            break
        else:
            print("❌ Invalid choice")

def medicine_menu_terminal():
    while True:
        print("\n--- Medicine Menu ---")
        print("1. Add Medicine")
        print("2. Edit Medicine")
        print("3. Low Quantity Alert")
        print("4. Expiration Alert")
        print("0. Back")

        choice = input("Choose: ")

        if choice == "1":
            add_medicine_terminal()
        elif choice == "2":
            edit_medicine_terminal()
        elif choice == "3":
            low_qty_terminal()
        elif choice == "4":
            exp_alert_terminal()
        elif choice == "0":
            break

def add_medicine_terminal():
    name = input("Name: ")
    price = float(input("Price: "))
    qty = int(input("Quantity: "))
    exp = input("Expiration (YYYY-MM-DD): ")

    if medicine_management.add_medicine(name, price, qty, exp):
        print("✅ Medicine added")
    else:
        print("❌ Medicine already exists")

def edit_medicine_terminal():
    name = input("Medicine name: ")

    price = input("New price (enter to skip): ")
    qty = input("New quantity (enter to skip): ")
    exp = input("New expiration (enter to skip): ")

    price = float(price) if price else None
    qty = int(qty) if qty else None
    exp = exp if exp else None

    if medicine_management.edit_medicine(name, price, qty, exp):
        print("✅ Medicine updated")
    else:
        print("❌ Medicine not found")

def low_qty_terminal():
    meds = medicine_management.check_low_quantity_alert()
    if meds:
        for m in meds:
            print(f"- {m['name']} ({m['qty']})")
    else:
        print("No low quantity medicines")

def exp_alert_terminal():
    meds = medicine_management.check_expiration_alert()
    if meds:
        for m in meds:
            print(f"- {m['name']} | {m['exp']}")
    else:
        print("No expired medicines")

def admin_menu_terminal():
    while True:
        print("\n--- Admin Menu ---")
        print("1. Add User")
        print("2. Remove User")
        print("0. Back")

        choice = input("Choose: ")

        if choice == "1":
            user_sys.add_user()
        elif choice == "2":
            username = input("Username to remove: ")
            user_sys.remove_user(username.lower())
        elif choice == "0":
            break


def billing_terminal():
    try:
        inventory = bil.load_inventory_from_file()
    except FileNotFoundError:
        print("❌ Medicines file not found")
        return

    if not inventory:
        print("❌ No medicines available")
        return

    client_name = bil.get_client_name()
    cart = bil.add_to_cart(inventory)

    if not cart:
        print("❌ No items purchased")
        return
    price_info = bil.calculate_total_price(cart)
    bil.print_receipt(client_name, cart, price_info)
    bil.save_receipt_file(client_name, cart, price_info)
    bil.save_inventory_to_file(inventory)


if __name__ == "__main__":
    login_terminal()