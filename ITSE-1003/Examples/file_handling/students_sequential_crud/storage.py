"""Leer y escribir el CSV (lista de dicts). Patron: READ -> modificar lista -> WRITE."""

import csv

from config import CSV_PATH, FIELDNAMES


def load_students():
    if not CSV_PATH.is_file():
        return []
    with open(CSV_PATH, "r", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def save_students(rows):
    CSV_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(CSV_PATH, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(rows)


def next_sid(rows):
    highest = 50000
    for row in rows:
        sid = row.get("SID", "").strip()
        if sid.isdigit():
            highest = max(highest, int(sid))
    return str(highest + 1)


def find_index_by_sid(rows, sid):
    key = sid.strip()
    if not key:
        return -1
    for i, row in enumerate(rows):
        if row.get("SID", "").strip() == key:
            return i
    return -1
