# -------------------------------------------------
# File Name: ITSE-1003/Examples/file_handling/tkinter_form_basic.py
# Author: Florentino
# Date: 4/11/2026
# Description: Basic Tkinter form with labels, entries, and Submit / Clear / Quit.
# Run: python tkinter_form_basic.py
# -------------------------------------------------

import tkinter as tk
from tkinter import messagebox, ttk


def submit() -> None:
    name = entry_name.get().strip()
    email = entry_email.get().strip()
    city = entry_city.get().strip()
    if not name:
        messagebox.showwarning("Form", "Please enter a name.")
        return
    messagebox.showinfo(
        "Form submitted",
        f"Name: {name}\nEmail: {email or '(none)'}\nCity: {city or '(none)'}",
    )


def clear_form() -> None:
    entry_name.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_city.delete(0, tk.END)
    entry_name.focus_set()


root = tk.Tk()
root.title("Basic form")
root.geometry("360x200")
root.minsize(320, 180)

frm = ttk.Frame(root, padding=12)
frm.grid(sticky="nsew")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
frm.columnconfigure(1, weight=1)

ttk.Label(frm, text="Name:").grid(column=0, row=0, sticky=tk.W, pady=4)
entry_name = ttk.Entry(frm, width=36)
entry_name.grid(column=1, row=0, sticky="ew", pady=4)

ttk.Label(frm, text="Email:").grid(column=0, row=1, sticky=tk.W, pady=4)
entry_email = ttk.Entry(frm, width=36)
entry_email.grid(column=1, row=1, sticky="ew", pady=4)

ttk.Label(frm, text="City:").grid(column=0, row=2, sticky=tk.W, pady=4)
entry_city = ttk.Entry(frm, width=36)
entry_city.grid(column=1, row=2, sticky="ew", pady=4)

btn_row = ttk.Frame(frm)
btn_row.grid(column=0, row=3, columnspan=2, pady=(12, 0))
ttk.Button(btn_row, text="Submit", command=submit).pack(side=tk.LEFT, padx=4)
ttk.Button(btn_row, text="Clear", command=clear_form).pack(side=tk.LEFT, padx=4)
ttk.Button(btn_row, text="Quit", command=root.destroy).pack(side=tk.LEFT, padx=4)

entry_name.focus_set()
root.mainloop()
