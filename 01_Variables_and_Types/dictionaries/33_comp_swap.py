# -------------------------------------------------
# File Name: 33_comp_swap.py
# Author: Florentino Báez
# Date: 01_Variables_and_Types
# Description: Swap keys and values in comprehension to invert dict.
# -------------------------------------------------

print("6. Swapping Keys and Values:")
print("-" * 60)
country_capital = {
    "USA": "Washington DC",
    "UK": "London",
    "France": "Paris",
    "Japan": "Tokyo"
}
print(f"Country → Capital: {country_capital}")

# Swap: use capital as key, country as value
# Note: Works only if all values are unique (no duplicate capitals)
capital_country = {capital: country for country, capital in country_capital.items()}
print(f"Capital → Country: {capital_country}")
