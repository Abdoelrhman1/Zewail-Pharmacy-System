from datetime import datetime

MEDICINE_FILE = r"C:\Users\user\.vscode\Pharmacy\medicines.txt"


# ===============================
# Ensure file exists
# ===============================
def ensure_file():
    open(MEDICINE_FILE, "a").close()

# ===============================
# Load medicines
# ===============================
def load_medicines_from_file():
    ensure_file()
    medicines = []

    with open(MEDICINE_FILE, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue

            parts = line.split(",")
            if len(parts) != 4:
                continue

            name, price, qty, exp = parts

            medicines.append({
                "name": name,
                "price": float(price),
                "qty": int(qty),
                "exp": exp
            })

        return medicines


# ===============================
# Save medicines
# ===============================
def save_medicines_to_file(medicines):
    with open(MEDICINE_FILE, "w") as file:
        for m in medicines:
            file.write(f"{m['name']},{m['price']},{m['qty']},{m['exp']}\n")


# ===============================
# Add medicine
# ===============================
def add_medicine(name, price, qty, exp):
    medicines = load_medicines_from_file()

    for m in medicines:
        if m["name"].lower() == name.lower():
            return 0  # already exists

    medicines.append({
        "name": name,
        "price": price,
        "qty": qty,
        "exp": exp
    })

    save_medicines_to_file(medicines)
    return 1


# ===============================
# Search medicine
# ===============================
def search_medicine(name):
    medicines = load_medicines_from_file()

    for m in medicines:
        if m["name"].lower() == name.lower():
            return m

    return None


# ===============================
# Delete medicine
# ===============================
def delete_medicine(name):
    medicines = load_medicines_from_file()
    new_list = [m for m in medicines if m["name"].lower() != name.lower()]

    if len(new_list) == len(medicines):
        return 0  # not found

    save_medicines_to_file(new_list)
    return 1


# ===============================
# Sell medicine
# ===============================
def sell_medicine(name, sold_qty):
    medicines = load_medicines_from_file()

    for m in medicines:
        if m["name"].lower() == name.lower():
            if m["qty"] < sold_qty:
                return None  # insufficient stock

            m["qty"] -= sold_qty
            save_medicines_to_file(medicines)
            return m["price"] * sold_qty

    return None  # medicine not found


# ===============================
# Edit medicine
# ===============================
def edit_medicine(name, new_price=None, new_qty=None, new_exp=None):
    medicines = load_medicines_from_file()

    for m in medicines:
        if m["name"].lower() == name.lower():
            if new_price is not None:
                m["price"] = new_price
            if new_qty is not None:
                m["qty"] = new_qty
            if new_exp is not None:
                m["exp"] = new_exp

            save_medicines_to_file(medicines)
            return 1

    return 0


# ===============================
# Low quantity alert
# ===============================
def check_low_quantity_alert(limit=5):
    medicines = load_medicines_from_file()
    return [m for m in medicines if m["qty"] <= limit]


# ===============================
# Expiration alert
# ===============================
def check_expiration_alert():
    medicines = load_medicines_from_file()
    today = datetime.today()
    expired = []

    for m in medicines:
        exp_date = datetime.strptime(m["exp"], "%Y-%m-%d")
        if today >= exp_date:
            expired.append(m)

    return expired
