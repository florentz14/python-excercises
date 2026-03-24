# -------------------------------------------------
# File Name: ITSE-1003/Examples/sales/invoice_model.py
# Author: Florentino Báez
# Date: 3/20/2026
# Description: Master-detail model — Invoice (header) and InvoiceLine (detail), load from CSV.
# -------------------------------------------------

from __future__ import annotations

import csv
import sys
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path
from typing import Iterable, List, Optional

_examples_dir = Path(__file__).resolve().parent.parent
if str(_examples_dir) not in sys.path:
    sys.path.insert(0, str(_examples_dir))

from examples_paths import INVOICE_LINES_CSV, INVOICES_CSV


@dataclass
class InvoiceLine:
    """Detail row belonging to one invoice (invoice_id FK)."""

    line_id: int
    invoice_id: int
    sku: str
    description: str
    quantity: float
    unit_price: float

    @property
    def line_total(self) -> float:
        return round(self.quantity * self.unit_price, 2)

    def __str__(self) -> str:
        return (
            f"  [{self.line_id}] {self.sku} ×{self.quantity} @ {self.unit_price:.2f} "
            f"= {self.line_total:.2f} — {self.description}"
        )


@dataclass
class Invoice:
    """Master record; holds related InvoiceLine instances."""

    invoice_id: int
    invoice_number: str
    customer_name: str
    invoice_date: date
    currency: str
    tax_rate: float
    status: str
    lines: List[InvoiceLine] = field(default_factory=list)

    def add_line(self, line: InvoiceLine) -> None:
        if line.invoice_id != self.invoice_id:
            raise ValueError(
                f"Line invoice_id={line.invoice_id} does not match invoice {self.invoice_id}"
            )
        self.lines.append(line)

    @property
    def subtotal(self) -> float:
        return round(sum(ln.line_total for ln in self.lines), 2)

    @property
    def tax_amount(self) -> float:
        return round(self.subtotal * self.tax_rate, 2)

    @property
    def grand_total(self) -> float:
        return round(self.subtotal + self.tax_amount, 2)

    def __str__(self) -> str:
        lines_txt = "\n".join(str(ln) for ln in self.lines) if self.lines else "  (no lines)"
        return (
            f"{self.invoice_number} | {self.customer_name} | {self.invoice_date} | {self.status}\n"
            f"  Subtotal: {self.subtotal:.2f} {self.currency} | "
            f"Tax ({self.tax_rate:.0%}): {self.tax_amount:.2f} | "
            f"Total: {self.grand_total:.2f} {self.currency}\n"
            f"{lines_txt}"
        )


def _parse_date(s: str) -> date:
    y, m, d = (int(p) for p in s.strip().split("-"))
    return date(y, m, d)


def load_invoice_lines_from_csv(
    path: Optional[Path] = None,
) -> List[InvoiceLine]:
    """Read all detail rows from invoice_lines.csv."""
    csv_path = path or INVOICE_LINES_CSV
    lines: List[InvoiceLine] = []
    with csv_path.open(encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            lines.append(
                InvoiceLine(
                    line_id=int(row["line_id"]),
                    invoice_id=int(row["invoice_id"]),
                    sku=row["sku"].strip(),
                    description=row["description"].strip(),
                    quantity=float(row["quantity"]),
                    unit_price=float(row["unit_price"]),
                )
            )
    return lines


def load_invoices_from_csv(
    invoices_path: Optional[Path] = None,
    lines_path: Optional[Path] = None,
) -> List[Invoice]:
    """Load invoices (master) and attach lines (detail) by invoice_id."""
    inv_path = invoices_path or INVOICES_CSV
    ln_path = lines_path or INVOICE_LINES_CSV

    by_invoice: dict[int, List[InvoiceLine]] = {}
    for ln in load_invoice_lines_from_csv(ln_path):
        by_invoice.setdefault(ln.invoice_id, []).append(ln)

    invoices: List[Invoice] = []
    with inv_path.open(encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            iid = int(row["invoice_id"])
            inv = Invoice(
                invoice_id=iid,
                invoice_number=row["invoice_number"].strip(),
                customer_name=row["customer_name"].strip(),
                invoice_date=_parse_date(row["invoice_date"]),
                currency=row["currency"].strip(),
                tax_rate=float(row["tax_rate"]),
                status=row["status"].strip(),
                lines=list(by_invoice.get(iid, [])),
            )
            invoices.append(inv)
    return invoices


def print_invoices_summary(invoices: Iterable[Invoice]) -> None:
    try:
        from tabulate import tabulate
    except ImportError:
        for inv in invoices:
            print(inv)
            print()
        return

    rows = []
    for inv in invoices:
        rows.append(
            [
                inv.invoice_number,
                inv.customer_name,
                str(inv.invoice_date),
                inv.status,
                inv.subtotal,
                inv.tax_amount,
                inv.grand_total,
                inv.currency,
                len(inv.lines),
            ]
        )
    headers = [
        "Number",
        "Customer",
        "Date",
        "Status",
        "Subtotal",
        "Tax",
        "Total",
        "Curr.",
        "Lines",
    ]
    print(tabulate(rows, headers=headers, tablefmt="grid", floatfmt=".2f"))


if __name__ == "__main__":
    all_invoices = load_invoices_from_csv()
    print("Invoices loaded:", len(all_invoices))
    print()
    print_invoices_summary(all_invoices)
    print()
    for inv in all_invoices:
        print(inv)
        print("-" * 60)
