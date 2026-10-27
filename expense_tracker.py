# Personal Expense Tracker

expenses = []

print("==============================")
print("       EXPENSE TRACKER")
print("==============================")

name = input("Enter your name: ")
print(f"\nWelcome, {name}!")

while True:
    print("\n---------- MENU ----------")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = float(input("Enter amount: ₹"))

        print("\nCategories:")
        print("1. Food")
        print("2. Travel")
        print("3. Shopping")
        print("4. Bills")
        print("5. Other")

        category_choice = input("Choose category: ")

        categories = {
            "1": "Food",
            "2": "Travel",
            "3": "Shopping",
            "4": "Bills",
            "5": "Other"
        }

        category = categories.get(category_choice, "Other")

        expense = {
            "amount": amount,
            "category": category
        }

        expenses.append(expense)

        print(f"Expense added: ₹{amount:.2f} ({category})")

    elif choice == "2":
        if not expenses:
            print("\nNo expenses recorded yet.")
        else:
            print("\n------- YOUR EXPENSES -------")

            for i, expense in enumerate(expenses, start=1):
                print(
                    f"{i}. {expense['category']} - "
                    f"₹{expense['amount']:.2f}"
                )

    elif choice == "3":
        total = sum(expense["amount"] for expense in expenses)
        print(f"\nTotal expenses: ₹{total:.2f}")

    elif choice == "4":
        print(f"\nThank you, {name}! Goodbye.")
        break

    else:
        print("\nInvalid choice. Please try again.")