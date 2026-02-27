# Baez_Final_Project

Final Project: ATM Simulation Program.

**Author:** Florentino Baez  
**Course:** ITSE-1002 Python Programming  
**Professor:** Mauricio Quiroga

---

## Description

Simulates a basic automated teller machine (ATM) with the following features:

- **Password protection**: 3 login attempts, default PIN: 1234
- **Menu-driven interface** with 7 options
- **Input validation**: Prevents invalid amounts and non-numeric entries
- **Session history**: Optional save to file on exit

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

---

## Project Files

| File | Description |
|------|-------------|
| `ATM_FinalProject_Baez.py` | **Main program** – Full ATM with try-except, type hints, all features |
| `ATM_FinalProject_Baez_v2.py` | Simplified version with functions (same features, cleaner code) |
| `ATM_FinalProject_Baez_v1.py` | Working ATM with **no functions** – all logic inline |
| `ATM_FinalProject_Baez_v0.py` | ATM menu skeleton – functions print placeholder messages only |
| `demo_menu.py` | Demo menu (Say Hello, Add Numbers, Show Name, Quit) – practice with `while choice != 4` |
| `atm_history.txt` | Session history (generated when saving on exit) |

### Version Overview

| Version | Style | Use Case |
|---------|--------|----------|
| v0 | Menu + placeholder functions | Learning structure, add logic later |
| v1 | No functions, inline code | Working app before refactoring |
| v2 | Functions, simplified | Cleaner production-ready code |
| Main | Full version, type hints, try-except | Complete reference implementation |

---

## How to Run

**Main program:**
```bash
cd Baez_Final_Project
python ATM_FinalProject_Baez.py
```

**Other versions:**
```bash
python ATM_FinalProject_Baez_v2.py   # Simplified with functions
python ATM_FinalProject_Baez_v1.py   # No functions
python ATM_FinalProject_Baez_v0.py   # Menu skeleton
python demo_menu.py                 # Demo menu
```

From project root:
```bash
python Baez_Final_Project/ATM_FinalProject_Baez.py
```

The session history file (`atm_history.txt`) is saved in the `Baez_Final_Project` folder.

---

## Note on try-except Blocks

The main program uses `try-except` for:

1. **Input validation**: `float()` and `int()` raise `ValueError` on non-numeric input. The try-except catches this and shows a friendly message instead of crashing.
2. **Robustness**: Prevents unexpected termination from invalid input.
3. **User experience**: Prompts the user to re-enter valid data.

---

## Requirements

- Python 3.10+ (3.14+ for full type hint support)
- Standard library only (no external dependencies)
