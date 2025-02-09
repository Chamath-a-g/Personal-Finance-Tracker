import json

# Global list to store transactions
transactions = []

# File handling functions

#Function to load transactions from json file
def load_transactions():
    try:
        with open('transactions.json', 'r') as file:
            global transactions
            transactions = json.load(file)
    except FileNotFoundError:
        pass

#function to save transactions to a json file
def save_transactions():
    file = open('transactions.json', 'w')
    file.write('[')  # Start with an empty list
    file.write('\n')
    for transaction in transactions:
        json.dump(transaction, file)
        file.write(',' if transaction != transactions[-1] else '')  # Add comma after each JSON object except the last one
        file.write('\n')  # Add newline after each JSON object
    file.write(']')
      
# Feature implementations

#Function to add a transaction
def add_transaction():
    while True:
        try:
            amount = float(input("Enter the amount: "))
        except ValueError:
            print("Invalid input")
            continue
        else:
            break

    while True:
        category = input("Enter the category: ")
        if not category:
            print("Category cannot be empty.")
            continue
        break

    while True:
        type_ = input("Enter the type (Income/Expense): ").capitalize()
        if type_ not in ["Income", "Expense"]:
            print("Invalid input. Type must be either 'Income' or 'Expense'.")
            continue
        break
    date = input("Enter the date (YYYY-MM-DD): ")

    new_transaction = [amount, category, type_, date]
    transactions.append(new_transaction)
    print("Transaction added successfully.")
    save_transactions()

#Function to view all transactions
def view_transactions():
    print("\nTransactions:")
    for transaction in transactions:
        print(transaction)
    print()

#Function to update a transaction
def update_transaction():
    view_transactions()
    try:
        index = int(input("Enter the index of the transaction to update: "))
        if 0 <= index < len(transactions):
            amount = float(input("Enter the new amount: "))
            category = input("Enter the new category: ")
            type_ = input("Enter the new type (Income/Expense): ").capitalize()
            date = input("Enter the new date (YYYY-MM-DD): ")

            transactions[index] = [amount, category, type_, date]
            print("Transaction updated successfully.")
            save_transactions()
        else:
            print("Invalid index.")
    except ValueError:
        print("Invalid input. Please enter a valid index.")
    # Placeholder for update transaction logic
    # Remember to use save_transactions() after updating

#Function to delete a transaction
def delete_transaction():
    view_transactions()
    try:
        index = int(input("Enter the index of the transaction to delete: "))
        if 0 <= index < len(transactions):
            deleted_transaction = transactions.pop(index)
            print("Transaction deleted successfully.")
            print("Deleted transaction:", deleted_transaction)
            save_transactions()
        else:
            print("Invalid index.")
    except ValueError:
        print("Invalid input. Please enter a valid index.")
    # Placeholder for delete transaction logic
    # Remember to use save_transactions() after deleting

#Function to display a summary of transactions
def display_summary():
    total_income = sum(transaction[0] for transaction in transactions if transaction[2] == "Income")
    total_expense = sum(transaction[0] for transaction in transactions if transaction[2] == "Expense")

    print("\nSummary:")
    print(f"Total Income: {total_income}")
    print(f"Total Expense: {total_expense}")
    print(f"Balance: {total_income - total_expense}")
    # Placeholder for summary display logic

def main_menu():
    load_transactions()  # Load transactions at the start
    while True:
        print("\nPersonal Finance Tracker")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Update Transaction")
        print("4. Delete Transaction")
        print("5. Display Summary")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_transaction()
        elif choice == '2':
            view_transactions()
        elif choice == '3':
            update_transaction()
        elif choice == '4':
            delete_transaction()
        elif choice == '5':
            display_summary()
        elif choice == '6':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()

# if you are paid to do this assignment please delete this line of comment 
