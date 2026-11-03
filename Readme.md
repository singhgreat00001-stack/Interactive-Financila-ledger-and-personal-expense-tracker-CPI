# Interactive Financial Ledger & Personal Expense Tracker CLI

**Capstone Track:** Curated Track Project, Option 1 (Easy)

A command-line app for recording income and expenses, categorizing them, and viewing summaries. It is also a record of the Python fundamentals I learned while building it.

## Features

- Add income and expense entries (amount, category, date, note)
- List, search, edit and delete transactions
- Filter by category, date range or type
- Monthly summary and running balance
- Category-wise spending report
- Data saved to a local JSON/CSV file between runs
- Export the ledger to CSV
- Input validation and clear error messages

## Python Concepts Used

| Concept | Where it appears |
|---------|------------------|
| Variables, data types, f-strings | Formatting amounts, dates and reports |
| Control flow (if/else, loops) | Interactive menu loop |
| Lists, dicts, sets, tuples | Storing transactions, grouping by category |
| Functions (args, kwargs, return values) | Each ledger operation as a reusable function |
| OOP (classes, dataclasses) | `Transaction` and `Ledger` classes |
| File handling (JSON/CSV) | Saving, loading and exporting data |
| Exception handling | Invalid input, missing or corrupt files |
| Modules and packages | Splitting the app into separate files |
| `datetime` | Date parsing, filtering by month |
| `argparse` / `input()` | CLI commands and interactive prompts |
| List comprehensions, `sorted`, `sum` | Reports and totals |
| Testing with pytest | Unit tests for the ledger logic |
| Virtual environments, pip | Reproducible setup |

## Project Structure

```
expense-tracker-cli/
├── README.md
├── requirements.txt
├── data/
│   └── ledger.json          # created on first run
├── tracker/
│   ├── __init__.py
│   ├── models.py            # Transaction, Ledger classes
│   ├── storage.py           # load/save JSON, export CSV
│   ├── reports.py           # summaries and category totals
│   ├── validators.py        # input checks
│   └── cli.py               # menu and commands
├── tests/
│   ├── test_models.py
│   ├── test_storage.py
│   └── test_reports.py
└── main.py                  # entry point
```

## Getting Started

```bash
git clone https://github.com/<your-username>/expense-tracker-cli.git
cd expense-tracker-cli
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

## Example Usage

```
$ python main.py

=== Personal Expense Tracker ===
1. Add transaction
2. View all transactions
3. Monthly summary
4. Category report
5. Export to CSV
6. Exit

Choose an option: 1
Type (income/expense): expense
Amount: 450
Category: Food
Note: Lunch
Saved.
```

## Running Tests

```bash
pytest
```

## What I Learned

- Breaking a problem into small functions and modules
- Modeling real data with classes
- Persisting data safely and handling bad input
- Writing tests to prove my code works
- Organizing a project so it is easy to read and run

## Challenges & Solutions

- _Challenge:_ (e.g. handling invalid dates) → _Solution:_ (e.g. validator with try/except)
- _Challenge:_ ...

## Future Improvements

- Budgets and overspending alerts
- SQLite instead of JSON
- Charts for monthly trends

## Original Work

All code in this repository is my own original work.

## License

MIT
