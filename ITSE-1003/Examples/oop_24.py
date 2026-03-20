# -------------------------------------------------
# File Name: ITSE-1003/Examples/oop_24.py
# Author: Florentino Báez
# Date: 3/20/2026
# Description: Simple CRUD system with utils.py validations.
# -------------------------------------------------

from datetime import datetime

from utils import (
    format_currency,
    format_phone_number,
    input_date,
    input_email,
    input_float,
    input_int,
    input_option,
    input_str,
    input_yes_no,
)


class Customer:
    def __init__(
        self,
        customer_id: int,
        name: str,
        age: int,
        email: str,
        phone: str,
        plan: str,
        newsletter: bool,
        join_date: datetime,
        monthly_budget: float,
    ) -> None:
        self.customer_id = customer_id
        self.name = name
        self.age = age
        self.email = email
        self.phone = phone
        self.plan = plan
        self.newsletter = newsletter
        self.join_date = join_date
        self.monthly_budget = monthly_budget

    def one_line(self) -> str:
        return (
            f"[{self.customer_id}] {self.name} | {self.plan} | "
            f"{format_currency(self.monthly_budget)} | {self.email}"
        )

    def details(self) -> str:
        return (
            f"ID: {self.customer_id}\n"
            f"Name: {self.name}\n"
            f"Age: {self.age}\n"
            f"Email: {self.email}\n"
            f"Phone: {self.phone}\n"
            f"Plan: {self.plan}\n"
            f"Newsletter: {'Yes' if self.newsletter else 'No'}\n"
            f"Join Date: {self.join_date.strftime('%Y-%m-%d')}\n"
            f"Monthly Budget: {format_currency(self.monthly_budget)}"
        )


class CustomerApp:
    def __init__(self) -> None:
        self.customers: list[Customer] = []
        self.next_id = 1

    def menu(self) -> int:
        print("\n=== Customer CRUD Menu ===")
        print("1) Create customer")
        print("2) List customers")
        print("3) View customer details")
        print("4) Update customer plan")
        print("5) Delete customer")
        print("6) Exit")
        return input_int("Choose an option (1-6): ", 1, 6)

    def create_customer(self) -> None:
        print("\n--- Create Customer ---")
        name = input_str("Name: ", min_length=2, max_length=50)
        age = input_int("Age (18-100): ", 18, 100)
        email = input_email("Email: ")
        phone = format_phone_number(input_str("Phone number: ", min_length=7, max_length=20))
        plan = input_option("Plan", ["basic", "pro", "premium"])
        newsletter = input_yes_no("Subscribe to newsletter?")
        join_date = input_date("Join date (YYYY-MM-DD): ")
        monthly_budget = input_float("Monthly budget (10 - 100000): ", 10, 100000)

        customer = Customer(
            customer_id=self.next_id,
            name=name,
            age=age,
            email=email,
            phone=phone,
            plan=plan,
            newsletter=newsletter,
            join_date=join_date,
            monthly_budget=monthly_budget,
        )
        self.customers.append(customer)
        self.next_id += 1
        print(f"Customer created with ID {customer.customer_id}.")

    def list_customers(self) -> None:
        print("\n--- Customer List ---")
        if not self.customers:
            print("No customers registered.")
            return
        for customer in self.customers:
            print(customer.one_line())

    def find_by_id(self, customer_id: int) -> Customer | None:
        for customer in self.customers:
            if customer.customer_id == customer_id:
                return customer
        return None

    def view_details(self) -> None:
        print("\n--- Customer Details ---")
        if not self.customers:
            print("No customers registered.")
            return
        customer_id = input_int("Enter customer ID: ", 1, 999999)
        customer = self.find_by_id(customer_id)
        if customer is None:
            print("Customer not found.")
            return
        print(customer.details())

    def update_plan(self) -> None:
        print("\n--- Update Customer Plan ---")
        if not self.customers:
            print("No customers registered.")
            return
        customer_id = input_int("Enter customer ID: ", 1, 999999)
        customer = self.find_by_id(customer_id)
        if customer is None:
            print("Customer not found.")
            return
        new_plan = input_option("New plan", ["basic", "pro", "premium"])
        customer.plan = new_plan
        print("Plan updated successfully.")

    def delete_customer(self) -> None:
        print("\n--- Delete Customer ---")
        if not self.customers:
            print("No customers registered.")
            return
        customer_id = input_int("Enter customer ID: ", 1, 999999)
        customer = self.find_by_id(customer_id)
        if customer is None:
            print("Customer not found.")
            return
        confirm = input_yes_no(f"Delete {customer.name}?")
        if not confirm:
            print("Deletion cancelled.")
            return
        self.customers.remove(customer)
        print("Customer deleted.")

    def run(self) -> None:
        while True:
            choice = self.menu()
            if choice == 1:
                self.create_customer()
            elif choice == 2:
                self.list_customers()
            elif choice == 3:
                self.view_details()
            elif choice == 4:
                self.update_plan()
            elif choice == 5:
                self.delete_customer()
            else:
                print("Goodbye.")
                break


def main() -> None:
    app = CustomerApp()
    app.run()


if __name__ == "__main__":
    main()
