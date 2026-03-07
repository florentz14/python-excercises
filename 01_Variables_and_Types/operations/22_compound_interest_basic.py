# Compound Interest Calculations in Python

def calculate_compound_interest(principal, rate, time, compounding_frequency=1):
    """
    Calculate compound interest
    Formula: A = P(1 + r/n)^(nt)
    Where:
    A = Final amount
    P = Principal amount
    r = Annual interest rate (decimal)
    n = Number of times interest is compounded per year
    t = Time in years
    """
    rate_decimal = rate / 100
    amount = principal * \
        (1 + rate_decimal / compounding_frequency) ** (compounding_frequency * time)
    interest = amount - principal
    return amount, interest


def calculate_principal_from_compound(amount, rate, time, compounding_frequency=1):
    """Calculate principal from final amount"""
    rate_decimal = rate / 100
    principal = amount / \
        (1 + rate_decimal / compounding_frequency) ** (compounding_frequency * time)
    return principal


# Examples
print("Compound Interest Calculations:")
print("=" * 35)

# Basic example
principal = 1000
rate = 5  # 5% per year
time = 2  # 2 years
compounding = 1  # Annually

amount, interest = calculate_compound_interest(
    principal, rate, time, compounding)
print(f"Principal: ${principal}")
print(f"Rate: {rate}% per year")
print(f"Time: {time} years")
print(f"Compounding: {compounding} time(s) per year")
print(f"Final Amount: ${amount:.2f}")
print(f"Interest Earned: ${interest:.2f}")

# Different compounding frequencies
print("\nDifferent Compounding Frequencies:")
p = 1000
r = 6
t = 1

frequencies = [
    ("Annually", 1),
    ("Semi-annually", 2),
    ("Quarterly", 4),
    ("Monthly", 12),
    ("Daily", 365)
]

for freq_name, freq in frequencies:
    amt, int_earned = calculate_compound_interest(p, r, t, freq)
    print("12s")

# Long-term investment
print("\nLong-term Investment:")
initial = 5000
annual_rate = 7
years = 20
comp_freq = 12  # Monthly

final_amount, total_interest = calculate_compound_interest(
    initial, annual_rate, years, comp_freq)
print(f"Initial investment: ${initial}")
print(f"Annual rate: {annual_rate}%")
print(f"Time: {years} years")
print(f"Monthly compounding")
print(f"Final amount: ${final_amount:.2f}")
print(f"Total interest: ${total_interest:.2f}")

# Rule of 72 (approximate time to double investment)
print("\nRule of 72:")
investment = 10000
rate_72 = 6
double_time = 72 / rate_72
actual_double = calculate_compound_interest(
    investment, rate_72, double_time, 1)[0]
print(f"Investment: ${investment} at {rate_72}%")
print(f"Rule of 72 says it doubles in {double_time} years")
print(f"Actual amount after {double_time} years: ${actual_double:.2f}")

# Savings goal
print("\nSavings Goal:")
goal = 100000
current_savings = 20000
years_to_save = 25
annual_rate = 5

required_principal = calculate_principal_from_compound(
    goal, annual_rate, years_to_save, 12)
additional_needed = required_principal - current_savings

print(f"Goal: ${goal}")
print(f"Current savings: ${current_savings}")
print(f"Time: {years_to_save} years at {annual_rate}%")
print(f"Monthly compounding")
print(f"Additional amount needed now: ${additional_needed:.2f}")

# Loan payment calculation (simplified)
print("\nLoan Example:")
loan_amount = 200000
interest_rate = 4.5
loan_term = 30  # years

# This is a simplified calculation - actual mortgage calculations are more complex
total_paid, total_interest_paid = calculate_compound_interest(
    loan_amount, interest_rate, loan_term, 12)
monthly_payment = total_paid / (loan_term * 12)

print(f"Loan amount: ${loan_amount}")
print(f"Interest rate: {interest_rate}%")
print(f"Term: {loan_term} years")
print(f"Total paid: ${total_paid:.2f}")
print(f"Total interest: ${total_interest_paid:.2f}")
print(f"Monthly payment (approx): ${monthly_payment:.2f}")

# Inflation impact
print("\nInflation Impact:")
investment_amount = 50000
nominal_rate = 8
inflation_rate = 3
time_period = 10

nominal_amount, _ = calculate_compound_interest(
    investment_amount, nominal_rate, time_period, 1)
inflation_factor = (1 + inflation_rate/100) ** time_period
real_value = nominal_amount / inflation_factor

print(
    f"Investment: ${investment_amount} at {nominal_rate}% for {time_period} years")
print(f"Nominal final amount: ${nominal_amount:.2f}")
print(f"Inflation rate: {inflation_rate}%")
print(f"Real value (inflation-adjusted): ${real_value:.2f}")
