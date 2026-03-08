# Notes: ATM_FinalProject_Baez_v2.py

**Author:** Florentino Baez  
**Course:** ITSE-1002 Python Programming  
**Professor:** Mauricio Quiroga  
**Date:** February 2026

---

## What the Program Does

`ATM_FinalProject_Baez_v2.py` simulates an ATM (Automated Teller Machine). It works like this:

1. **Login** — At startup, the program asks for a username and PIN. It checks them against a hardcoded default user. You get up to 3 attempts; after 3 failed tries, the program exits.

2. **Main loop** — After a successful login, the program shows a menu and lets you choose what to do. It keeps showing the menu until you pick Exit (option 7).

3. **Transactions** — You can deposit and withdraw money. The program keeps lists of all deposits, all withdrawals, and the balance after each transaction.

4. **Persistence** — All data is stored in `atm_data.txt`. When you run the program, it loads your balance and histories from that file. When you exit, it saves everything back to the same file so your data is kept between sessions.

5. **Input handling** — It only accepts valid positive amounts. If you enter something non‑numeric or negative, it asks again instead of crashing.

---

## Program Flow (Step by Step)

```
Start
  → verify_login() → if fail, exit
  → load_account() → get balance and histories from atm_data.txt (or start at 0)
  → Loop:
       print_menu()
       user picks 1–7
       → Option 1: deposit()
       → Option 2: withdraw()
       → Option 3: show current balance
       → Option 4: show_history(deposits)
       → Option 5: show_history(withdrawals)
       → Option 6: show_history(balances)
       → Option 7: save_account(), goodbye, break
  → End
```

---

## What Each Function Does

### `verify_login()`

**What it does:** Handles the login step at the beginning.

- Clears the screen and asks for username and PIN.
- Uses `getpass` to hide the PIN while typing and shows a warning.
- Compares input to `DEFAULT_USER` (e.g., `("elvin", "1234")`).
- Allows up to 3 attempts (`MAX_ATTEMPTS`). On correct login, returns `(True, username)`. On failure after 3 tries, returns `(False, None)` and the program exits.

---

### `get_amount(prompt)`

**What it does:** Gets a valid positive dollar amount from the user.

- Shows the given prompt (e.g., `"Enter amount to deposit: $"`).
- Uses a loop to keep asking until the user enters a valid positive number.
- Ignores non‑numeric input and negative values, and prints clear error messages.
- Returns the valid amount as a float.

---

### `deposit(balance, deposits, balances)`

**What it does:** Processes a deposit.

- Asks for an amount using `get_amount()`.
- Adds the amount to the current balance.
- Appends the amount to the `deposits` list.
- Appends the new balance to the `balances` list (balance history).
- Prints a success message with the new balance.
- Returns the updated balance.

---

### `withdraw(balance, withdrawals, balances)`

**What it does:** Processes a withdrawal.

- Asks for an amount using `get_amount()`.
- If the amount is greater than the balance, prints an error and returns the unchanged balance.
- Otherwise, subtracts the amount from the balance.
- Appends the withdrawn amount to the `withdrawals` list.
- Appends the new balance to the `balances` list.
- Prints a success message with the new balance.
- Returns the updated balance.

---

### `show_history(title, items)`

**What it does:** Displays one of the history lists on screen.

- Prints a title (e.g., `"Deposit History"` or `"Withdrawal History"`).
- If the list is empty, prints `"No transactions yet."`
- Otherwise, prints each item as a numbered list with currency format (`$X,XXX.XX`).
- Used for Deposit History (option 4), Withdrawal History (option 5), and Balance History (option 6).

---

### `print_menu(username)`

**What it does:** Prints the main ATM menu.

- Shows the username and current date/time.
- Prints the 7 options: Deposit, Withdraw, Check Balance, Deposit History, Withdrawal History, Balance History, Exit.
- Does not process input; that is done in `main()`.

---

### `get_data_filepath()`

**What it does:** Returns the path to the data file.

- Returns `Path(__file__).parent / "atm_data.txt"` so the file is in the same folder as the script.
- Used by `load_account()` and `save_account()` to know where to read from and write to.

---

### `file_exists()`

**What it does:** Checks if the account data file exists.

- Returns `True` if `atm_data.txt` exists, `False` otherwise.
- Used to decide whether to show “Account loaded. Current balance: $X.XX” when the program starts.

---

### `_parse_amount_line(line)`

**What it does:** Helper used when loading the account file.

- Parses a line like `"1. $78.90"` and returns the number (e.g., `78.90`) as a float.
- Returns `None` if the line does not contain a valid amount.
- Used inside `load_account()` to read deposit, withdrawal, and balance values from `atm_data.txt`.

---

### `load_account()`

**What it does:** Loads the account state from the file.

- If `atm_data.txt` does not exist, returns `(0.0, [], [], [])` (empty account).
- If it exists, reads the file and parses Deposit History, Withdrawal History, and Balance History.
- Sets the current balance to the last value in Balance History.
- Returns `(balance, deposits, withdrawals, balances)`.
- On read errors, prints a message and returns an empty account so the program can continue.

---

### `save_account(balance, deposits, withdrawals, balances_list)`

**What it does:** Writes the current account state to the file.

- Writes to `atm_data.txt` in a human‑readable format.
- Saves a timestamp, plus Deposit History, Withdrawal History, and Balance History, each as numbered lists.
- Called when the user chooses Exit (option 7) so data is preserved between sessions.

---

### `clear_screen()`

**What it does:** Clears the terminal screen.

- On Windows, runs `cls`. On Unix/Mac, runs `clear`.
- Used after login and before each menu action to keep the display tidy.

---

### `main()`

**What it does:** Runs the whole ATM program.

1. Calls `verify_login()`. If login fails, exits.
2. Calls `load_account()` to get balance and histories (or start empty).
3. If the data file existed, shows “Account loaded. Current balance: $X.XX”.
4. Enters a loop:
   - Calls `print_menu()`.
   - Reads the user’s choice.
   - Calls the right function for each option (1–6) or saves and exits (7).
5. Exits when the user chooses option 7.

---

## Data File (atm_data.txt)

The program uses a single file, `atm_data.txt`, in the same folder as the script. It looks like:

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

- **Loaded** when the program starts (if the file exists).
- **Saved** when the user exits (option 7).

---

## How to Run

```bash
cd Baez_Final_Project
python ATM_FinalProject_Baez_v2.py
```

**Default credentials:** username `elvin`, PIN `1234` (defined in `DEFAULT_USER`).

---

## Requirements

- Python 3.10+
- Standard library only: `getpass`, `os`, `datetime`, `pathlib`
