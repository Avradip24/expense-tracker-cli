"""Command handlers: business logic for add, list, and total operations."""



import argparse
from datetime import date

from .storage import load_expenses, save_expenses
from .models import Expense


def handle_add(args: argparse.Namespace) -> None:
    """Handle the 'add' command to add a new expense."""
    expenses = load_expenses()
    next_id = 1
    if expenses:
        next_id = max(e.id for e in expenses) + 1
    new_expense = Expense(
        id = next_id,
        amount = args.amount,
        category = args.category,
        note = args.note,
        date = date.today().isoformat()
    )
    expenses.append(new_expense)
    save_expenses(expenses)
    print(f"Added expense: {new_expense.id} - {new_expense.amount} Euro for {new_expense.category}")

def handle_list(args: argparse.Namespace) -> None:
    """Handle the 'list' command to display expenses."""
    expenses = load_expenses()

    if args.category:
        expenses = [e for e in expenses if e.category == args.category]

    if not expenses:
        if args.category:
            print(f"No expenses found for category '{args.category}'.")
        else:
            print("No expenses found.")
        return
    
    for e in expenses:
        print(f"{e.id}: {e.amount} Euro for {e.category} on {e.date} - Note: {e.note}")

def handle_total(args: argparse.Namespace) -> None:
    """Handle the 'total' command to display total spending."""
    expenses = load_expenses()

    if args.category:
        expenses = [e for e in expenses if e.category == args.category]
        
    if not expenses:
        if args.category:
            print(f"No expenses to total for category '{args.category}'.")
        else:
            print("No expenses to total.")
        return
    
    total = sum(e.amount for e in expenses)
    label = f"for category '{args.category}'" if args.category else "across all categories"
    print(f"Total spending {label}: {total} Euro")
