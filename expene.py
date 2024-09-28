def display_expenses(expenses):
    """Display all logged expenses."""
    if not expenses:
        print("No expenses logged.")
    else:
        print("\nYour Expenses:")
        for index, (description, amount) in enumerate(expenses, start=1):
            print(f"{index}. {description}: ${amount:.2f}")
        print()

def add_expense(expenses):
    """Add a new expense."""
    description = input("Enter expense description: ")
    try:
        amount = float(input("Enter amount: "))
        expenses.append((description, amount))
        print("Expense added.\n")
    except ValueError:
        print("Invalid amount. Please enter a numeric value.\n")

def total_expenses(expenses):
    """Calculate and return total expenses."""
    return sum(amount for _, amount in expenses)

def expense_tracker():
    expenses = []
    
    print("Welcome to the Expense Tracker!")
    
    while True:
        print("1. View Expenses")
        print("2. Add Expense")
        print("3. Total Expenses")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            display_expenses(expenses)
        elif choice == '2':
            add_expense(expenses)
        elif choice == '3':
            total = total_expenses(expenses)
            print(f"Total Expenses: ${total:.2f}\n")
        elif choice == '4':
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid option, please try again.\n")

if __name__ == "__main__":
    expense_tracker()
