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



add_expense()
view_expenses()
total_expenses()

