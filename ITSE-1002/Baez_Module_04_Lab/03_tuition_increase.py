# -------------------------------------------------
# File Name: 03_tuition_increase.py
# Author: Florentino Báez
# Date: Baez_Module_04_Lab
# Description: At one college, the tuition for a full-time student is $8,000
# -------------------------------------------------

print("=" * 60)
print("EXERCISE 3: Tuition Increase")
print("=" * 60)

# Constants
CURRENT_TUITION = 8000  # dollars per semester
INCREASE_RATE = 0.03  # 3 percent
YEARS = 5

print(f"Current tuition: ${CURRENT_TUITION:,.2f} per semester")
print(f"Annual increase rate: {INCREASE_RATE * 100}%")
print(f"\nProjected semester tuition for the next {YEARS} years:")
print(f"\nYear\t\tTuition per Semester")
print("-" * 40)

# Calculate and display tuition for next 5 years
tuition = CURRENT_TUITION

# Loop: Iterate through each year from 1 to 5
for year in range(1, YEARS + 1):
    print(f"{year}\t\t${tuition:,.2f}")
    tuition = tuition * (1 + INCREASE_RATE)

