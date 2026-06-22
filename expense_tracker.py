expenses = []

while True:
    print("\n=== Expense Tracker ===")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Total Expense")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        try:
            amount = float(input("Enter expense amount: "))
            category = input("Enter expense category: ")

            expenses.append({
                "amount": amount,
                "category": category
            })

            print("Expense added successfully!")

        except ValueError:
            print("Please enter a valid amount.")

    elif choice == "2":
        if not expenses:
            print("No expenses recorded.")
        else:
            print("\nRecorded Expenses:")
            for expense in expenses:
                print(
                    f"Category: {expense['category']} | Amount: ₹{expense['amount']}"
                )

    elif choice == "3":
        total = sum(expense["amount"] for expense in expenses)
        print(f"\nTotal Expense: ₹{total}")

    elif choice == "4":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice. Please try again.")
