#!/usr/bin/env python3
"""Baez Module 05 Lab - Exercise 2
Monthly Sales Tax
"""

def calculate_county_sales_tax(total_sales: float, county_rate: float = 0.025) -> float:
    return total_sales * county_rate


def calculate_state_sales_tax(total_sales: float, state_rate: float = 0.05) -> float:
    return total_sales * state_rate


def calculate_total_sales_tax(total_sales: float, county_rate: float = 0.025, state_rate: float = 0.05) -> float:
    county_tax = calculate_county_sales_tax(total_sales, county_rate)
    state_tax = calculate_state_sales_tax(total_sales, state_rate)
    return county_tax + state_tax


if __name__ == "__main__":
    print("=" * 60)
    print("EXERCISE 2: Monthly Sales Tax")
    print("=" * 60)
    STATE_TAX_RATE = 0.05
    COUNTY_TAX_RATE = 0.025
    try:
        total_sales = float(input("Enter the total sales for the month: $"))
        if total_sales < 0:
            print("Error: Total sales cannot be negative.")
        else:
            county_tax = calculate_county_sales_tax(total_sales, COUNTY_TAX_RATE)
            state_tax = calculate_state_sales_tax(total_sales, STATE_TAX_RATE)
            total_tax = calculate_total_sales_tax(total_sales, COUNTY_TAX_RATE, STATE_TAX_RATE)
            print(f"\nTotal Sales: ${total_sales:,.2f}")
            print(f"County Sales Tax ({COUNTY_TAX_RATE * 100}%): ${county_tax:,.2f}")
            print(f"State Sales Tax ({STATE_TAX_RATE * 100}%): ${state_tax:,.2f}")
            print(f"Total Sales Tax: ${total_tax:,.2f}")
    except ValueError:
        print("Error: Please enter a valid number.")
    except Exception as e:
        print(f"Error: {e}")
