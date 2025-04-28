import json
import tkinter as tk
from tkinter import messagebox
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
    save_expenses()
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


def save_expenses():
    with open("expenses.json","w") as file:
        json.dump(expenses, file, indent=4)


def load_expenses():
    global expenses
    try:
        with open("expenses.json","r") as file:
            expenses = json.load(file)
    except FileNotFoundError:
        expenses = []

def main():
    load_expenses()
    

def submit_expense():
    amount = entry_amount.get()
    if amount:
        messagebox.showinfo("Success",f"Expense Added: ${amount}")
        entry_amount.delete(0,tk.END)
    else:
        messagebox.showwarning("Warning","Please enter an amount!")


root = tk.Tk()
root.title("Expense Tracker")
root.geometry("400x300")

label_category = tk.Label(root, text="Enter Expense Category:")
label_category.pack()

entry_category = tk.Entry(root)
entry_category.pack()

label_amount = tk.Label(root, text="Enter Expense Amount:")
label_amount.pack()

entry_amount = tk.Entry(root)
entry_amount.pack()

btn_submit = tk.Button(root, text="Add Expense", command=submit_expense)
btn_submit.pack()

root.mainloop()
