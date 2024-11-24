# ------------------------------------PERSONAL BUDGET TRACKER-----------------------------------:

Income = {}  # Dictionary to store income by date
Expenses = {}  # Dictionary to store expenses by date


# Function to add multiple entries (income or expense)
def add_multiple_entries(entry_dict, entry_type):
    print(f'Adding multiple {entry_type} entries.')
    while True:
        date = input(f'Enter {entry_type} date (DD-MM-YYYY): ')  # Get date from the user
        if not date:  # Stop if no date is entered
            print(f'Finished adding {entry_type}.')
            break

        while True:
            category = input(f'Enter {entry_type} category (or press Enter to stop adding for this date): ')
            if not category:  # Stop adding for this date if no category is entered
                break

            amount = int(input(f'Enter {entry_type} amount: '))

            # Create a new entry dictionary
            entry = {'category': category, 'amount': amount}

            # Check if the date already exists in the dictionary
            if date not in entry_dict:
                entry_dict[date] = []  # Initialize an empty list if the date is not present

            # Append the new entry to the list for that date
            entry_dict[date].append(entry)
            print(f'Added {entry_type} entry for {date} successfully.')


# Function to calculate total amount of income or expenses for a specific date
def total_list(entry_dict, date):
    if date in entry_dict:  # Check if there are entries for that date
        total = sum(entry['amount'] for entry in entry_dict[date])
        return total
    else:
        print(f'No entries found for {date}')
        return 0


# Function to view the summary of income, expenses, and remaining budget for a specific date
def view_summary():
    date = input('Enter the date to view the summary (DD-MM-YYYY): ')  # Get date from the user
    total_income = total_list(Income, date)
    total_expense = total_list(Expenses, date)
    remaining_budget = total_income - total_expense

    print(f'\nSummary for {date}:')
    print(f'The Total Income Received is: ${total_income}')
    print(f'The Total Expense Spent is: ${total_expense}')
    print(f'The Remaining Budget is: ${remaining_budget}')

    if remaining_budget < 0:
        print('Warning: You are exceeding your expenses more than your income!')


# Main menu to navigate the program
def mainmenu():
    while True:
        print('\n--- PERSONAL BUDGET TRACKER ---')
        print('1. ADD MULTIPLE INCOME ENTRIES')
        print('2. ADD MULTIPLE EXPENSE ENTRIES')
        print('3. VIEW SUMMARY')
        print('4. VIEW INCOME LIST')
        print('5. VIEW EXPENSE LIST')
        print('6. EXIT')

        choice = int(input('Enter Your Choice: '))
        if choice == 1:
            add_multiple_entries(Income, 'income')
        elif choice == 2:
            add_multiple_entries(Expenses, 'expense')
        elif choice == 3:
            view_summary()
        elif choice == 4:
            print("\nIncome List:")
            print(Income)
        elif choice == 5:
            print("\nExpense List:")
            print(Expenses)
        elif choice == 6:
            print('Thank you for your information. Spend wisely. Have a Good Day!')
            break
        else:
            print("Invalid choice. Please enter a valid option.")


# Run the program
mainmenu()
