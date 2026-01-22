# Add new user
def add_user():
    # ---- Username ----
    while True:
        username = input("Enter your Username: ").strip().lower()

        if len(username) > 0 and not username_exists(username):
            break
        else:
            print("Invalid or existing username")

    # ---- Password ----
    while True:
        password = input("Enter your Password: ")
        if len(password) >= 6:
            break
        else:
            print("Password must be at least 6 characters")

    # ---- Role ----
    while True:
        role = input("Enter role (admin/employee): ").lower().strip()
        if role in ["admin", "employee"]:
            break
        else:
            print("Invalid role")

    # ---- Gender ----
    while True:
        gender = input("Enter your Gender (male/female): ").lower().strip()
        if gender in ["male", "female"]:
            break
        else:
            print("Invalid gender")

    # ---- Age ----
    while True:
        age = input("Enter your Age: ")
        if age.isdigit():
            break
        else:
            print("Invalid Age")

    # ---- Save user ----
    with open(r"C:\Users\user\.vscode\Pharmacy\users_info.txt", "a") as file:
        file.write(f"{username},{password},{role},{gender},{age}\n")

    print("Account created successfully")


# Load users from file
def load_users():
    users = {}

    with open(r"C:\Users\user\.vscode\Pharmacy\users_info.txt", "r") as file:
        for line in file:
            username, password, role, gender, age = line.strip().split(",")
            users[username] = {
                "password": password,
                "role": role,
                "gender": gender,
                "age": age
            }
    return users


# ===============================
# Remove user
# ===============================
def remove_user(username):
    users = load_users()

    if username in users:
        del users[username]
        save_users(users)
        print("User removed successfully")
    else:
        print("Invalid username")


# ===============================
# Save users to file
# ===============================
def save_users(users):
    with open(r"C:\Users\user\.vscode\Pharmacy\users_info.txt", "w") as file:
        for u, data in users.items():
            file.write(
                f"{u},{data['password']},{data['role']},"
                f"{data['gender']},{data['age']}\n"
            )


# ===============================
# Check if username exists
# ===============================
def username_exists(username):
    with open(r"C:\Users\user\.vscode\Pharmacy\users_info.txt", "r") as file:
        for line in file:
            data = line.strip().split(",")
            if username == data[0]:
                return True
    return False


# ===============================
# Authenticate user
# ===============================
def authenticate_user(username, password):
    users = load_users()

    if username in users and users[username]["password"] == password:
        return {
            "username": username,
            "role": users[username]["role"],
            "gender": users[username]["gender"],
            "age": users[username]["age"]
        }
    return None


# ===============================
# Permission check
# ===============================
def check_permissions(user, required_role):
    if user is None:
        return False
    return user["role"] == required_role

