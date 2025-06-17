# Capstone Project: Personal Finance Tracker
# Mandy Lubinski 

def menu(expense_dict):
    while True:
        print("\nWelcome to the Personal Finance Tracker!")
        print("What would you like to do?")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Summary")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            while True:
                try:
                    expense_desc = input("Enter expense description: ")
                    if not expense_desc:
                        raise ValueError("Description cannot be empty.")

                    expense_cat = input("Enter category: ")
                    if not expense_cat:
                        raise ValueError("Category cannot be empty.")

                    while True:
                        amount_input = input("Enter amount: ").strip()
                        if not amount_input:
                            print("Amount cannot be empty.")
                            continue
                        try:
                            expense_amt = float(amount_input)
                            break
                        except ValueError:
                            print("Invalid amount. Please enter a number.")

                except ValueError as e:
                    print(f"Error: {e}")
            
                expense_tuple = (expense_desc, expense_amt)

                if expense_cat in expense_dict:
                    expense_dict[expense_cat].append(expense_tuple)
                else:
                    expense_dict[expense_cat] = [expense_tuple]
                print("\nExpense added successfully.")
                
                answer = input("Would you like to add another? (yes/no) ")
                if answer == "no":
                    break
                    
        elif choice == "2":
            view_expenses(expense_dict)
        elif choice == "3":
            view_summary(expense_dict)
        elif choice == "4":
            print("Goodbye!")
            break

        else: 
            print("Invalid option. Please enter 1, 2, 3, or 4.")

def view_expenses(data):
    for cat in data:
        print(f"Category: {cat}")
        for desc, amount in data[cat]:
            print(f"  - {desc}: ${amount:.2f}")

def view_summary(data):
    print("\nSummary:")
    for cat in data:
        total = sum(amount for _, amount in data[cat])
        print(f"{cat}: ${total:.2f}")

def main():
    expense_dict = {}
    menu(expense_dict)

if __name__ == "__main__":
    main()