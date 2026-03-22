# -------------------------------------------------
# File Name: ITSE-1003/Examples/customer_form.py
# Author: Florentino Báez
# Date: 3/20/2026
# Description: Integrating validations from utils.py.
# -------------------------------------------------

import sys
from datetime import datetime
from pathlib import Path

_examples_dir = Path(__file__).resolve().parent
if str(_examples_dir) not in sys.path:
    sys.path.insert(0, str(_examples_dir))

from utils import (
    clamp,
    format_currency,
    format_phone_number,
    input_date,
    input_email,
    input_float,
    input_int,
    input_option,
    input_str,
    input_yes_no,
    is_positive_float,
)


class Customer:
    def __init__(
        self,
        name: str,
        age: int,
        email: str,
        phone: str,
        plan: str,
        newsletter: bool,
        join_date: datetime,
        monthly_budget: float,
        discount_pct: float,
    ) -> None:
        self.name = name
        self.age = age
        self.email = email
        self.phone = phone
        self.plan = plan
        self.newsletter = newsletter
        self.join_date = join_date
        self.monthly_budget = monthly_budget
        self.discount_pct = clamp(discount_pct, 0, 50)

    @property
    def final_monthly_budget(self) -> float:
        return self.monthly_budget * (1 - self.discount_pct / 100)

    def summary(self) -> str:
        newsletter_text = "Yes" if self.newsletter else "No"
        return (
            f"Customer: {self.name}\n"
            f"Age: {self.age}\n"
            f"Email: {self.email}\n"
            f"Phone: {self.phone}\n"
            f"Plan: {self.plan}\n"
            f"Newsletter: {newsletter_text}\n"
            f"Join date: {self.join_date.strftime('%Y-%m-%d')}\n"
            f"Monthly budget: {format_currency(self.monthly_budget)}\n"
            f"Discount: {self.discount_pct:.1f}%\n"
            f"Final monthly budget: {format_currency(self.final_monthly_budget)}"
        )


def create_customer() -> Customer:
    print("\n=== Customer Registration (Validated) ===")

    name = input_str("Name: ", min_length=2, max_length=50)
    age = input_int("Age (18-100): ", 18, 100)
    email = input_email("Email: ")
    phone = format_phone_number(input_str("Phone number: ", min_length=7, max_length=20))
    plan = input_option("Plan", ["basic", "pro", "premium"])
    newsletter = input_yes_no("Subscribe to newsletter?")
    join_date = input_date("Join date (YYYY-MM-DD): ")
    monthly_budget = input_float("Monthly budget (10 - 100000): ", 10, 100000)
    discount_pct = input_float("Discount % (0 - 50): ", 0, 50)

    if not is_positive_float(monthly_budget):
        raise ValueError("Monthly budget must be positive.")

    return Customer(
        name=name,
        age=age,
        email=email,
        phone=phone,
        plan=plan,
        newsletter=newsletter,
        join_date=join_date,
        monthly_budget=monthly_budget,
        discount_pct=discount_pct,
    )


def main() -> None:
    customer = create_customer()
    print("\n=== Registration Summary ===")
    print(customer.summary())


if __name__ == "__main__":
    main()
