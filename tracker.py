import argparse
from datetime import date, datetime
import json

CATEGORIES = ["food", "transport", "entertainment", "rent", "others"]
EXPENSES_FFILE = "expenses.json"

def load_expenses() -> list[dict]:
    """Load expenses from expenses.json. Returns an empty list if the file doesn't exist."""
    try:
        with open(EXPENSES_FFILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_expenses(expenses: list[dict]) -> None:
    """Save the expenses list to expenses.json."""
    with open(EXPENSES_FFILE, "w", encoding="utf-8") as f:
        json.dump(expenses, f, indent=2)

def handle_add(args: argparse.Namespace) -> None:
    """Handle the 'add' command to add a new expense."""
    expenses = load_expenses()
    next_id = 1
    if expenses:
        next_id = max(e["id"] for e in expenses) + 1
    new_expense = {
        "id": next_id,
        "amount": args.amount,
        "category": args.category,
        "note": args.note,
        "date": date.today().isoformat()
    }
    expenses.append(new_expense)
    save_expenses(expenses)
    print(f"Added expense: {new_expense['id']} - {new_expense['amount']} Euro for {new_expense['category']}")

def handle_list(args: argparse.Namespace) -> None:
    """Handle the 'list' command to display expenses."""
    expenses = load_expenses()

    if args.category:
        expenses = [e for e in expenses if e["category"] == args.category]

    if not expenses:
        if args.category:
            print(f"No expenses found for category '{args.category}'.")
        else:
            print("No expenses found.")
        return
    
    for e in expenses:
        print(f"{e['id']}: {e['amount']} Euro for {e['category']} on {e['date']} - Note: {e['note']}")

def handle_total(args: argparse.Namespace) -> None:
    """Handle the 'total' command to display total spending."""
    expenses = load_expenses()

    if args.category:
        expenses = [e for e in expenses if e["category"] == args.category]
    if not expenses:
        if args.category:
            print(f"No expenses to total for category '{args.category}'.")
        else:
            print("No expenses to total.")
        return
    
    total = sum(e["amount"] for e in expenses)
    label = f"for category '{args.category}'" if args.category else "across all categories"
    print(f"Total spending {label}: {total} Euro")

def parse_args()-> argparse.Namespace:
    """Parse Command Line Arguments"""

    parser = argparse.ArgumentParser(description="Expense Tracker")
    subparsers = parser.add_subparsers(dest="command", required=True)

    #add command
    add_parser = subparsers.add_parser("add", help="Add a new Expense")
    add_parser.add_argument("--amount", type=float, required=True, help="Amount of expense in Euro")
    add_parser.add_argument("--category", choices=CATEGORIES, required=True, help="Expense falls in which category ?")
    add_parser.add_argument("--note", type=str, default="", help="Optional note for the expense")

    #list command
    list_parser = subparsers.add_parser("list", help="List expenses, optionally filtered by category")
    list_parser.add_argument("--category", choices=CATEGORIES, help="Filter expenses by category")

    #total command
    total_parser = subparsers.add_parser("total", help="Show total spending, optionally filtered by category")
    total_parser.add_argument("--category", choices=CATEGORIES, help="Filter total by category")

    return parser.parse_args()

def main() -> None:
    """Entry point for the Application"""
    args = parse_args()

    if args.command == "add":
        handle_add(args)
    elif args.command == "list":
        handle_list(args)
    elif args.command == "total":
        handle_total(args)

if __name__ == "__main__":
    main()

