# Deliverable: ATM_FinalProject_Baez_v2.py

**Author:** Florentino Baez  
**Course:** ITSE-1002 Python Programming  
**Professor:** Mauricio Quiroga  
**Date:** February 2026

---

## Overview

`ATM_FinalProject_Baez_v2.py` is a simplified ATM (Automated Teller Machine) simulation program that replicates the main functionality of a real ATM: user authentication, deposits, withdrawals, balance inquiry, transaction history, and persistent data storage.

---

## Features

### 1. User Authentication

- **Default user:** Username and PIN defined in `DEFAULT_USER` (e.g., `("elvin", "1234")`)
- **Max attempts:** 3 login attempts before the program exits
- **Login flow:** Prompts for username and PIN; validates against the default user
- **Screen feedback:** Clears screen and displays success or failure messages

### 2. Persistent Account

- **Data file:** `atm_data.txt` stores the account state between sessions
- **On startup:** If the file exists, the program loads balance and transaction history
- **On exit:** Account data is always saved automatically
- **Format:** Same human-readable format as `atm_history.txt` (Deposit History, Withdrawal History, Balance History)

### 3. Menu Options

| # | Option | Description |
|---|--------|-------------|
| 1 | Deposit | Add funds with validation; updates balance and history |
| 2 | Withdraw | Remove funds if balance is sufficient |
| 3 | Check Balance | Show current balance |
| 4 | Deposit History | List all deposits |
| 5 | Withdrawal History | List all withdrawals |
| 6 | Balance History | Balance snapshot after each transaction |
| 7 | Exit | Save account and optionally export session report |

### 4. Input Validation

- **Amounts:** Only positive numbers accepted; re-prompts on invalid input
- **Withdrawals:** Checks sufficient funds before processing
- **Errors:** Catches `ValueError` for non-numeric input

### 5. User Interface

- **User and time:** Menu displays logged-in username and current date/time
- **Clear screen:** Used before actions (deposit, withdraw, history, etc.) for a cleaner layout
- **Formatting:** Currency values shown as `$X,XXX.XX`

---

## Data Files

| File | Purpose |
|------|---------|
| `atm_data.txt` | Persistent account data (balance, deposits, withdrawals, balances). Loaded on start, saved on exit. |
| `atm_history.txt` | Optional session report. Generated when the user chooses "Save session report" on exit. |

Both files use the same format:
```
ATM Session History
Saved: YYYY-MM-DD HH:MM:SS
==================================================

Deposit History:
1. $78.90
2. $56.89
...

Withdrawal History:
...
Balance History:
...
```

---

## Main Functions

| Function | Role |
|----------|------|
| `verify_login()` | Validates username and PIN; returns `(True, username)` or `(False, None)` |
| `load_account()` | Reads `atm_data.txt` and returns balance and history lists |
| `save_account()` | Writes current account state to `atm_data.txt` |
| `deposit()` | Prompts for amount, updates balance and deposit history |
| `withdraw()` | Prompts for amount, checks funds, updates balance and withdrawal history |
| `show_history()` | Prints a titled list of amounts |
| `save_to_file()` | Exports session report to `atm_history.txt` |
| `clear_screen()` | Clears terminal (Windows: `cls`, Unix: `clear`) |

---

## How to Run

```bash
cd Baez_Final_Project
python ATM_FinalProject_Baez_v2.py
```

**Default credentials:** username and PIN as defined in `DEFAULT_USER` (edit the constant to change them).

---

## Requirements

- Python 3.10+
- Standard library only (`os`, `datetime`, `pathlib`)
