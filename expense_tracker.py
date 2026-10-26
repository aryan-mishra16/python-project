# Personal Expense Tracker

print("==============================")
print("       EXPENSE TRACKER")
print("==============================")

name = input("Enter your name: ")

expenses = []

while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        category = input("Enter category (Food/Travel/Shopping/Other): ")
        amount = float(input("Enter amount: ₹"))

        expenses.append({
            "category": category,
            "amount": amount
        })

        print("Expense added successfully!")

    elif choice == "2":
        if not expenses:
            print("No expenses recorded.")
        else:
            print("\nYour Expenses:")
            for i, expense in enumerate(expenses, start=1):
                print(
                    f"{i}. {expense['category']} - "
                    f"₹{expense['amount']:.2f}"
                )

    elif choice == "3":
        total = sum(expense["amount"] for expense in expenses)
        print(f"\nTotal spent: ₹{total:.2f}")

    elif choice == "4":
        print(f"\nGoodbye, {name}!")
        break

    else:
        print("Invalid choice. Please try again.")