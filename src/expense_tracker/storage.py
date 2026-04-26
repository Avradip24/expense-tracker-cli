"""Persistence layer: load and save expenses to a JSON file."""

import json
from dataclasses import asdict

from .models import Expense

EXPENSES_FILE = "expenses.json"


def load_expenses() -> list[Expense]:
    """Load expenses from expenses.json. Returns an empty list if the file doesn't exist."""
    try:
        with open(EXPENSES_FILE, "r", encoding="utf-8") as f:
            return [Expense(**expense) for expense in json.load(f)]
    except FileNotFoundError:
        return []

def save_expenses(expenses: list[Expense]) -> None:
    """Save the expenses list to expenses.json."""
    with open(EXPENSES_FILE, "w", encoding="utf-8") as f:
        json.dump([asdict(expense) for expense in expenses], f, indent=2)