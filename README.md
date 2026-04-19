# Expense Tracker CLI

A simple command-line tool for tracking personal expenses. Built in Python using the standard library — no external dependencies.

## Features

- Add expenses with amount, category, and optional note
- List expenses, optionally filtered by category
- Show total spending, optionally filtered by category
- JSON-based local storage (auto-created on first use)
- Input validation with clear error messages
- Auto-incrementing expense IDs
- Automatic date tagging

## Requirements

- Python 3.10 or higher

No third-party packages required.

## Installation

Clone the repository:

```bash
git clone https://github.com/Avradip24/Expense-Tracker-CLI.git
cd expense-tracker-cli
```

## Usage

### Add an expense

```bash
python tracker.py add --amount 12.50 --category food --note "lunch"
```

Available categories: `food`, `transport`, `entertainment`, `rent`, `others`.

### List expenses

All expenses:
```bash
python tracker.py list
```

Filtered by category:
```bash
python tracker.py list --category food
```

### Show total spending

Across all categories:
```bash
python tracker.py total
```

Filtered by category:
```bash
python tracker.py total --category transport
```

### Built-in help

```bash
python tracker.py --help
python tracker.py add --help
```

## How it works

Expenses are stored in `expenses.json` in the current directory. The file is created automatically on the first `add`. Each expense has the shape:

```json
{
  "id": 1,
  "amount": 12.50,
  "category": "food",
  "note": "lunch",
  "date": "2026-04-19"
}
```

## Project structure

```
expense-tracker-cli/
├── tracker.py      # Main script (CLI, persistence, command handlers)
├── .gitignore
└── README.md
```

## What I learned building this

- Structuring a Python CLI with `argparse` and subcommands
- JSON persistence with safe file handling (`with open`, UTF-8 encoding)
- Clean separation of concerns (parsing, command handling, storage)
- Input validation and graceful error handling
- Auto-incrementing IDs and date management

## Roadmap

Future enhancements I may add:
- Delete and edit commands
- CSV export
- Date range filtering
- Rewritten with dataclasses and proper project structure (Part 2 of my Python learning journey)