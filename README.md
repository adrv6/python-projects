# 📦 Inventory Management System

A simple command-line inventory management program built in Python. Manage products, update stock levels, and calculate total inventory value — all from an interactive menu.

---

## 🚀 Features

- Add new products with ID, name, price and quantity
- Update stock (add or remove units) with error handling
- Display a formatted inventory table
- Calculate the total value of the inventory
- Interactive menu loop
- Built-in automated test suite

---

## 🛠️ Requirements

- Python 3.6+
- No external libraries needed

---

## ▶️ How to run

```bash
python inventory.py
```

You'll be prompted to either open the interactive menu or run the automated tests.

---

## 📋 Menu options

| Option | Description |
|--------|-------------|
| 1 | Add a new product |
| 2 | Update stock (positive to add, negative to remove) |
| 3 | Show full inventory |
| 4 | Calculate total inventory value |
| 5 | Run automated tests |
| 6 | Exit |

---

## 🧪 Automated tests

Selecting option **5** (or **1** at startup) will run a test suite that covers:

- Adding 3 products
- Handling duplicate product IDs
- Updating stock up and down
- Attempting to sell more than available stock (error case)
- Attempting to update a non-existing product (error case)
- Displaying the final inventory and total value

---

## 📁 Project structure

```
inventory-management/
│
└── inventory.py   # Main script
```

---

## 💡 Example output

```
╔══════════════════════════════╗
║    INVENTORY MANAGEMENT      ║
╠══════════════════════════════╣
║  1. Add product              ║
║  2. Update stock             ║
║  3. Show inventory           ║
║  4. Calculate total value    ║
║  5. Run tests                ║
║  6. Exit                     ║
╚══════════════════════════════╝

=======================================================
ID       Name                   Price  Quantity
=======================================================
P001     Mechanical Keyboard    89.99€       20
P002     Gaming Mouse           45.50€       20
P003     24" Monitor           199.00€        8
=======================================================

💰 Total inventory value: 4301.80€
```

---

## 📝 License

This project is open source and available under the [MIT License](LICENSE).
