import csv
from datetime import date
import sys
import os


def main():
    try:
        write_header()
        choice = get_choice()
        if choice == 1:
            today = date.today()
            description = input("Description: ").strip()
            category = input("Category: ").strip()
            amount = get_amount()
            add_expenses(today, description, category, amount)

        if choice == 2:
            view_expenses()

    except ValueError:
        sys.exit("Invalid Choice!")

def write_header():
    if not os.path.exists("expenses.csv"):
        with open("expenses.csv", 'w', newline="") as file:
            writer = csv.DictWriter(
                file,
                fieldnames= ["Date", "Description", "Category", "Amount"]
            )
            writer.writeheader()


def get_choice():
    try:
        return validate_choice(input("""Choose an option:
                        1. Add Expenses
                        2. View Expenses
                        Choice: """))

    except ValueError:
        sys.exit("Invalid Choice")


def validate_choice(choice):
    choice = int(choice)
    if choice not in [1, 2]:
        raise ValueError
    return choice

def add_expenses(dt, description, category, amount):
    with open("expenses.csv", 'a', newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["Date", "Description", "Category", "Amount"])
        writer.writerow({'Date': dt, 'Description' : description, 'Category' : category, 'Amount' : amount})


def view_expenses():
    total = 0

    with open("expenses.csv", 'r') as file:
        reader = csv.DictReader(file)

        print("\nExpense History:")
        print('-'*50)

        for row in reader:
            print(f"""Date: {row['Date']}
                      Description: {row['Description']}
                      Category: {row['Category']}
                      Amount:  {row['Amount']} Taka""")
            total += int(row['Amount'])
        print('-'*50)
        print(f"Total spent: {total} Taka")
        print('-'*50)



def get_amount():
    try:
        return validate_amount(input("Amount: "))

    except ValueError:
        sys.exit("Invalid amount!")

def validate_amount(amount):
    amount = int(amount)
    if amount <= 0:
        raise ValueError
    return amount



if __name__ == '__main__':
    main()
