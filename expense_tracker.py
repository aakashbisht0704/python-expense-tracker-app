from expense import Expense

def main():
    print(f'🎯Running Expense Tracker')
    expense_file_path = "expenses.csv"
    budget = 30000

    # Get user to input expense
    # expense = get_user_expense()

    # # Write the expense to a file
    # save_expense_to_file(expense, expense_file_path)

    # Read the file and summarise the expenses
    summarize_expenses(expense_file_path, budget)
    pass

def get_user_expense():
    print(f'Getting user expense')
    expense_name = input("Enter expense name:")
    expense_amount = float(input("Enter expense amount:"))

    expense_categories = [
        '🍔Food', 
        '🏠Home', 
        '💼Work', 
        '🎊Fun', 
        '✨Misc',
    ]
    while True:
        print("Select a category:")
        for i, catergory_name in enumerate(expense_categories):
            print(f' {i+1}. {catergory_name}')

        value_range = f"[1 - {len(expense_categories)}]"
        selected_index = int(input(f"Enter a category number {value_range}: ")) - 1

        if selected_index in range(len(expense_categories)):
            selected_category = expense_categories[selected_index]
            new_expense = Expense(
                name= expense_name, category= selected_category, amount= expense_amount, 
            )
            return new_expense
        else:
            print('Invalid Category. Please try again')

def save_expense_to_file(expense: Expense, expense_file_path):
    print(f'Saving user expense: {expense} to {expense_file_path}')
    with open(expense_file_path, "a", encoding= 'utf-8') as f:
        f.write(f"{expense.name},{expense.category},{expense.amount}\n")

def summarize_expenses(expense_file_path, budget):
    print(f'Reading and summarising user expense')
    expenses: list[Expense] = []
    with open(expense_file_path, "r", encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            expense_name, expense_category, expense_amount = line.strip().split(",")
            line_expense = Expense(
                name=expense_name, category= expense_category, amount= float(expense_amount)
            )
            expenses.append(line_expense)
    
    amount_by_category = {}
    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount

    print('Expenses by category')
    for key, amount in amount_by_category.items():
        print(f"  {key}: {amount} INR")

    total_spent = sum([x.amount for x in expenses])
    print(f"You've spent {total_spent} INR this month!")

    remaining_budget = budget - total_spent
    print(f"You have {remaining_budget} INR remaining")

if __name__ == '__main__':
    main()