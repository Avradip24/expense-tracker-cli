"""Command-line interface: argument parsing and dispatch."""

import argparse

from .commands import handle_add, handle_list, handle_total
from .models import CATEGORIES

def parse_args() -> argparse.Namespace:
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
