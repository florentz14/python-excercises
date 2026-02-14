# Baez_Final_Project

Final Project: ATM Simulation Program.

## Note on try-except Blocks

A `try-except` block has been added to the program. **Reasons:**

1. **Input validation**: `float()` and `int()` raise `ValueError` when the user enters non-numeric input (e.g., letters or empty input). The try-except catches this and displays a friendly error message instead of crashing.
2. **Robustness**: Prevents the program from terminating unexpectedly due to invalid or unexpected input.
3. **User experience**: Prompts the user to re-enter valid data rather than exiting with a traceback.

## Description

Simulates a basic automated teller machine (ATM) with the following features:

- **Password protection**: 3 login attempts, default PIN: 1234
- **Menu-driven interface** with 7 options
- **Input validation**: Prevents invalid amounts and non-numeric entries

## Menu Options

| # | Option | Description |
|---|--------|-------------|
| 1 | Deposit | Add funds with validation |
| 2 | Withdraw | Remove funds (if sufficient balance) |
| 3 | Check Balance | Display current amount |
| 4 | History of Deposit | List all deposits |
| 5 | History of Withdrawals | List all withdrawals |
| 6 | History of Balance | Balance snapshot after each transaction |
| 7 | Exit | Save session histories to file (optional) and quit |

## Files

| File | Content |
|------|---------|
| `ATM_FinalProject_Baez.py` | Main program: ATM simulation with menu, deposit, withdraw, balance, history, and file export |
| `atm_history.txt` | Session history (generated when saving on exit; stored in this folder) |

## How to Run

```bash
cd Baez_Final_Project
python ATM_FinalProject_Baez.py
```

Or from the project root:

```bash
python Baez_Final_Project/ATM_FinalProject_Baez.py
```

The session history file (`atm_history.txt`) is always saved inside the `Baez_Final_Project` folder, regardless of where the program is run from.

## Requirements

- Python 3.14+ (or 3.10+ for type hints)
- Standard library only (no external dependencies)
