import os
import sys
import glob


# Function to read data from all files

def read_data(folder):
    invoices = []
    for filename in glob.glob(os.path.join(folder, "*.dat")):
        with open(filename, "r") as f:
            lines = [line.strip() for line in f if line.strip()]

        bill_no, store, customer = lines[0].split(",")

        items = []
        for line in lines[1:]:
            name, category, qty, price = line.split(",")
            items.append((name, category, float(qty), float(price)))

        invoices.append((bill_no, store, customer, items))
    return invoices



# Get all customers (unique names)

def get_all_customers(data):
    customers = sorted({c for _, _, c, _ in data})
    print("\nCustomers:\n")
    for c in customers:
        print(c)
    print()


# Get all stores (unique names)

def get_all_stores(data):
    stores = sorted({s for _, s, _, _ in data})
    print("\nStores:\n")
    for s in stores:
        print(s)
    print()



# Get all categories (unique)

def get_all_categories(data):
    categories = set()
    for _, _, _, items in data:
        for _, category, _, _ in items:
            categories.add(category)
    print("\nCategories:\n")
    for c in sorted(categories):
        print(c)
    print()



# See customer spend per store

def customer_spend_per_store(data, customer):
    # Collect all stores
    stores = sorted({s for _, s, _, _ in data})
    spend = {store: 0.0 for store in stores}

    for _, store, cust, items in data:
        if cust.lower() == customer.lower():
            total = sum(q * p for _, _, q, p in items)
            spend[store] += total

    print(f"\n{customer} spend per store:\n")
    for s in stores:
        print(f"{s:15s} {spend[s]:8.1f}")
    print()



# Loyal customers (buy from only one store)

def loyal(data):
    customer_stores = {}
    for _, store, customer, _ in data:
        customer_stores.setdefault(customer, set()).add(store)

    loyal_customers = [c for c, stores in customer_stores.items() if len(stores) == 1]

    print("\nLoyal customers:\n")
    for c in sorted(loyal_customers):
        print(c)
    print()



# Main program menu

def main():
    if len(sys.argv) != 2:
        print("Usage: python Shopping.py <folder>")
        return

    folder = sys.argv[1]
    data = read_data(folder)

    print("\nWelcome to Shopping Program\n")
    while True:
        print("See all customers (c)")
        print("See all stores (s)")
        print("See all categories (g)")
        print("See customer purchases at various stores (p cname)")
        print("See loyal customers (y)")
        print("Quit (q)")
        choice = input("\nWhat do you want to see? ").strip()

        if choice == "c":
            get_all_customers(data)
        elif choice == "s":
            get_all_stores(data)
        elif choice == "g":
            get_all_categories(data)
        elif choice.startswith("p "):
            cname = choice[2:].strip()
            customer_spend_per_store(data, cname)
        elif choice == "y":
            loyal(data)
        elif choice == "q":
            print("\nBye!")
            break
        else:
            print("\nInvalid command\n")


if __name__ == "__main__":
    main()
