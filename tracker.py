import argparse
from datetime import datetime
import random


categories = ["food", "transport", "entertainment", "rent", "others"]

def parse_args()-> argparse.Namespace:
    """Parse Command Line Arguments"""

    parser = argparse.ArgumentParser(description="Expense Tracker")
    subparsers = parser.add_subparsers(dest="command", required=True)

    #add command
    add_parser = subparsers.add_parser("add", help="Add a new Expense")
    add_parser.add_argument("--amount", type=float, required=True, help="Amount of expense in Euro")
    add_parser.add_argument("--category", choices=categories, required=True, help="Expense falls in which category ?")
    add_parser.add_argument("--note", type=str, default="", help="Optional note for the expense")

    #list command
    list_parser = subparsers.add_parser("list", help="List expenses, optionally filtered by category")
    list_parser.add_argument("--category", choices=categories, help="Filter expenses by category")

    #total command
    total_parser = subparsers.add_parser("total", help="Show total spending, optionally filtered by category")
    total_parser.add_argument("--category", choices=categories, help="Filter total by category")

    return parser.parse_args()

def main() -> None:
    """Entry point for the Application"""
    args = parse_args()

    if args.command == "add":
        print(f"TODO: add expense - amount={args.amount}, category={args.category}, note='{args.note}'") 
    elif args.command == "list":
        if args.category:
            print(f"TODO: list expenses filtered by category - {args.category}")
        else:
            print(f"TODO: list all expenses")
    elif args.command == "total":
        if args.category:
            print(f"TODO: show total spending filtered by category - {args.category}")
        else:
            print(f"TODO: show total spending across all categories")

if __name__ == "__main__":
    main()

