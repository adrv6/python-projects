# ============================================================
#  INVENTORY MANAGEMENT SYSTEM
# ============================================================

inventory = {}


def add_product(inventory, prod_id, name, price, quantity):
    """Adds a new product to the inventory."""
    if prod_id in inventory:
        print(f"❌ Error: A product with ID '{prod_id}' is already registered.")
        return
    inventory[prod_id] = {
        "name": name,
        "price": price,
        "quantity": quantity
    }
    print(f"✅ Product '{name}' added successfully.")


def update_stock(inventory, prod_id, quantity):
    """Adds or subtracts stock from an existing product."""
    if prod_id not in inventory:
        print(f"❌ Error: No product found with ID '{prod_id}'.")
        return
    new_stock = inventory[prod_id]["quantity"] + quantity
    if new_stock < 0:
        print(f"❌ Error: Insufficient stock. Current stock: {inventory[prod_id]['quantity']} units.")
        return
    inventory[prod_id]["quantity"] = new_stock
    action = "added" if quantity >= 0 else "removed"
    print(f"✅ Stock updated. {abs(quantity)} units {action}. Current stock: {new_stock}.")


def show_inventory(inventory):
    """Prints a formatted list of all products."""
    if not inventory:
        print("⚠️  The inventory is empty.")
        return
    print("\n" + "=" * 55)
    print(f"{'ID':<8} {'Name':<20} {'Price':>8} {'Quantity':>8}")
    print("=" * 55)
    for prod_id, data in inventory.items():
        print(f"{prod_id:<8} {data['name']:<20} {data['price']:>7.2f}€ {data['quantity']:>8}")
    print("=" * 55 + "\n")


def calculate_total_value(inventory):
    """Returns the total value of the inventory."""
    total = sum(p["price"] * p["quantity"] for p in inventory.values())
    return total


# ============================================================
#  INTERACTIVE MENU
# ============================================================

def menu():
    while True:
        print("\n╔══════════════════════════════╗")
        print("║    INVENTORY MANAGEMENT      ║")
        print("╠══════════════════════════════╣")
        print("║  1. Add product              ║")
        print("║  2. Update stock             ║")
        print("║  3. Show inventory           ║")
        print("║  4. Calculate total value    ║")
        print("║  5. Run tests                ║")
        print("║  6. Exit                     ║")
        print("╚══════════════════════════════╝")

        option = input("Choose an option: ").strip()

        if option == "1":
            prod_id = input("Product ID (e.g. P001): ").strip()
            name = input("Name: ").strip()
            try:
                price = float(input("Price (€): ").strip())
                quantity = int(input("Quantity: ").strip())
            except ValueError:
                print("❌ Error: price and quantity must be numbers.")
                continue
            add_product(inventory, prod_id, name, price, quantity)

        elif option == "2":
            prod_id = input("Product ID: ").strip()
            try:
                quantity = int(input("Quantity to add/remove (use negative to remove): ").strip())
            except ValueError:
                print("❌ Error: quantity must be a whole number.")
                continue
            update_stock(inventory, prod_id, quantity)

        elif option == "3":
            show_inventory(inventory)

        elif option == "4":
            total = calculate_total_value(inventory)
            print(f"\n💰 Total inventory value: {total:.2f}€")

        elif option == "5":
            run_tests()

        elif option == "6":
            print("👋 Goodbye!")
            break

        else:
            print("❌ Invalid option. Choose between 1 and 6.")


# ============================================================
#  AUTOMATED TESTS
# ============================================================

def run_tests():
    print("\n" + "🧪 " * 10)
    print("   RUNNING AUTOMATED TESTS")
    print("🧪 " * 10)

    test_inv = {}

    # Add 3 products
    print("\n--- Adding products ---")
    add_product(test_inv, "P001", "Mechanical Keyboard", 89.99, 15)
    add_product(test_inv, "P002", "Gaming Mouse", 45.50, 30)
    add_product(test_inv, "P003", '24" Monitor', 199.00, 8)

    # Try to add a duplicate ID
    print("\n--- Attempting duplicate ---")
    add_product(test_inv, "P001", "Duplicate Product", 10.00, 5)

    # Update stock (add and remove)
    print("\n--- Updating stock ---")
    update_stock(test_inv, "P001", 5)    # +5 keyboards
    update_stock(test_inv, "P002", -10)  # -10 mice

    # Try to sell more than available
    print("\n--- Attempting to sell more than available ---")
    update_stock(test_inv, "P003", -50)  # only 8 in stock, error expected

    # Try to update a non-existing product
    print("\n--- Non-existing product ---")
    update_stock(test_inv, "P999", 10)

    # Show final inventory
    print("\n--- Final inventory ---")
    show_inventory(test_inv)

    # Total value
    total = calculate_total_value(test_inv)
    print(f"💰 Total inventory value: {total:.2f}€")


# ============================================================
#  ENTRY POINT
# ============================================================

if __name__ == "__main__":
    print("What would you like to do?")
    print("  1. Run automated tests")
    print("  2. Open interactive menu")
    choice = input("Choose (1/2): ").strip()

    if choice == "1":
        run_tests()
    elif choice == "2":
        menu()
    else:
        print("Invalid option. Running tests by default...")
        run_tests()
