"""Application configuration.

Resolves file paths and other configurable values, allowing overrides
from environment variables (loaded from a .env file if present).
"""

import os
from pathlib import Path

from dotenv import load_dotenv

# Load variables from .env file if it exists. Silent if not present.
load_dotenv()

# Default location: a per-user data directory.
# On Windows: C:\Users\<user>\.expense-tracker\
# On macOS / Linux: ~/.expense-tracker/
_DEFAULT_DATA_DIR = Path.home() / ".expense-tracker"


def get_data_dir() -> Path:
    """Return the directory where expense data is stored.

    Override with the EXPENSE_TRACKER_DATA_DIR environment variable.
    """
    env_dir = os.environ.get("EXPENSE_TRACKER_DATA_DIR")
    data_dir = Path(env_dir) if env_dir else _DEFAULT_DATA_DIR
    data_dir.mkdir(parents=True, exist_ok=True)
    return data_dir


def get_expenses_file() -> Path:
    """Return the full path to the expenses JSON file.

    Override with the EXPENSE_TRACKER_FILE environment variable.
    """
    env_file = os.environ.get("EXPENSE_TRACKER_FILE")
    if env_file:
        return Path(env_file)
    return get_data_dir() / "expenses.json"