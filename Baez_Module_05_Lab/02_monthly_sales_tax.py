#!/usr/bin/env python3
# -------------------------------------------------
# File Name: 02_monthly_sales_tax.py
# Author: Florentino Báez
# Course: ITSE-1002: Python Programming
# Professor: Mauricio Quiroga
# Date: Module 05 Lab
# Description: Monthly sales tax calculator (county + state).
# -------------------------------------------------

# Calculate county sales tax
def calculate_county_sales_tax(total_sales: float, county_rate: float = 0.025) -> float:
    return total_sales * county_rate


# Calculate state sales tax
def calculate_state_sales_tax(total_sales: float, state_rate: float = 0.05) -> float:
    return total_sales * state_rate


# Calculate total sales tax (county + state)
def calculate_total_sales_tax(total_sales: float, county_rate: float = 0.025, state_rate: float = 0.05) -> float:
    county_tax = calculate_county_sales_tax(total_sales, county_rate)
    state_tax = calculate_state_sales_tax(total_sales, state_rate)
    return county_tax + state_tax


print("=" * 60)
print("EXERCISE 2: Monthly Sales Tax")
print("=" * 60)

STATE_TAX_RATE = 0.05
COUNTY_TAX_RATE = 0.025

total_sales = float(input("Enter the total sales for the month: $"))
if total_sales < 0:
    print("Error: Total sales cannot be negative.")
else:
    county_tax = calculate_county_sales_tax(total_sales, COUNTY_TAX_RATE)
    state_tax = calculate_state_sales_tax(total_sales, STATE_TAX_RATE)
    total_tax = calculate_total_sales_tax(
        total_sales, COUNTY_TAX_RATE, STATE_TAX_RATE)
    print(f"\nTotal Sales: ${total_sales:,.2f}")
    print(f"County Sales Tax ({COUNTY_TAX_RATE * 100}%): ${county_tax:,.2f}")
    print(f"State Sales Tax ({STATE_TAX_RATE * 100}%): ${state_tax:,.2f}")
    print(f"Total Sales Tax: ${total_tax:,.2f}")

print()

print("\n" + "=" * 60)
print("CITATION")
print("=" * 60)
print("1. Sales Tax Calculation:")
print("   - Standard formula: Tax Amount = Sales Amount × Tax Rate")
print("   Source: State and Local Sales Tax Rates")
print("   https://taxfoundation.org/state-and-local-sales-tax-rates/")
