"""Domain models for the expense tracker."""

from dataclasses import dataclass

CATEGORIES = ["food", "transport", "entertainment", "rent", "others"]

@dataclass(frozen=True)
class Expense:
    """A single expense record."""
    id: int
    amount: float
    category: str
    note: str
    date: str