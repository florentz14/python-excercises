# -------------------------------------------------
# File Name: ITSE-1003/Examples/file_handling/students_sequential_crud/gui_app.py
# Author: Florentino
# Date: 4/10/2026
# Description: Simple Tkinter GUI for student CSV CRUD (uses storage.py).
# Run from this folder: python gui_app.py
# -------------------------------------------------

import tkinter as tk
from tkinter import messagebox, ttk

from storage import (
    find_index_by_sid,
    load_students,
    next_sid,
    save_students,
)


def _name_taken(rows: list[dict[str, str]], name: str, skip_sid: str | None = None) -> bool:
    key = name.strip().casefold()
    for row in rows:
        if skip_sid is not None and row["SID"].strip() == skip_sid.strip():
            continue
        if row["Name"].strip().casefold() == key:
            return True
    return False


class StudentCrudApp:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Student CSV CRUD (Tkinter)")
        self.root.geometry("640x400")
        self.root.minsize(520, 320)

        toolbar = ttk.Frame(root, padding=4)
        toolbar.pack(fill=tk.X)
        ttk.Button(toolbar, text="Refresh", command=self.refresh).pack(side=tk.LEFT, padx=2)
        ttk.Button(toolbar, text="Add", command=self.open_add).pack(side=tk.LEFT, padx=2)
        ttk.Button(toolbar, text="Edit", command=self.open_edit).pack(side=tk.LEFT, padx=2)
        ttk.Button(toolbar, text="Delete", command=self.delete_selected).pack(side=tk.LEFT, padx=2)

        tree_frame = ttk.Frame(root, padding=4)
        tree_frame.pack(fill=tk.BOTH, expand=True)
        cols = ("SID", "Name", "Age", "Major")
        self.tree = ttk.Treeview(
            tree_frame,
            columns=cols,
            show="headings",
            selectmode="browse",
        )
        for c in cols:
            self.tree.heading(c, text=c)
            self.tree.column(c, width=120 if c != "Major" else 180)
        scroll = ttk.Scrollbar(tree_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scroll.set)
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)

        self.refresh()

    def refresh(self) -> None:
        for item in self.tree.get_children():
            self.tree.delete(item)
        for row in load_students():
            self.tree.insert(
                "",
                tk.END,
                values=(row["SID"], row["Name"], row["Age"], row["Major"]),
            )

    def _selected_sid(self):
        sel = self.tree.selection()
        if not sel:
            return None
        return str(self.tree.item(sel[0], "values")[0])

    def open_add(self) -> None:
        win = tk.Toplevel(self.root)
        win.title("Add student")
        win.transient(self.root)
        win.grab_set()

        entries = {}
        for i, label in enumerate(("Name", "Age", "Major")):
            ttk.Label(win, text=f"{label}:").grid(row=i, column=0, sticky=tk.W, padx=8, pady=4)
            e = ttk.Entry(win, width=32)
            e.grid(row=i, column=1, padx=8, pady=4)
            entries[label] = e

        def save() -> None:
            name = entries["Name"].get().strip()
            if not name:
                messagebox.showwarning("Add", "Name is required.", parent=win)
                return
            rows = load_students()
            if _name_taken(rows, name):
                messagebox.showwarning("Add", "That name already exists.", parent=win)
                return
            row = {
                "SID": next_sid(rows),
                "Name": name,
                "Age": entries["Age"].get().strip(),
                "Major": entries["Major"].get().strip(),
            }
            rows.append(row)
            save_students(rows)
            self.refresh()
            win.destroy()

        ttk.Button(win, text="Save", command=save).grid(row=3, column=0, columnspan=2, pady=12)

    def open_edit(self) -> None:
        sid = self._selected_sid()
        if not sid:
            messagebox.showwarning("Edit", "Select a student in the table.")
            return
        rows = load_students()
        i = find_index_by_sid(rows, sid)
        if i < 0:
            messagebox.showerror("Edit", "Student not found.")
            return
        current = rows[i]

        win = tk.Toplevel(self.root)
        win.title(f"Edit SID {sid}")
        win.transient(self.root)
        win.grab_set()

        ttk.Label(win, text=f"SID: {sid} (read-only)").grid(row=0, column=0, columnspan=2, padx=8, pady=4)
        entries = {}
        for r, field in enumerate(("Name", "Age", "Major"), start=1):
            ttk.Label(win, text=f"{field}:").grid(row=r, column=0, sticky=tk.W, padx=8, pady=4)
            e = ttk.Entry(win, width=32)
            e.insert(0, current[field])
            e.grid(row=r, column=1, padx=8, pady=4)
            entries[field] = e

        def save() -> None:
            rows2 = load_students()
            idx = find_index_by_sid(rows2, sid)
            if idx < 0:
                messagebox.showerror("Edit", "Student disappeared; refresh and try again.", parent=win)
                return
            new_name = entries["Name"].get().strip()
            if not new_name:
                messagebox.showwarning("Edit", "Name is required.", parent=win)
                return
            if new_name != rows2[idx]["Name"] and _name_taken(rows2, new_name, skip_sid=sid):
                messagebox.showwarning("Edit", "Another student has that name.", parent=win)
                return
            rows2[idx]["Name"] = new_name
            rows2[idx]["Age"] = entries["Age"].get().strip()
            rows2[idx]["Major"] = entries["Major"].get().strip()
            save_students(rows2)
            self.refresh()
            win.destroy()

        ttk.Button(win, text="Save", command=save).grid(row=4, column=0, columnspan=2, pady=12)

    def delete_selected(self) -> None:
        sid = self._selected_sid()
        if not sid:
            messagebox.showwarning("Delete", "Select a student in the table.")
            return
        rows = load_students()
        i = find_index_by_sid(rows, sid)
        if i < 0:
            return
        name = rows[i]["Name"]
        if not messagebox.askyesno("Delete", f"Delete SID {sid} ({name})?"):
            return
        rows = [r for r in rows if r["SID"].strip() != sid.strip()]
        save_students(rows)
        self.refresh()


def main() -> None:
    root = tk.Tk()
    StudentCrudApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
