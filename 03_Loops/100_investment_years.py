# -------------------------------------------------
# File Name: 100_investment_years.py
# Description: Investment: amount, rate, years - capital each year
# -------------------------------------------------

amount = float(input("Amount to invest: "))
rate = float(input("Annual interest (%): ")) / 100
years = int(input("Years: "))
capital = amount
for year in range(1, years + 1):
    capital *= 1 + rate
    print(f"Year {year}: {capital:.2f} EUR")
