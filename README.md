# Zewail Pharmacy System 💊

A complete pharmacy management system built with Python.  
The system supports user management, medicine inventory control, and billing with receipts.

---

## 📌 Project Overview

**Zewail Pharmacy System** is a console-based pharmacy management application designed for academic purposes.  
It allows admins and employees to manage medicines, users, and billing operations efficiently using file-based storage.

---

## ✨ Features

### 👤 User Management
- Add new users (Admin / Employee)
- Remove users (Admin only)
- User authentication (Login system)
- Role-based permissions

### 💊 Medicine Management
- Add, edit, search, and delete medicines
- Load and save medicines from file
- Low quantity alerts
- Expiration date alerts

### 🧾 Billing System
- Load inventory
- Add medicines to cart
- Calculate subtotal, tax (14%), and total
- Print formatted receipts
- Save receipts to file

---

## 🛠 Technologies Used
- **Python**
- File Handling (`.txt` files)
- Date & Time (`datetime` module)
- Console-based UI

---

## 📂 Project Structure

```
Pharmacy/
│
├── billing.py
├── user_management.py
├── medicine_management.py
├── main.py
│
├── users_info.txt
├── medicines.txt
├── all_receipts.txt
│
└── README.md
```

---
## ▶️ How to Run the Project

1. Make sure Python is installed
2. Open the project folder in terminal or VS Code
3. Run the main file:

```bash
python main.py
```
---
## 🔐 Permissions

### Admin
- Add / remove users
- Full access to medicines and billing

### Employee
- Medicine management
- Billing system only



---

## ⚠️ Notes
- Data is stored using text files (for educational purposes)
- No external libraries are required
- This project is not intended for production use

---

## 👨‍💻 Authors
- Abdelrahman Khaled  
- Mark Sherif  
- Youssef Wael

---

## 📄 License
This project is for educational use only.
Modification or redistribution without permission is not allowed.