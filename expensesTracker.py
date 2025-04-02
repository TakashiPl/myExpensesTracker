import json
expenses = []
def add_expense():
    amount = float(input("Enter expenses amount: "))
    category = input("Enter category of your expenses (car, house, food, etc.): ")
    desc = input("Enter description: ")
    date = input("Enter date (YYYY-MM-DD): ")
    expense = {
        "amount": amount,
        "category": category,
        "description": desc,
        "date": date
    }
    expenses.append(expense)
    x = json.dumps(expenses)
    print("Expense added successfully!")

def view_expenses():
    if not expenses:
        print("There are no expenses to show. Maybe you should add some?")
        return
    
    print("\n--- Expense list ---")
    for idx, expense in enumerate(expenses, 1):
        print(f"{idx}. {expense['date']} - {expense['category']} - ${expense['amount']} ({expense['description']})")

def total_expenses():
    if not expenses:
        print("There were no expenses added.")
        return
    
    total = sum(expense["amount"] for expense in expenses)
    print(f"Total amount of the expenses is {total}")



while True:
    print("\nExpenses Tracker Menu")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Total Amount Of Expenses")
    print("4. Bye bye")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        total_expenses()
    elif choice == "4":
        print("Bye bye, thanks for using our expenses tracker!")
        break
    else:
        print("Wrong choice! Please pick between 1-4")
