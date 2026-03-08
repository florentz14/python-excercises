# -------------------------------------------------
# File Name: 21_simple_interest.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Simple interest and related amount calculations.
# -------------------------------------------------

def calculate_simple_interest(principal, rate, time):
    """
    Calculate simple interest
    Formula: SI = P * R * T / 100
    Where:
    P = Principal amount
    R = Rate of interest per year
    T = Time in years
    """
    return (principal * rate * time) / 100


def calculate_total_amount(principal, interest):
    """Calculate total amount (principal + interest)"""
    return principal + interest


def calculate_principal_from_interest(interest, rate, time):
    """Calculate principal from interest amount"""
    return (interest * 100) / (rate * time)


def calculate_rate_from_interest(interest, principal, time):
    """Calculate rate from interest amount"""
    return (interest * 100) / (principal * time)


def calculate_time_from_interest(interest, principal, rate):
    """Calculate time from interest amount"""
    return (interest * 100) / (principal * rate)


# Examples
print("Simple Interest Calculations:")
print("=" * 30)

# Basic example
principal = 1000
rate = 5  # 5% per year
time = 2  # 2 years

interest = calculate_simple_interest(principal, rate, time)
total = calculate_total_amount(principal, interest)

print(f"Principal: ${principal}")
print(f"Rate: {rate}% per year")
print(f"Time: {time} years")
print(f"Simple Interest: ${interest}")
print(f"Total Amount: ${total}")

# Different scenarios
print("\nDifferent Scenarios:")

# Scenario 1: Short term loan
p1, r1, t1 = 5000, 8, 0.5  # 6 months = 0.5 years
si1 = calculate_simple_interest(p1, r1, t1)
print(f"Loan: ${p1} at {r1}% for {t1} years = ${si1} interest")

# Scenario 2: Savings account
p2, r2, t2 = 2500, 3.5, 3
si2 = calculate_simple_interest(p2, r2, t2)
total2 = calculate_total_amount(p2, si2)
print(f"Savings: ${p2} at {r2}% for {t2} years = ${total2} total")

# Scenario 3: Investment
p3, r3, t3 = 10000, 7, 5
si3 = calculate_simple_interest(p3, r3, t3)
total3 = calculate_total_amount(p3, si3)
print(f"Investment: ${p3} at {r3}% for {t3} years = ${total3} total")

# Reverse calculations
print("\nReverse Calculations:")

# If I know the interest earned, what was the principal?
interest_earned = 250
rate_known = 5
time_known = 2
principal_calc = calculate_principal_from_interest(
    interest_earned, rate_known, time_known)
print(
    f"If interest is ${interest_earned} at {rate_known}% for {time_known} years, principal = ${principal_calc}")

# What rate gives this interest?
interest_known = 300
principal_known = 2000
time_known = 3
rate_calc = calculate_rate_from_interest(
    interest_known, principal_known, time_known)
print(
    f"If interest is ${interest_known} on ${principal_known} for {time_known} years, rate = {rate_calc}%")

# How long to earn this interest?
interest_target = 400
principal_target = 5000
rate_target = 4
time_calc = calculate_time_from_interest(
    interest_target, principal_target, rate_target)
print(f"To earn ${interest_target} on ${principal_target} at {rate_target}%, time needed = {time_calc} years")

# Monthly interest calculation
print("\nMonthly Interest:")
monthly_principal = 1200
monthly_rate = 6  # Annual rate
months = 12
annual_interest = calculate_simple_interest(monthly_principal, monthly_rate, 1)
monthly_interest = annual_interest / 12
print(
    f"Annual interest on ${monthly_principal} at {monthly_rate}% = ${annual_interest}")
print(f"Monthly interest = ${monthly_interest:.2f}")

# Comparison with compound interest
print("\nComparison (Simple vs Compound):")
p = 1000
r = 5
t = 3

simple_total = calculate_total_amount(p, calculate_simple_interest(p, r, t))
compound_total = p * (1 + r/100) ** t

print(f"Principal: ${p}, Rate: {r}%, Time: {t} years")
print(f"Simple Interest Total: ${simple_total:.2f}")
print(f"Compound Interest Total: ${compound_total:.2f}")
print(f"Difference: ${compound_total - simple_total:.2f}")
