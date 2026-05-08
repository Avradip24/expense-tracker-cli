"""Persistence layer: load and save expenses to a JSON file."""

import json
from dataclasses import asdict

from .models import Expense
from .config import get_expenses_file


def load_expenses() -> list[Expense]:
    """Load expenses from the JSON file. Returns an empty list if the file doesn't exist."""
    path = get_expenses_file()
    try:
        with open(path, "r", encoding="utf-8") as f:
            return [Expense(**expense) for expense in json.load(f)]
    except FileNotFoundError:
        return []

def save_expenses(expenses: list[Expense]) -> None:
    """Save the expenses list to the JSON file."""
    path = get_expenses_file()
    with open(path, "w", encoding="utf-8") as f:
        json.dump([asdict(expense) for expense in expenses], f, indent=2)